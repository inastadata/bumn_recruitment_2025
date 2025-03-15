# BUMN Recruitment 2025 Job Scraper

This project contains Python scripts to extract job vacancies from the **BUMN Recruitment 2025** portal. The scripts fetch job vacancy data with and without authentication, process the data, and save it as CSV files for further analysis.

## 📌 Features

- Fetches job vacancies from the **BUMN Recruitment 2025** API.
- Supports both **authenticated** and **unauthenticated** requests.
- Extracts **total applicants** for each job posting.
- Saves data in a structured **CSV format**.
- Implements **rate limiting** to avoid excessive requests.

## 📂 Project Structure
bumn_recruitment_2025/
│── scripts/
│   ├── extract_no_auth.py      # Fetch job vacancies without authentication
│   ├── extract_auth.py         # Fetch job vacancies with authentication
│── data/                       # Folder to store extracted CSV files
│── .gitignore                   # Ignore cache, virtual env, and CSV files
│── README.md                    # Project documentation

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/inastadata/bumn_recruitment_2025.git
   cd bumn_recruitment_2025

2.	**Create a virtual environment (optional but recommended)**:
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3.	**Install dependencies**:
pip install -r requirements.txt

## 🚀 Usage

1️⃣ **Extract job vacancies without authentication**

This script fetches job vacancies without requiring authentication.

python scripts/extract_no_auth.py

	•	The script starts from page 7 and continues fetching jobs until no more vacancies are available.
	•	The data is saved to: data/bumn_jobs_no_auth.csv
	•	The total number of applicants across all pages is displayed.


2️⃣ **Extract job vacancies with authentication**

This script fetches job vacancies using a Bearer Token for authentication.

python scripts/extract_auth.py

	•	Requires a valid Bearer Token (replace "null" in BEARER_TOKEN).
	•	Fetches job listings and their total applicant count.
	•	Saves the extracted data to: data/bumn_jobs_auth.csv
	•	The total number of applicants for Page 1 is displayed.

  🔒 Security Considerations
	•	Do not hardcode sensitive credentials in the scripts.
	•	Store authentication tokens in a .env file or configuration file that is excluded via .gitignore.
	•	Avoid making too many requests in a short period to prevent rate-limiting.

🏗️ Future Improvements
	•	Implement multi-page fetching for authenticated requests.
	•	Add error handling for API failures.
	•	Store credentials securely using environment variables.

📄 License

This project is licensed under the MIT License.
