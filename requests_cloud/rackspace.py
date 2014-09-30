from requests_cloud.keystone import KeystoneV2AuthBase

US_ENDPOINT = 'https://identity.api.rackspacecloud.com'
UK_ENDPOINT = 'https://lon.identity.api.rackspacecloud.com'


class RackspacePasswordAuth(KeystoneV2AuthBase):

    def __init__(self, username, password, endpoint=None,
                 region='US'):
        if not endpoint:
            endpoint = UK_ENDPOINT if region.lower() == 'uk' else US_ENDPOINT

        super(RackspacePasswordAuth, self).__init__(
            endpoint=endpoint,
            username=username,
            password=password
        )

    def get_token(self):
        body = {
            'auth': {
                'passwordCredentials': {
                    'username': self.username,
                    'password': self.password
                }
            }
        }
        return self.get_token_from_request_body(body)


class RackspaceApiKeyAuth(KeystoneV2AuthBase):

    def __init__(self, username, api_key, endpoint=None,
                 region='US'):
        if not endpoint:
            endpoint = UK_ENDPOINT if region.lower() == 'uk' else US_ENDPOINT

        super(RackspaceApiKeyAuth, self).__init__(
            endpoint=endpoint,
            username=username,
            api_key=api_key
        )

    def get_token(self):
        body = {
            'auth': {
                'RAX-KSKEY:apiKeyCredentials': {
                    'username': self.username,
                    'apiKey': self.api_key
                }
            }
        }
        return self.get_token_from_request_body(body)
