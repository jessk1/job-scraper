import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_job_listings(job_title, location, num_pages=1):
    """Scrapes job listings from Indeed based on job title and location."""

    base_url = "https://www.indeed.com/jobs"
    job_title = "+".join(job_title.split())  # Format job title for URL
    location = "+".join(location.split())  # Format location for URL

    job_listings = []

    for page in range(0, num_pages * 10, 10):  # Pagination (10 results per page)
        url = f"{base_url}?q={job_title}&l={location}&start={page}"
        headers = {"User-Agent": "Mozilla/5.0"}  # Avoid bot detection
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch data (Status Code: {response.status_code})")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="job_seen_beacon")

        for job in jobs:
            title = job.find("h2", class_="jobTitle")
            company = job.find("span", class_="companyName")
            location = job.find("div", class_="companyLocation")
            job_link = job.find("a", class_="jcs-JobTitle")

            if title and company and location and job_link:
                job_listings.append({
                    "Title": title.text.strip(),
                    "Company": company.text.strip(),
                    "Location": location.text.strip(),
                    "Link": "https://www.indeed.com" + job_link["href"],
                })

    return job_listings

def save_to_csv(job_listings, filename="jobs.csv"):
    """Saves job listings to a CSV file."""
    df = pd.DataFrame(job_listings)
    df.to_csv(filename, index=False)
    print(f"Saved {len(job_listings)} jobs to {filename}")

if __name__ == "__main__":
    job_title = input("Enter job title: ")
    location = input("Enter job location: ")
    num_pages = int(input("How many pages to scrape? (Each page = 10 jobs): "))

    job_listings = get_job_listings(job_title, location, num_pages)

    if job_listings:
        save_to_csv(job_listings)
        print("Scraping complete! Check the CSV file.")
    else:
        print("No jobs found. Try a different search.")