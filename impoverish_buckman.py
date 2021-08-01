import requests
from time import sleep
from sql_methods import get_phone_number, check_table, insert_number

def read_phone_number():
    phone_number = get_phone_number()[1]
    is_already_used = check_table(phone_number)
    if is_already_used is None:
        insert_number('already_used_phone_numbers', phone_number)
        return phone_number
    return None

def validate_number(phone_number):
    url = f'https://4uryubhk96.execute-api.us-east-1.amazonaws.com/prod/lookupcarrier/{phone_number}'
    carrier_info = requests.get(url).json()
    print(carrier_info)
    carrier_name = carrier_info['carrier']['name']
    carrier_mcc_mnc = str(carrier_info['carrier']['mobile_country_code']) + '-' + str(carrier_info['carrier']['mobile_network_code'])
    return [carrier_name, carrier_mcc_mnc]

def sign_number_up(phone_number, carrier_name, carrier_mcc_mnc):
    corgi_data = {
        'token': '43ni0vn00fne0',
        'name': 'Captain Falcon',
        'phone': phone_number,
        'carrier_name': carrier_name,
        'carrier_mcc_mnc': carrier_mcc_mnc,
        'message': "Sorry if you don't like Corgis, tryna to impoverish someone here",
        'timezone': -5,
        'timezone_name': 'America/New_York',
        'paid': 'false'
    }
    url = 'https://4uryubhk96.execute-api.us-east-1.amazonaws.com/prod/adduser/corgis'
    resp = requests.post(url, data= corgi_data).json()
    print(resp, '\n')

if __name__ == "__main__":
    while True: 
        phone_number = read_phone_number()
        if phone_number is None:
            continue
        carrier_info = validate_number(phone_number)
        sign_number_up(phone_number, carrier_info[0], carrier_info[1])
        sleep(1)
        