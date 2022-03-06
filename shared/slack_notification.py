import requests
import os

slack_alert_webhook = os.environ['SLACK_ALERTS_WEBHOOK']


def send_msg(msg):
    payload = '{"text":"%s"}' % msg
    response = requests.post(slack_alert_webhook,
                             payload)