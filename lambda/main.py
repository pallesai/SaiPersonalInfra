#!/usr/bin/env python

def handler(event, context):
    if event.request == "test":
        print(event, context)

