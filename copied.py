import pandas as pd
import os
import requests
import datetime as dt
import json
from utils import send_email


def lambda_handler(event, context):
    df = pd.DataFrame(
        columns=['date', 'name', 'address', 'pincode', 'district_name', 'from', 'to', 'vaccine', 'fee_type',
                 'min_age_limit', 'available_capacity'])
    i = 0
    # Convert from UTC to IST. pytz is missing that's why hardcoding
    date = (dt.datetime.now() + dt.timedelta(hours=5, minutes=30)).strftime('%d-%m-%Y')
    district_ids = [*range(140, 151)] + [188, 199]  # Added Gurgaon and Faridabad
    for district_id in district_ids:
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'authority': 'cdn-api.co-vin.in'
        }
        r = requests.get(url, headers=headers, verify=False)
        d = json.loads(r.text)
        for data in d['centers']:
            for session_data in data['sessions']:
                df.loc[i, 'name'] = data.get('name')
                df.loc[i, 'address'] = data.get('address')
                df.loc[i, 'pincode'] = data.get('pincode')
                df.loc[i, 'district_name'] = data.get('district_name')
                df.loc[i, 'from'] = data.get('from')
                df.loc[i, 'to'] = data.get('to')
                df.loc[i, 'fee_type'] = data.get('fee_type')
                df.loc[i, 'date'] = session_data.get('date')
                df.loc[i, 'vaccine'] = session_data.get('vaccine')
                df.loc[i, 'min_age_limit'] = session_data.get('min_age_limit')
                df.loc[i, 'available_capacity'] = session_data.get('available_capacity')
                i += 1

    df_ = df[(df.min_age_limit == 18) & (df.available_capacity > 0) & (df.vaccine == 'COVAXIN')]
    print(f'Found {len(df_)} vaccination slots(18+) near you!')
    if len(df_) > 0:
        df_['Address'] = df_.apply(lambda x: f"{x['name']}, {x['address']} - {x['pincode']}", axis=1)
        df_['Timings'] = df_.apply(lambda x: f"{x['from']} - {x['to']}", axis=1)
        df_.rename(columns={'date': 'Date', 'district_name': 'District', 'vaccine': 'Vaccine',
                            'fee_type': 'Fee', 'available_capacity': 'Available Capacity'}, inplace=True)
        df_ = df_[['Date', 'Address', 'District', 'Vaccine', 'Fee', 'Available Capacity']]
        df_.reset_index(drop=True, inplace=True)

        HTML = df_.to_html()
        TEXT = df_.to_string()
        SUBJECT = f"Found {len(df_)} vaccination slots(18+) near you!"
        RECIPIENTS = os.getenv('RECIPIENTS').split(',')

        send_email(
            'anshuls235@gmail.com',
            RECIPIENTS,
            'ap-south-1',
            subject=SUBJECT,
            body_text=TEXT,
            body_html=HTML
        )