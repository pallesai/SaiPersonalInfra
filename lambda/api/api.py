import requests
import json
import yaml

with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

def get_bearer_token():

    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver',
        "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache, no-store",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    }

    payload = {
        "drvrLastName": config['icbc']['drvrLastName'],
        "licenceNumber": config['icbc']['licenceNumber'],
        "keyword": config['icbc']['keyword']
    }

    response = requests.put(config['end_points']['login_end_point'], data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.headers["Authorization"]
    return ""

def get_appointments(location, bearer_token):

    headers = {
        'Content-type': 'application/json',
        'Authorization': bearer_token,
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://onlinebusiness.icbc.com/webdeas-ui/booking',
        "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache, no-store",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    }

    payload = {
        "aPosID": location['aPosID'],
        "examType": location['examType'],
        "examDate": location['examDate'],
        "ignoreReserveTime": location['ignoreReserveTime'],
        "prfDaysOfWeek": "[0,1,2,3,4,5,6]",
        "prfPartsOfDay": "[0,1]",
        "lastName": config['icbc']['drvrLastName'],
        "licenseNumber": config['icbc']['licenceNumber']
    }

    response = requests.post(config['end_points']['appointments_end_point'], data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print('Authorization Error')
        return []