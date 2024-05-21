#!/usr/bin/env python

from datetime import datetime
from api.api import get_appointments, get_bearer_token

import yaml
import email_client

DATE_FORMAT = "%Y-%m-%d"

with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)


def new_date_found(appointment):
    # check for new availability
    appointment_date = appointment["appointmentDt"]["date"]
    new_date = datetime.strptime(appointment_date, DATE_FORMAT)
    before_date = datetime.strptime(config['icbc']['expactAfterDate'], DATE_FORMAT)

    return new_date <= before_date


def create_email_body(matching_appointments):
    body = "<h1>Available appointments</h1>"
    for index, appointment in enumerate(matching_appointments):
        body += f"<h3>Appointment #:{index}</h3>"
        body += f"<strong> Date: </strong> {appointment['appointmentDt']['date']} <br>"
        body += f"<strong>Day of week: </strong> {appointment['appointmentDt']['dayOfWeek']} <br>"
        body += f"<strong>Start time: </strong> {appointment['startTm']} <br>"
        body += f"<strong>End time: </strong> {appointment['endTm']} <br>"
        body += f"-------------------------------------------------------- <br>"
    return body


def run():
    token = get_bearer_token()

    checking_time = datetime.now()
    locations = config['location']
    new_appointments = []

    print('Checking appointments at ', checking_time)

    for location in locations:
        appointments = get_appointments(location, token)

        for appointment in appointments:
            if new_date_found(appointment):
                new_appointments.append(appointment)
                print('New appointment found', appointment)

    print(len(new_appointments), ' appointments found at', checking_time)

    if len(new_appointments) != 0:
        subject = 'ICBC bot notification'
        body = create_email_body(new_appointments)
        sender = ''
        receipients = []
        password = ''

        email_client.send_email(subject, body, sender, receipients, password)

def handler(event, context):
    run()

if __name__ == "__main__":
    run()
