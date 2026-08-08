![adze](asset/adze_logo_main.svg)
> A production level, lightweight, and rapid webhook normalization tool.

![Python](https://img.shields.io/badge/Python-v3.14%2B-3776AB?style=flat-square&logo=python&logoColor=white&color=3776AB)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0%2B-3776AB?style=flat-square&logo=sqlalchemy&logoColor=red&color=red)
![Auth](https://img.shields.io/badge/Hashes-000000?style=flat-square&logo=jsonwebtokens&logoColor=white&label=Auth)
![Flask](https://img.shields.io/badge/v3.1%2B-3776AB?style=flat-square&logo=Flask&label=Flask)

---

## What is it?

Adze is a centralized webhook normalizer and relay engine designed to securely ingest, verify, and standardize asynchronous events from multiple third-party providers like GitHub, Stripe, and Twilio. Adze strips away the structural inconsistencies of disparate webhook formats, packing them into a single, unified data envelope.

The service is built on a modern Python stack, operating as a lightweight Flask REST application. It is fully containerized with Docker and utilizes SQLAlchemy alongside PostgreSQL for reliable schema management and data handling. Operating as a secure, always-on middleman, Adze bridges the gap between external platforms and internal infrastructure, safely forwarding normalized event data downstream to stakeholders.

---

## Tech Stack
 
| Layer           | Technology                          |
|-----------------|-------------------------------------|
| Language        | Python 3.14+                        |
| API             | Flask 3.1+                          |
| Database Tools  | SQLAlchemy                          |
| Database Deploy |                                     |
| Authentication  | hmac, hashlib                       |
| Config          | python-dotenv                       |
| Deployment      | Render (web service), Gunicorn WSGI |