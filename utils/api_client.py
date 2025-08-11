# api_client.py
# This module provides reusable functions for interacting with the Lab Scheduler API.
# It abstracts HTTP requests for create, read, update, and delete operations,
# making the test code cleaner and easier to maintain.

import requests

BASE_URL = "https://fh-qa-labscheduler-apeksha823.replit.app/api"

def create_lab(payload):
    return requests.post(f"{BASE_URL}/labs", json=payload)

def get_lab(lab_id):
    return requests.get(f"{BASE_URL}/labs/{lab_id}")

def update_lab(lab_id, payload):
    return requests.put(f"{BASE_URL}/labs/{lab_id}", json=payload)

def delete_lab(lab_id):
    return requests.delete(f"{BASE_URL}/labs/{lab_id}")
