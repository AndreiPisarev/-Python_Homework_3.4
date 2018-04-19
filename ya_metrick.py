from pprint import pprint
from urllib.parse import urlencode
import requests


AUTH_URL = 'https://oauth.yandex.ru/authorize'

APP_ID = 'd2148f05297942ea8e2827526d441e37'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))

token = 'AQAAAAAlyLWCAAT0tfqjOnO75k2vopdUfE4T6vA'
# params = {
#     'oauth_token': token
# }
#
# response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', params)

class YaMetrika:

    def __init__(self, token):
        self.token = token

    def get_metrics(self):
        params = {
            'oauth_token': self.token,
            'id': 48525710,
            'metrics': ['ym:s:visits', 'ym:s:pageviews', 'ym:s:users']
        }

        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params=params)
        visits, pageviews, users = [m for m in response.json()['data'][0]['metrics']]
        return visits, pageviews, users


user1 = YaMetrika(token)
print(user1.get_metrics())

