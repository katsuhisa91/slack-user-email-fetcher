# slack-user-email-fetcher

This Python script fetches email addresses for a list of Slack user IDs using the Slack API. It includes error handling and a retry mechanism for improved reliability.

## Installation & Usage

1. Set up your Slack Bot Token as an environment variable.

```sh
export SLACK_BOT_TOKEN="xoxb-your-actual-token"  # Unix
set SLACK_BOT_TOKEN=xoxb-your-actual-token       # Windows
```

2. Modify the users_json variable in the script to include the Slack user IDs you want to fetch emails for.

```
users_json = '''
{
    "users": [ "U0000000000", "U1111111111", "U2222222222" ]
}
'''
```

3. Install the required Python package & run the script.

```sh
pip install slack_sdk
python slack-user-email-fetcher.py
```
