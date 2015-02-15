from requests_cloud_auth.keystone import KeystoneV2AuthBase

US_ENDPOINT = 'https://identity.api.rackspacecloud.com'
UK_ENDPOINT = 'https://lon.identity.api.rackspacecloud.com'


class RackspacePasswordAuth(KeystoneV2AuthBase):

    def __init__(self, username, password, endpoint=None,
                 region='US'):
        """Authentication extension for Requests that supports Rackspace
           password authentication.

        :param username: Valid Rackspace Cloud username
        :param password: Valid Rackspace Cloud password
        :param endpoint: (optional) URI to override authentication endpoint
        :param region: (optional) Specify the Rackspace Cloud region.
            Supported values: US, UK

        :return: Instance of RackspacePasswordAuth
        """
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
        """Authentication extension for Requests that supports Rackspace
           API key authentication.

        :param username: Valid Rackspace Cloud username
        :param api_key: Valid Rackspace Cloud API key
        :param endpoint: (optional) URI to override authentication endpoint
        :param region: (optional) Specify the Rackspace Cloud region.
            Supported values: US, UK

        :return: Instance of RackspaceApiKeyAuth
        """
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
