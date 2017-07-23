from mock import patch
from specter import Spec, expect
from pretend import stub

import requests_cloud_auth
from requests_cloud_auth.keystone import KeystoneV3PasswordAuth
from requests_cloud_auth.keystone import KeystoneV2PasswordAuth
from requests_cloud_auth.keystone import KeystoneV2AuthBase
from requests_cloud_auth import FailedAuthenticationError
from requests_cloud_auth import UnexpectedResponseCodeError
from spec import get_keystone_v2_auth_resp
from spec import get_keystone_v3_auth_resp


class AuthenticationToKeystone(Spec):
    class V2AuthBase(Spec):
        def before_all(self):
            self.auth = KeystoneV2AuthBase(None, None)

        def get_token_should_raise_not_implemented(self):
            expect(self.auth.get_token).to.raise_a(NotImplementedError)

    class V2PasswordAuth(Spec):

        def before_each(self):
            requests_cloud_auth.STORED_AUTHENTICATION = None

            self.auth = KeystoneV2PasswordAuth(
                endpoint='http://',
                username='tester',
                password='password',
                tenant_name='test'
            )

        @patch("requests.post")
        def can_authenticate(self, post_func):
            r = get_keystone_v2_auth_resp()
            post_func.return_value = r

            self.auth(r)

            expect(r.headers.get('X-Auth-Token')).to.equal('some_token')
            expect(r.headers.get('X-Project-Id')).to.equal('some_tenant')

        @patch("requests.post")
        def can_get_token(self, post_func):
            post_func.return_value = get_keystone_v2_auth_resp()

            token, tenant = self.auth.get_token()
            expect(token).to.equal('some_token')

        @patch("requests.post")
        def raises_a_failed_auth_error_on_401(self, post_func):
            post_func.return_value = get_keystone_v2_auth_resp(
                code=401,
                json={'msg': 'something'}
            )
            expect(self.auth.get_token).to.raise_a(FailedAuthenticationError)

        @patch("requests.post")
        def raises_a_unexpected_response_error_on_500(self, post_func):
            post_func.return_value = get_keystone_v2_auth_resp(
                code=500,
                json={'msg': 'something'}
            )
            expect(self.auth.get_token).to.raise_a(UnexpectedResponseCodeError)

        def uses_a_basic_cache(self):
            r = stub(headers={})
            project = 'some_project'
            username = 'tester'
            token = 'some_token'

            self.auth.project_id = project
            self.auth.username = username

            self.auth.stored_auth.set_credentials(
                category=project,
                name=username,
                data={'token': token, 'project_id': project},
            )

            self.auth(r)

            expect(r.headers.get('X-Project-Id')).to.equal(project)
            expect(r.headers.get('X-Auth-Token')).to.equal(token)

    class V3PasswordAuth(Spec):

        def before_each(self):
            requests_cloud_auth.STORED_AUTHENTICATION = None

            self.auth = KeystoneV3PasswordAuth(
                endpoint='http://',
                username='tester',
                password='password',
                project_name='test'
            )

        @patch("requests.post")
        def can_authenticate(self, post_func):
            r = get_keystone_v3_auth_resp()
            post_func.return_value = r

            self.auth(r)

            expect(r.headers.get('X-Auth-Token')).to.equal('some_token')
            expect(r.headers.get('X-Project-Id')).to.equal('some_project')

        @patch("requests.post")
        def can_get_token(self, post_func):
            post_func.return_value = get_keystone_v3_auth_resp()

            token, tenant = self.auth.get_token()
            expect(token).to.equal('some_token')

        @patch("requests.post")
        def raises_a_failed_auth_error_on_401(self, post_func):
            post_func.return_value = get_keystone_v3_auth_resp(
                code=401,
                json={'msg': 'something'}
            )
            expect(self.auth.get_token).to.raise_a(FailedAuthenticationError)

        @patch("requests.post")
        def raises_a_unexpected_response_error_on_500(self, post_func):
            post_func.return_value = get_keystone_v3_auth_resp(
                code=500,
                json={'msg': 'something'}
            )
            expect(self.auth.get_token).to.raise_a(UnexpectedResponseCodeError)

        def uses_a_basic_cache(self):
            r = stub(headers={})
            project = 'some_project'
            username = 'tester'
            token = 'some_token'

            self.auth.project_id = project
            self.auth.username = username

            self.auth.stored_auth.set_credentials(
                category=project,
                name=username,
                data={'token': token, 'project_id': project},
            )

            self.auth(r)

            expect(r.headers.get('X-Project-Id')).to.equal(project)
            expect(r.headers.get('X-Auth-Token')).to.equal(token)
