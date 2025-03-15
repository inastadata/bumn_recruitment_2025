import requests
import json
import pandas as pd
import os

# API URLs
LIST_VACANCY_URL = "https://api-rbb.fhcibumn.id/general/career/list-vacancy"
VACANCY_APPLIED_URL = "https://api-rbb.fhcibumn.id/general/career/vacancy-applied"

# Bearer Token (Move this to a config file for security)
BEARER_TOKEN = "null"

# Headers (With Authentication)
HEADERS_AUTH = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": f"Bearer {BEARER_TOKEN}",
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

# Fetch vacancies from Page 1
print("Fetching job vacancies from Page 1...")
payload_vacancy = {
    "page": 1,
    "size": 15,
    "job_title": "",
    "stream_id": [],
    "company_id": [],
    "experience_level": [],
    "education_level": [],
    "major_id": [],
    "search": ""
}

response_vacancy = requests.post(LIST_VACANCY_URL, headers=HEADERS_AUTH, json=payload_vacancy)

if response_vacancy.status_code != 201:
    print(f"🚨 Error fetching Page 1 - Status Code: {response_vacancy.status_code}")
    exit()

vacancy_data = response_vacancy.json().get("data", [])

# Extract vacancy IDs
vacancy_ids = [job["vacancy_id"] for job in vacancy_data]

# Fetch total applicants using vacancy-applied API
print("Fetching total applicants for Page 1 jobs...")
payload_applied = {"vacancy_id": vacancy_ids}
response_applied = requests.post(VACANCY_APPLIED_URL, headers=HEADERS_AUTH, json=payload_applied)

if response_applied.status_code != 201:
    print(f"🚨 Error fetching applicant data - Status Code: {response_applied.status_code}")
    exit()

applied_data = {item["vacancy_id"]: item["total_applied"] for item in response_applied.json().get("data", [])}

# Merge data
for job in vacancy_data:
    job["total_applied"] = int(applied_data.get(job["vacancy_id"], 0))

# Calculate total applicants
total_applicants = sum(job["total_applied"] for job in vacancy_data)

# Convert to DataFrame
df = pd.DataFrame(vacancy_data)

# Ensure the 'data' directory exists
os.makedirs("data", exist_ok=True)

# Save to CSV
df.to_csv("data/bumn_jobs_auth.csv", index=False)

# Print Total Applicants
print(f"✅ Total Applicants (Page 1-6): {total_applicants}")
print("✅ Data saved to data/bumn_jobs_auth.csv")