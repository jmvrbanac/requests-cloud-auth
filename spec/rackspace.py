from mock import patch
from specter import Spec, expect

from requests_cloud_auth import rackspace
from spec import get_auth_resp


class AuthenticationToRackspace(Spec):
    class PasswordAuthentication(Spec):
        def before_all(self):
            self.auth = rackspace.RackspacePasswordAuth(
                username='tester',
                password='password'
            )

        @patch("requests.post")
        def can_authenticate(self, post_func):
            post_func.return_value = get_auth_resp()

            creds = self.auth.authenticate()

            expect(creds.get('token', None)).to.equal('some_token')
            expect(creds.get('project_id', None)).to.equal('some_tenant')

        @patch("requests.post")
        def can_get_token(self, post_func):
            post_func.return_value = get_auth_resp()

            token, tenant = self.auth.get_token()
            expect(token).to.equal('some_token')

    class ApiKeyAuthentication(Spec):
        def before_all(self):
            self.auth = rackspace.RackspaceApiKeyAuth(
                username='tester',
                api_key='api_key'
            )

        @patch("requests.post")
        def can_authenticate(self, post_func):
            post_func.return_value = get_auth_resp()

            creds = self.auth.authenticate()

            expect(creds.get('token', None)).to.equal('some_token')
            expect(creds.get('project_id', None)).to.equal('some_tenant')

        @patch("requests.post")
        def can_get_token(self, post_func):
            post_func.return_value = get_auth_resp()

            token, tenant = self.auth.get_token()
            expect(token).to.equal('some_token')
