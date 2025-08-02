# WWR Remote Jobs Dashboard 

This project automatically scrapes the top 150 trending job listings from weworkremotely.com, cleans the collected data, and presents the insights in an interactive web dashboard built with Streamlit.

***

## Project Overview

The goal of this project is to provide a clear and up-to-date overview of the remote job market based on data from one of the leading remote job boards. The entire pipeline is automated using a Makefile, from data collection to launching the visualization dashboard.

The dashboard provides insights into:
- Top hiring companies
- Most in-demand skills
- Job distribution by category and type
- Salary benchmarks and distribution
- Regional job availability

## Key Features

- **Automated Scraping:** Uses Selenium to collect fresh job data.
- **Data Cleaning:** Processes raw data into a structured format, parsing salaries and skills.
- **Interactive Dashboard:** Visualizes key trends using Plotly and Streamlit.
- **Makefile Automation:** Simple commands (`make install`, `make run`) to set up and run the entire project.

## 📂 Project Structure

The project is organized into the following directories and files:

├── data/
│   ├── cleaned_data.csv        # The final, cleaned data used by the dashboard.
│   └── top_trending_jobs.csv   # The raw, scraped data.
│
├── scripts/
│   ├── job_scraper.py          # Script to scrape job data from the website.
│   ├── data_cleaning.py        # Script to clean and process the raw data.
│   └── dashboard.py            # The Streamlit application script.
│
├── .gitignore                  # Specifies files to be ignored by Git (e.g., *.csv).
├── Makefile                    # Defines the automated workflow for the project.
└── requirements.txt            # Lists all Python dependencies for easy installation.

## Getting Started

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.7+
- `make` command installed (standard on Linux/macOS, can be installed on Windows)

### 1. Clone the Repository

First, clone the project repository to your local machine.

```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2. Install Dependencies

Install all the required Python packages by running the following command. This will read the `requirements.txt` file and set up your environment.

```bash
make install
```
### 3. Run the Application

Now, you can run the entire project with a single command. This will execute the data pipeline (scraping and cleaning) and then launch the dashboard in your web browser.

```bash
make run_dashboard
```
## Makefile Commands

This project uses a `Makefile` to automate common tasks.
- `make install`: Installs all Python packages listed in `requirements.txt`.
- `make all`: Runs the complete data pipeline (scraping and cleaning) without launching the dashboard.
- `make run`: Updates the data by running the `all` pipeline and then launches the Streamlit dashboard. This is the main command you will use.
- `make clean`: Deletes all generated CSV files from the `data/` folder, allowing you to start fresh.
