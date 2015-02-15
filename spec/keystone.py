from mock import patch
from specter import Spec, expect

from requests_cloudauth.keystone import KeystoneV2PasswordAuth
from requests_cloudauth.keystone import KeystoneV2AuthBase
from requests_cloudauth import FailedAuthenticationError
from requests_cloudauth import UnexpectedResponseCodeError
from spec import get_auth_resp


class AuthenticationToKeystone(Spec):
    class V2AuthBase(Spec):
        def before_all(self):
            self.auth = KeystoneV2AuthBase(None, None)

        def get_token_should_raise_not_implemented(self):
            expect(self.auth.get_token).to.raise_a(NotImplementedError)

    class V2PasswordAuth(Spec):

        def before_all(self):
            self.auth = KeystoneV2PasswordAuth(
                endpoint='http://',
                username='tester',
                password='password',
                tenant_name='test'
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

        @patch("requests.post")
        def raises_a_failed_auth_error_on_401(self, post_func):
            post_func.return_value = get_auth_resp(401, {'msg': 'something'})
            expect(self.auth.get_token).to.raise_a(FailedAuthenticationError)

        @patch("requests.post")
        def raises_a_unexpected_response_error_on_500(self, post_func):
            post_func.return_value = get_auth_resp(500, {'msg': 'something'})
            expect(self.auth.get_token).to.raise_a(UnexpectedResponseCodeError)
