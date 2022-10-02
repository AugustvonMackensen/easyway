import base64
import hashlib
import hmac
import time
import requests
import json





def make_signature(string):
    secret_key = bytes('5rmLIdLmEawi2diWCXDAGgnVSOLIGzE7h9MoFj5y', 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64


def make_signature2(timestamp):
    access_key = '22lhKDJsMNwqsoCPyT0P'
    secret_key = bytes('5rmLIdLmEawi2diWCXDAGgnVSOLIGzE7h9MoFj5y', 'UTF-8')

    secret_key = bytes(secret_key, 'UTF-8')

    uri = "/sms/v2/services/ncp:sms:kr:263092132141:sms/messages"
    # uri 중간에 Console - Project - 해당 Project 서비스 ID 입력 (예시 = ncp:sms:kr:263092132141:sms)

    message = "POST" + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey

import json, random, requests, time

from django.views import View
from .utils import make_signature
from django.http import JsonResponse
#from .models import SmsAuth
def send_sms(User):
    url = "https://sens.apigw.ntruss.com"
    uri = "/sms/v2/services/" + 'ncp:sms:kr:289640846112:sms_auth' + "/messages"
    api_url = url + uri
    timestamp = str(int(time.time() * 1000))
    access_key = '22lhKDJsMNwqsoCPyT0P'
    string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + access_key
    signature = make_signature(string_to_sign)

    headers = {
        'Content-Type': "application/json; charset=UTF-8",
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': signature
    }

    body = {
        "type": "SMS",
        "contentType": "COMM",
        "from": "01030496533",
        "content": f"EasyWay 아이디는 [{User.username}]입니다.",
        "messages": [{"to": User.phone}]
    }

    body = json.dumps(body)

    response = requests.post(api_url, headers=headers, data=body)
    response.raise_for_status()