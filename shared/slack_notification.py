import json

import requests
import os

os.environ['SLACK_ALERTS_WEBHOOK'] = "https://hooks.slack.com/services/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"
os.environ[
    'SLACK_REGISTER_WEBHOOK'] = "https://hooks.slack.com/services/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"

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
