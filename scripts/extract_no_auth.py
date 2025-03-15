import requests
import json
import pandas as pd
import time

# API URL
LIST_VACANCY_URL = "https://api-rbb.fhcibumn.id/general/career/list-vacancy"

# Headers (No Authentication)
HEADERS_NO_AUTH = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://rekrutmenbersama2025.fhcibumn.id",
    "priority": "u=1, i",
    "referer": "https://rekrutmenbersama2025.fhcibumn.id/",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# Storage for all vacancies
all_jobs = []
total_applicants = 0
page = 7  # Start from Page 7

while True:
    print(f"Fetching vacancies from Page {page}...")

    payload = {
        "page": page,
        "size": 15,
        "job_title": "",
        "stream_id": [],
        "company_id": [],
        "experience_level": [],
        "education_level": [],
        "major_id": [],
        "search": ""
    }

    response = requests.post(LIST_VACANCY_URL, headers=HEADERS_NO_AUTH, json=payload)

    if response.status_code != 201:
        print(f"🚨 Stopping at Page {page} - Received Status Code {response.status_code}")
        break

    data = response.json()
    job_list = data.get("data", [])

    if not job_list:
        print(f"✅ No more jobs found. Stopping at Page {page}.")
        break

    # Collect vacancies and count applicants
    for job in job_list:
        job["total_applied"] = int(job.get("total_applied", 0))  # Extract number of applicants
        total_applicants += job["total_applied"]  # Sum up applicants
        all_jobs.append(job)

    page += 1
    time.sleep(1)  # Prevent rate-limiting

# Convert to DataFrame
df = pd.DataFrame(all_jobs)

# Save to CSV
df.to_csv("data/bumn_jobs_no_auth.csv", index=False)

# Print Total Applicants
print(f"✅ Total Applicants Across Pages 7+: {total_applicants}")
print("✅ Data saved to data/bumn_jobs_no_auth.csv")