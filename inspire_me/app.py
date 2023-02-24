import json

import logging
import requests


def lambda_handler(event, context):
    inspirebot_url = "http://inspirobot.me/api?generate=true"

    # Call inspirobot to get the image url
    response = requests.get(inspirebot_url)
    result_content = response.content.decode('utf-8')

    logging.info(result_content)

    return {
        "statusCode": 200,
        "body": json.dumps({
            'response_type': 'in_channel',
            'attachments': [{
                'image_url': result_content
            }]
        })
    }
