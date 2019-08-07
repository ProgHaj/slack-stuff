# input: url to archived message and the id of the used slack
# outputs: url to thread of archived message which can be viewed

# example of a slack url with a thread open:
#    https://app.slack.com/client/SLACK_ID/CHANNEL_ID/thread/CHANNEL_ID-MESSAGE_ID_FIRST_10.MESSAGE_ID_REST
# example of archived slack url:
#    https://SLACK_NAME.slack.com/archives/CHANNEL_ID/pMESSAGE_ID

# usage: python create_thread_url.py URL_TO_ARCHIVED_MESSAGE SLACK_ID


def extract(url, slack_id):
    channel, message = url.split("/")[-2:]
    transformed = "{}-{}.{}".format(channel, message[1:11], message[11:])
    base = ["https://app.slack.com/client",
            slack_id,
            channel,
            "thread",
            transformed]
    new_url = "/".join(base)
    return new_url

if __name__ == "__main__":
    import sys
    url = extract(sys.argv[1], sys.argv[2])
    print(url)
