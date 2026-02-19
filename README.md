# WeWorkRemotely Remote Jobs Dashboard

This project provides a fully automated solution for scraping and visualizing remote job trends from WeWorkRemotely.com. It collects data on the top trending job listings, processes the information, and presents insights through an interactive web dashboard.

## Overview

The goal of this project is to offer a comprehensive view of the remote job market by leveraging data from a leading remote job platform. The entire workflow, from data collection to visualization, is automated using a Makefile for ease of use.

The dashboard provides key insights into:
- Top hiring companies
- In-demand skills
- Job distribution by category and type
- Salary ranges and averages
- Regional job availability

## Features

- **Automated Scraping**: Utilizes Selenium with undetected-chromedriver to collect fresh job data efficiently.
- **Data Processing**: Cleans and structures raw data, including salary parsing and skill extraction.
- **Interactive Dashboard**: Built with Streamlit and Plotly for dynamic visualizations.
- **Automation**: Makefile enables simple setup and execution of the entire pipeline.

## Tech Stack

- **Python** for core functionality
- **Selenium** & **undetected-chromedriver** for web scraping
- **Pandas** & **NumPy** for data manipulation
- **Streamlit** for the web application
- **Plotly** for data visualization

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.7 or higher
- The `make` command (available on Linux/macOS; install via Chocolatey on Windows)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KrisBruurs/selenium-job-scraper
   cd selenium_job_scraper
   ```

2. Install dependencies:

   ```bash
   make install
   ```

   This command installs all required Python packages from `requirements.txt`.

### Usage

To run the full pipeline (scraping, cleaning, and launching the dashboard):

```bash
make run
```

The dashboard will open in your default web browser. If it does not, navigate to the provided local URL (typically http://localhost:8501).

## How It Works

The project consists of three main components:

1. **Scraping** (`job_scraper.py`): Accesses WeWorkRemotely's trending jobs pages, extracts job details, and saves data to CSV.
2. **Data Cleaning** (`data_cleaning.py`): Processes raw data by extracting salaries, normalizing text, and calculating averages.
3. **Dashboard** (`dashboard.py`): Loads processed data and generates interactive charts using Streamlit and Plotly.

The Makefile automates the workflow, eliminating the need to execute scripts individually.

## Project Structure

```
├── data/
│   ├── cleaned_data.csv      # Processed data for the dashboard
│   └── top_trending_jobs.csv # Raw scraped data
├── scripts/
│   ├── job_scraper.py        # Scraping script
│   ├── data_cleaning.py      # Data processing script
│   └── dashboard.py          # Streamlit application
├── notebooks/                # Jupyter notebooks for exploration
├── Makefile                  # Automation script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Makefile Commands

- `make install`: Installs Python dependencies.
- `make all`: Executes scraping and cleaning without launching the dashboard.
- `make run`: Runs the complete pipeline and starts the dashboard.
- `make clean`: Removes generated CSV files for a fresh start.

## License

This project is open-source. Feel free to use and modify it, with appropriate attribution.
