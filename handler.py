import os

import requests

BASE_URL = os.environ.get("BASE_URL")


def warn_up(event, context):
    health_url = f"{BASE_URL}/health"

    resp = requests.get(health_url).json()

    return {
        "BaseURL": health_url,
        "HealthResponse": resp
    }
