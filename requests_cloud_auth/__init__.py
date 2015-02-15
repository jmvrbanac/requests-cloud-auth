from requests.auth import AuthBase

STORED_AUTHENTICATION = None


class StoredAuthentication(object):
    def __init__(self):
        # If we've already created an instance, use that.
        if STORED_AUTHENTICATION:
            return STORED_AUTHENTICATION

        self._stored_data = {}

    def get_credentials(self, category, name):
        stored_cat = self._stored_data.get(category)

        if stored_cat:
            stored_creds = stored_cat.get(name)
            return stored_creds

    def set_credentials(self, category, name, data):
        stored_cat = self._stored_data.get(category, {})
        stored_name = stored_cat.get(name)

        if not stored_name:
            stored_cat[name] = data
            self._stored_data[category] = stored_cat

        return stored_cat.get(name)


class RequestsCloudAuthBase(AuthBase):
    @property
    def stored_auth(self):
        global STORED_AUTHENTICATION
        if not STORED_AUTHENTICATION:
            STORED_AUTHENTICATION = StoredAuthentication()
        return STORED_AUTHENTICATION


class UnexpectedResponseCodeError(Exception):
    def __init__(self, resp):
        msg = 'Response Code: {code}, Body: {body}'.format(
            code=resp.status_code,
            body=resp.content
        )
        super(UnexpectedResponseCodeError, self).__init__(msg)


class FailedAuthenticationError(Exception):
    def __init__(self, resp):
        msg = 'Could not authenticate: {0}'.format(resp.content)
        super(FailedAuthenticationError, self).__init__(msg)
