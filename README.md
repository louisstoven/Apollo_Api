# LinkedIn Email Finder

This project provides a script to automatically retrieve professional email addresses from LinkedIn profile URLs using the Apollo API. The script reads a list of LinkedIn profile URLs from your Linkedin contact export, retrieves the associated email addresses, and stores the results in a new CSV file. 

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)

## Features

- **Automated Email Retrieval**: Retrieves email addresses associated with LinkedIn profiles via the Apollo API.
- **CSV Input/Output**: Reads profile URLs from a CSV file and saves the results in an output CSV.
- **Configurable Range**: Allows specifying the range of rows to process, enabling selective email retrieval from large datasets.

## Requirements

- Python 3.6+
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/)

## Installation

1. Clone the repository:
    ```bash
    git clone __
    cd __
    ```

2. Install the required Python packages:
    ```bash
    pip install pandas requests
    ```

## Usage

1. Prepare your contacts export CSV file.
2. Set your Apollo API key in the `get_email_from_apollo` function in `email_finder.py`:
    ```python
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'YOUR_API_KEY'
    }
    ```

3. Run the script with the following command:
    ```bash
    python email_finder.py
    ```

4. The script will generate an `output.csv` file with the retrieved email addresses.
