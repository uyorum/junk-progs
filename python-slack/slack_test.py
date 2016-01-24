import os
from slacker import Slacker

token = os.environ.get("SLACK_TOKEN")
incoming_webhook_url = os.environ.get("SLACK_INCOMING_URL")

slack = Slacker(token, incoming_webhook_url)
print(slack.api.test().body)
print(slack.channels.list().body)
print(slack.users.list().body)
print(slack.chat.post_message('#general', 'test message').body)
data = {
        "username": "ghost-bot",
        "icon_emoji": ":ghost:",
        "text": "BOO!"
}

# Incoming Webhook
print(slack.incomingwebhook.post(data).text)
