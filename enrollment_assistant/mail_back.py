"""
Email backend that writes messages to console instead of sending them.
"""
import json
import requests
from django.core.mail.backends.base import BaseEmailBackend


class EmailBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_messages(self, email_messages):
        """Write all messages to the stream in a thread-safe way."""
        if not email_messages:
            return
        try:
            for message in email_messages:
                # print(f'message: {message}')
                mail_box = message.message()
                # for k,v in mail_box.items():
                #     print(k,'>',v)
                print(f"dir: {dir(mail_box)}")
                # print(mail_box._payload)
                print(mail_box.__getattribute__('_payload'))
                print(f'============================')
                print(mail_box)
                print('+++++++++++++++++++++++++++++')
                print(f"type: {type(mail_box)}, mail_box: {mail_box}")
                url = "http://127.0.0.1:5000//mailing"
                data = {'mail': mail_box["to"], 'subject': 'Changing password',
                        'text': mail_box['Message-ID']}
                data_json = json.dumps(data)
                response = requests.post(url, data=data_json)
                print(response)
        except Exception:
            print("503: Service Unavailable")
        return
