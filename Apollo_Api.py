import pandas as pd
import requests


def load_data(input_file):
    return pd.read_csv(input_file)

def save_data(df, output_file):
    df.to_csv(output_file, index=False)

def get_email_from_apollo(url):
    api_url = 'https://api.apollo.io/v1/people/match'
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': 'X' 
    }
    data = {
        "linkedin_url": url,
        "reveal_personal_emails": True
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        person_data = response.json().get('person', {})
        email = person_data.get('email', '')
        return email
    else:
        print(f"Query error code: {url} : {response.status_code} - {response.text}")
        return ''

def main(input_file, output_file, start_index=1, end_index=200):
    df = load_data(input_file)
    for index in range(start_index, min(end_index, len(df))):
        row = df.iloc[index]
        url = row['URL']
        if pd.notna(url):
            email = get_email_from_apollo(url)
            df.at[index, 'Pro_Email'] = email
    save_data(df, output_file)

input_file = 'input.csv'  
output_file = 'output.csv'  

main(input_file, output_file)
