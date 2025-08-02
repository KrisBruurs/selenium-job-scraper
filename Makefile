# Run entire pipeline
all: data/cleaned_data.csv

# Install required packages
install: requirements.txt
	@echo "---Installing Required Packages---"
	python -m pip install -r requirements.txt

# 3. Generate and Run Dashboard
run: data/cleaned_data.csv scripts/dashboard.py
	@echo: "---Finished... Generating Dashboard Now---"
	streamlit run scripts/dashboard.py

# 2. Clean Scraped Data
data/cleaned_data.csv: scripts/data_cleaning.py data/top_trending_jobs.csv
	@echo "---Step 2: Cleaning Raw Scraped Data---"
	python scripts/data_cleaning.py

# 1. Scrape to Generate Dataset
data/top_trending_jobs.csv: scripts/job_scraper.py
	@echo "---Step 1: Scraping WeWorkRemotely---"
	python scripts/job_scraper.py

# Clean Generated Data
clean:
	@echo "---Cleaning Now---"
	del data/*.csv