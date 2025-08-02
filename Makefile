# Run entire pipeline
all: data/cleaned_data.csv

# Install required packages
install: requirements.txt
	python -m pip install -r requirements.txt

# 3. Generate and Run Dashboard
run_dashboard: data/cleaned_data.csv scripts/dashboard.py
	streamlit run scripts/dashboard.py

# 2. Clean Scraped Data
data/cleaned_data.csv: scripts/data_cleaning.py data/top_trending_jobs.csv
	python scripts/data_cleaning.py

# 1. Scrape to Generate Dataset
data/top_trending_jobs.csv: scripts/job_scraper.py
	python scripts/job_scraper.py

# Clean Generated Data
clean:
	rm -f data/*.csv