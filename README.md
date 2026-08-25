![adze](asset/adze_logo_main.svg)
> A production level, lightweight, and rapid webhook normalization tool.

[![.github/workflows/Continuous%20Integration.yml](https://img.shields.io/github/actions/workflow/status/bugra-ozer/adze/Continuous%20Integration.yml?style=flat-square&logo=github&label=Continuous%20Integration)](https://github.com/bugra-ozer/adze/Continuous%20Integration.yml)
![Python](https://img.shields.io/badge/Python-v3.14%2B-3776AB?style=flat-square&logo=python&logoColor=white&color=3776AB)
![Flask](https://img.shields.io/badge/v3.1.3%2B-3776AB?style=flat-square&logo=Flask&label=Flask)
![PostgreSQL](https://img.shields.io/badge/v18.6%2B-3776AB?style=flat-square&logo=PostgreSQL&label=PostgreSQL&logoColor=white)
![Docker](https://img.shields.io/badge/v29.6.2%2B-3776AB?style=flat-square&logo=Docker&label=Docker&logoColor=white)
![Auth](https://img.shields.io/badge/hmac-000000?style=flat-square&logo=jsonwebtokens&logoColor=white&label=Auth)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0%2B-3776AB?style=flat-square&logo=sqlalchemy&logoColor=red&color=red)

---

## What is it?

Adze is a centralized webhook normalizer and relay engine designed to securely ingest, verify, and standardize asynchronous events from multiple third-party providers like GitHub, Stripe, and Twilio.

Meaning? Often than not, the providers of webhooks present the data with different structure that tend to change over time. Fixing or sometimes even identifying the cause costs time, money or both. Adze aims to unify webhook envelopes under one roof.

The service is built on a modern Python stack, operating as a lightweight Flask REST application. It is fully containerized with Docker and utilizes SQLAlchemy alongside PostgreSQL for reliable schema management and data handling. 

---

## Architecture

![Architecture](asset/adze_architecture.svg)

---

## Tech Stack
 
| Layer           | Technology                          |
|-----------------|-------------------------------------|
| Language        | Python 3.14+                        |
| API             | Flask 3.1.3+                        |
| Database Tools  | SQLAlchemy                          |
| Database Deploy | Postgres                            |
| Authentication  | hmac, hashlib                       |
| Testing         | pytest, mock, unittest              |
| Dev-Tools       | Docker, python-dotenv               |

## Getting Started

```bash
## Requirements
- Python 3.14+
- Docker Desktop

## Running

# Clone the repo
git clone https://github.com/bugra-ozer/adze
cd adze

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env  # fill in DATABASE_URL, GITHUB_WEBHOOK_SECRET, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

# Start PostgreSQL
docker-compose up -d

# Run the app
python main.py
```

## Author

**Bugra Ozer** — [github.com/bugra-ozer](https://github.com/bugra-ozer)
