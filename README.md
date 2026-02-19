# WeWorkRemotely Remote Jobs Dashboard

Hey there! I'm excited to share this project I built, a fully automated web scraper and dashboard that pulls in the latest remote job trends from WeWorkRemotely.com. If you're into remote work or just curious about the job market, this tool gives you a real-time peek into what's hot in the remote job world.

## What This Project Does

I created this to help job seekers and recruiters get a quick overview of the remote job landscape. It scrapes the top 150 trending jobs, cleans up the messy data, and turns it into beautiful, interactive visualizations. No more sifting through endless listings. Just run it and see the patterns emerge!

The dashboard highlights:
- Which companies are hiring the most
- The skills that are in high demand
- How jobs break down by category and type
- Salary ranges and averages
- Where these remote jobs are located

## Cool Features

- **Smart Scraping**: Uses Selenium with undetected-chromedriver to grab fresh data without getting blocked
- **Data Magic**: Cleans and parses salaries, skills, and other details into usable formats
- **Interactive Dashboard**: Built with Streamlit and Plotly for charts that you can actually play with
- **One-Click Automation**: Makefile makes setup and running a breeze

## Tech Stack

- **Python** for the core logic
- **Selenium** & **undetected-chromedriver** for web scraping
- **Pandas** & **NumPy** for data wrangling
- **Streamlit** for the web app
- **Plotly** for the visualizations

## Getting Started

Ready to try it out? Here's how to get it running on your machine.

### What You Need

- Python 3.7 or higher
- The `make` command (comes with Linux/Mac, or install it on Windows via Chocolatey or similar)

### Step 1: Grab the Code

Clone this repo and hop into the directory:

```bash
git clone <your-repository-url>
cd selenium_job_scraper
```

### Step 2: Set Up Your Environment

Install all the Python goodies with one command:

```bash
make install
```

This reads `requirements.txt` and installs everything you need.

### Step 3: Fire It Up!

Run the whole pipeline – scraping, cleaning, and launching the dashboard:

```bash
make run
```

Your browser should open automatically to the dashboard. If not, check the terminal for the local URL (usually http://localhost:8501).

## How It All Works

The project is split into three main parts:

1. **Scraping** (`job_scraper.py`): Hits WeWorkRemotely's trending jobs pages, collects job details, and saves to CSV
2. **Cleaning** (`data_cleaning.py`): Takes the raw data, extracts salaries, normalizes text, and computes averages
3. **Dashboard** (`dashboard.py`): Loads the cleaned data and creates interactive charts

Everything's automated with the Makefile, so you don't have to run each script manually.

## Project Files

```
├── data/
│   ├── cleaned_data.csv      # Processed data for the dashboard
│   └── top_trending_jobs.csv # Raw scraped data
├── scripts/
│   ├── job_scraper.py        # The scraper
│   ├── data_cleaning.py      # Data processor
│   └── dashboard.py          # Streamlit app
├── notebooks/                # Jupyter versions for exploration
├── Makefile                  # Automation magic
├── requirements.txt          # Python dependencies
└── README.md                 # This file!
```

## Makefile Shortcuts

- `make install` - Get all packages
- `make all` - Run scraping and cleaning only
- `make run` - Full pipeline + dashboard
- `make clean` - Wipe the data folder for a fresh start

## A Bit About Me

I'm passionate about using code to solve real-world problems, especially around data and automation. This project combines web scraping, data analysis, and visualization – skills I've picked up through self-learning and projects like this. If you find it useful or have ideas to improve it, I'd love to hear from you!

## License

Feel free to use this for your own projects. Just give credit where it's due!
