# Install required packages
install: requirements.txt
	python -m pip install -r requirements.txt

# 3. Generate Dashboard

# 2. Clean Scraped Data
data/cleaned_data.csv: scripts/data_cleaning.py data/top_trending_jobs.csv
	python data_cleaning.py

# 1. Scrape to Generate Dataset
data/top_trending_jobs.csv: scripts/job_scraper.py
	python job_scraper.py