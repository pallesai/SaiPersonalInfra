#!/usr/bin/env python

from api.api import get_appointments, get_bearer_token

def handler(event, context):
    token = get_bearer_token()
    print(token)
    print(get_appointments(token))

