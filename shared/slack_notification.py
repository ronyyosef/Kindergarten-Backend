import json

import requests
import os


slack_new_user_alert_webhook = os.environ['SLACK_REGISTER_WEBHOOK']
slack_errors_alert_webhook = os.environ['SLACK_ALERTS_WEBHOOK']


def send_new_user_msg(msg):
    payload = '{"text":"%s"}' % msg
    response = requests.post(slack_new_user_alert_webhook,
                             payload)

def send_errors_alert_msg(msg):
    payload = '{"text":"%s"}' % msg
    payload = json.dumps({

        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": msg
                }
            }
        ]
    })
    response = requests.post(slack_errors_alert_webhook,
                             payload)
    print(response)
