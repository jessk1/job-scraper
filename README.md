# Job Scraper (Indeed)
A Python-based web scraper that extracts job listings from **Indeed** based on Job Title and Location, then saves them as a CSV file.

## Features
- Scrapes **job title, company, location and job link**
- Saves results in a **CSV file**
- Supports **user-defined search** (role, location, pages)

## Installation
**1. Clone the repository**
```bash
git clone https://github.com/jessk1/job-scraper.git
cd job-scraper
```
**2. Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage
Run the scipt and enter job details:
```bash
python job_scraper.py
```
Then input:
- **Job Title:** _Data Analyst_
- **Location:** _New York_
- **Pages to Scrape:** _2_

## Future Enhancements
- Add support for **LinkedIn & Glassdoor**
-Convert to **Flask API** for automation
- Store jobs in a **database**

## License
This project is **MIT Licensed**. Feel free to use & modify!