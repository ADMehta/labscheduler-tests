# README.md
# Provides an overview of the project, setup instructions, how to run tests locally,
# how the CI pipeline works, and how to view test reports.
# Also includes notes on test structure and design decisions.

# 🧪 Lab Scheduler API Test Suite

This project contains a comprehensive set of automated tests for the Lab Scheduler API. It validates the full lifecycle of a lab entity using RESTful operations: **Create**, **Read**, **Update**, and **Delete**—along with negative test scenarios to ensure robust validation.

---

## 🚀 Features

- ✅ End-to-end API workflow testing
- 🔁 Reusable fixtures for consistent test data
- ❌ Negative test scenarios for input validation
- 📊 HTML reports for each test run
- 🧩 Easily integrable into CI/CD pipelines

---

## 📦 Project Structure

```
labscheduler-tests/
├── tests/
│   └── test_lab_workflow.py       # Main test suite
├── utils/
│   └── api_client.py              # API wrapper functions
├── .github/
│   └── workflows/
│       └── api-tests.yml          # GitHub Actions workflow
├── report.html                    # Generated test report (after execution)
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/labscheduler-tests.git
cd labscheduler-tests
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Backend URL

Update `utils/api_client.py` with your backend API base URL:

```python
BASE_URL = "https://your-backend-url.replit.app/api"
```

---

## 🧪 Running Tests

### Run All Tests with HTML Report

```bash
pytest tests/ --html=report.html
```

### View Report

Open `report.html` in your browser to view detailed results.

---

## 🔁 Reusability & Multiple Executions

- Tests use fixtures to isolate data and avoid conflicts.
- Each run generates a fresh `report.html`.
- You can execute the suite multiple times without manual cleanup.
- Logs and results are preserved per run.

---

## ❌ Negative Test Coverage

Includes tests for:
- Missing required fields
- Invalid data formats
- Expected failure responses

---

## 🧩 CI/CD Integration (Extra Credit)

This project includes a GitHub Actions workflow (`.github/workflows/api-tests.yml`) that:

- Runs tests automatically on every push to `main`
- Installs dependencies
- Generates and uploads the HTML report as an artifact

### Example Workflow Trigger

```yaml
on:
  push:
    branches: [ main ]
  workflow_dispatch:
```

### Artifact Access

After each run, the `report.html` is available in the GitHub Actions UI under **Artifacts**.

---

## 📬 Contact

For questions or contributions, reach out to [apeksha.d.mehta@gmail.com].

---

## 🏁 Final Notes

This test suite is designed to be:
- Easy to set up
- Reliable across environments
- Extendable for future endpoints

Happy testing! 🧪
```
--