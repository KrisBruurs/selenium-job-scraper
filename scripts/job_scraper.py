import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
import os

def accept_cookies(driver_instance):
    """Attempts to accept cookie consent popups."""
    try:
        WebDriverWait(driver_instance, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.fc-button, button.adroll_button_text, #adroll_consent_allow_all, .fc-cta-consent'))).click()
        time.sleep(1)
        print("Cookies accepted (or attempted).")
    except Exception:
        print("Cookie buttons not found or already accepted/handled.")

def scrape_weworkremotely():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized") 

    driver = uc.Chrome(options=options)
    print("WebDriver initialized.")

    base_url = "https://weworkremotely.com/top-trending-remote-jobs?page="
    urls = [f"{base_url}{i}" for i in range(1, 4)] 

    all_job_links = []
    job_data = [] 

    try: 
        print("\n--- Phase 1: Collecting Job Links ---")
        for index, url in enumerate(urls):
            driver.get(url)
            print(f"Scraping page {index + 1}: {url}")

            if index == 0: 
                accept_cookies(driver)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(3, 6))

            job_links_elements = driver.find_elements(By.CSS_SELECTOR, "section.jobs li > a")
            print(f"Found {len(job_links_elements)} potential job listings on page {index + 1}")

            page_links = [
                link.get_attribute("href")
                for link in job_links_elements
                if link.get_attribute("href") and link.get_attribute("href") != "https://weworkremotely.com/"
            ]
            all_job_links.extend(page_links)

            time.sleep(random.uniform(2, 5)) 

        print(f"\nTotal unique job links collected: {len(all_job_links)}")
        all_job_links = list(set(all_job_links))
        print(f"Total unique job links after deduplication: {len(all_job_links)}")


        print("\n--- Phase 2: Scraping Detailed Job Data ---")
        for i, link in enumerate(all_job_links):
            print(f"Processing job {i+1}/{len(all_job_links)}: {link}")
            try:
                driver.get(link)

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lis-container__header__hero__company-info__title')))

                job_title = driver.find_element(By.CLASS_NAME, 'lis-container__header__hero__company-info__title').text
                company_block = driver.find_element(By.CLASS_NAME, 'lis-container__job__sidebar__companyDetails__info')
                company_title = company_block.find_element(By.CLASS_NAME, 'lis-container__job__sidebar__companyDetails__info__title').text

                try:
                    jobs_posted_text = WebDriverWait(company_block, 10).until( 
                        EC.visibility_of_element_located((By.CLASS_NAME, 'lis-container__job__sidebar__companyDetails__info__jobs-posted'))
                    ).text.strip()
                except:
                    jobs_posted_text = "NA"
                    print(f"  Warning: 'Jobs Posted' not found for {link}")

                job_block = driver.find_element(By.CLASS_NAME, 'lis-container__job__sidebar__job-about')
                category_items = job_block.find_elements(By.CLASS_NAME, 'lis-container__job__sidebar__job-about__list__item')

                job_details = {}
                for item in category_items:
                    lines = item.text.strip().split("\n")
                    if len(lines) >= 2:
                        label = lines[0].strip()
                        value = "\n".join(lines[1:]).strip()
                        job_details[label] = value

                region_raw = job_details.get("Region", "NA")
                region_extracted = "NA"
                if " Only" in region_raw:
                    region_extracted = region_raw.split(" Only")[0].strip() + " Only"
                elif region_raw != "NA": 
                    region_extracted = region_raw 
                skills_list = []
                try:
                    skills_container = driver.find_element(By.XPATH, "//li[contains(., 'Skills')]//div[@class='boxes']")
                    skill_elements = skills_container.find_elements(By.CSS_SELECTOR, "span.box")
                    skills_list = [skill.text.strip() for skill in skill_elements]
                except Exception as e:
                    skills_list = [] 
    
                skills_clean = ', '.join(skills_list) if skills_list else "NA"

                job_entry = {
                    "Ranking": i + 1, 
                    "Job Title": job_title,
                    "Company": company_title,
                    "Jobs Posted": jobs_posted_text.replace("Jobs posted: ", ""),
                    "Job Type": job_details.get("Job type", "NA"),
                    "Category": job_details.get("Category", "NA"),
                    "Salary": job_details.get("Salary", "NA"),
                    "Skills": skills_clean,
                    "Region": region_extracted,
                    "Link": link
                }

                job_data.append(job_entry)

            except Exception as e:
                print(f"Error scraping details for link {link}: {e}")

            time.sleep(random.uniform(1, 3))

    except Exception as e:
        print(f"Critical error during scraping process: {e}")
    finally:
        driver.quit()
        print("\nWebDriver closed.")

    if job_data: 
        output_folder = "data"
        output_file_name = "top_trending_jobs.csv"
        os.makedirs(output_folder, exist_ok=True)
        full_path = os.path.join(output_folder, output_file_name)
        with open(full_path, "w", newline='', encoding='utf-8') as f:
            fieldnames = list(job_data[0].keys()) 
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(job_data)
        print(f"Scraped {len(job_data)} jobs and saved to '{output_file_name}'")
    else:
        print("No job data scraped. CSV file not created.")

if __name__ == '__main__':
    scrape_weworkremotely()