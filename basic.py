import csv
from jobspy import scrape_jobs

from jobspy.model import Country



jobs = scrape_jobs(
    # site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google", "bayt", "naukri"],
    site_name=["linkedin", "google", "indeed", "zip_recruiter", "glassdoor"],
    search_term="summer part time",
    google_search_term="summer part time in toronto area",
    location="Toronto, Canada",
    results_wanted=80,
    hours_old=72,
    country_indeed='Canada',
    
    # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("./backend_toronto_1.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel