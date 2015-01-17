import json
import requests

from requests_cloudauth import RequestsCloudAuthBase, UnexpectedResponseCode


class KeystoneV2AuthBase(RequestsCloudAuthBase):

    def __init__(self, endpoint, username, tenant_name=None, password=None,
                 api_key=None):
        """Base Authentication class for KeystoneV2 support"""
        self.endpoint = '{base}/v2.0/tokens'.format(base=endpoint)
        self.username = username
        self.tenant_name = tenant_name
        self.password = password
        self.api_key = api_key
        self.project_id = None
        self.token = None

    def parse(self, response_dict):
        access_dict = response_dict.get('access', {})
        token_dict = access_dict.get('token', {})
        tenant_dict = token_dict.get('tenant', {})

        return token_dict.get('id'), tenant_dict.get('id')

    def get_token_from_request_body(self, request_body_dict):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        auth_json_str = json.dumps(request_body_dict)
        resp = requests.post(self.endpoint,
                             data=auth_json_str,
                             headers=headers)

        if resp.status_code != 200:
            msg = 'Response Code: {code}, Body: {body}'.format(
                code=resp.status_code,
                body=resp.content
            )
            raise UnexpectedResponseCode(msg)

        token, tenant_id = self.parse(resp.json())
        self.token = token
        self.project_id = tenant_id

        return token, tenant_id

    def get_token(self):
        raise NotImplemented()

    def authenticate(self):
        creds = self.stored_auth.get_credentials(self.tenant_name,
                                                 self.username)
        if not creds:
            self.get_token()
            data = {'token': self.token, 'project_id': self.project_id}
            creds = self.stored_auth.set_credentials(
                self.tenant_name, self.username, data)

        return creds

    def __call__(self, r):
        creds = self.authenticate()

        # modify and return the request
        r.headers['X-Project-Id'] = creds.get('project_id')
        r.headers['X-Auth-Token'] = creds.get('token')
        return r


class KeystoneV2PasswordAuth(KeystoneV2AuthBase):

    def __init__(self, endpoint, username, password, tenant_name):
        super(KeystoneV2PasswordAuth, self).__init__(
            endpoint=endpoint,
            username=username,
            tenant_name=tenant_name,
            password=password
        )

    def get_token(self):
        body = {
            'auth': {
                'passwordCredentials': {
                    'username': self.username,
                    'password': self.password
                },
                'tenantName': self.tenant_name
            }
        }
        return self.get_token_from_request_body(body)