import logging
import os
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

token = os.environ.get("SLACK_BOT_TOKEN", "")
logger.info(f"Using token starting with: {token[:10]}...")

client = WebClient(token=token)

def fetch_user_emails(users):
    emails = []
    for user_id in users:
        try:
            result = client.users_info(user=user_id)
            email = result["user"]["profile"]["email"]
            emails.append(email)
            logger.info(f"Fetched email for user {user_id}: {email}")
        except SlackApiError as e:
            logger.error(f"Error fetching information for user {user_id}: {e}")
            logger.error(f"Response data: {e.response}")

    return ",".join(emails)

users_json = '''
{
    "users": [ "U0000000000", "U1111111111", "U2222222222" ]
}
'''

if __name__ == "__main__":
    users_data = json.loads(users_json)

    email_list = fetch_user_emails(users_data["users"])
    print(f"Comma-separated email list: {email_list}")

    with open("user_emails.txt", "w") as f:
        f.write(email_list)
    print("Email list has been saved to user_emails.txt")