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

Adze is a centralized webhook normalizer and relay engine designed to securely ingest, verify, and standardize asynchronous events from multiple third-party providers like GitHub, Stripe, and Twilio. Adze strips away the structural inconsistencies of disparate webhook formats, packing them into a single, unified data envelope.

The service is built on a modern Python stack, operating as a lightweight Flask REST application. It is fully containerized with Docker and utilizes SQLAlchemy alongside PostgreSQL for reliable schema management and data handling. Operating as a secure, always-on middleman, Adze bridges the gap between external platforms and internal infrastructure, safely forwarding normalized event data downstream to stakeholders.

---

## Architecture

![Architecture](asset/adze_architecture.svg)

---

## Tech Stack
 
| Layer           | Technology                          |
|-----------------|-------------------------------------|
| Language        | Python 3.14+                        |
| API             | Flask 3.1+                          |
| Database Tools  | SQLAlchemy                          |
| Database Deploy | Postgres                            |
| Authentication  | hmac, hashlib                       |
| Testing         | pytest, mock, unittest              |
| Dev-Tools       | Docker, python-dotenv               |
