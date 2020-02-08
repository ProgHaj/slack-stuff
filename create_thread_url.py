# input: url to archived message
# outputs: thread-url to append to any slack url of the slack with the archived message

# example of a slack url with a thread open:
#    https://app.slack.com/client/SLACK_ID/CHANNEL_ID/thread/CHANNEL_ID-MESSAGE_ID_FIRST_10.MESSAGE_ID_REST
# example of archived slack url:
#    https://SLACK_NAME.slack.com/archives/CHANNEL_ID/pMESSAGE_ID

# usage: python create_thread_url.py URL_TO_ARCHIVED_MESSAGE

import sys

def extract(url, slack_id=None):
    channel, message = url.split("/")[-2:]
    return "/thread/{}-{}.{}".format(channel, message[1:11], message[11:])


if __name__ == "__main__":
    url = extract(sys.argv[1])
    print(url)
