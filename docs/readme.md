<div align="center">

# venmo-requester <br> 🤖🗓️💰

[![ci](https://img.shields.io/github/actions/workflow/status/sherif-attia/venmo-requester/ci.yml?branch=main&label=ci&logo=github)](https://github.com/sherif-attia/venmo-requester/actions/workflows/ci.yml)
[![version](https://img.shields.io/github/v/release/sherif-attia/venmo-requester?color=success&logo=github)](https://github.com/sherif-attia/venmo-requester/releases)
[![coverage](https://img.shields.io/codecov/c/github/sherif-attia/venmo-requester?logo=codecov&logoColor=white)](https://codecov.io/gh/sherif-attia/venmo-requester)
[![python](https://img.shields.io/badge/python-3.13%20%7C%20stable-success?logo=python&logoColor=white)](https://devguide.python.org/versions/#full-chart)

<br>

> Auto-request money from friends based on a Google Sheet.

</div>

## 📊 Google Sheet Format

| Username            | Note                   | Amount | Frequency | Payment Date |
|---------------------|------------------------|--------|-----------|--------------|
| george-bush-2       | 🏠 Rent                | $3,000 | Monthly   | 1           |
| george-bush-2       | 🔌 Utilities           | $500   | Monthly   | 5           |
| donald-trump-$$$    | 📺 YouTube Premium     | $125   | Monthly   | 10          |
| barack-obama        | 💳 Costco Membership   | $100   | Yearly    | 04-20       |
| bill-clinton-69     | 🍿 Netflix Family Plan | $75    | Yearly    | 09-12       |

## ⏰ Schedule

- Runs daily at **10 AM**
- Sends Venmo requests for rows matching today's date
