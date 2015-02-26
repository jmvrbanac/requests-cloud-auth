from json import dumps as dict_to_str

from pretend import stub


def get_keystone_v2_auth_resp(code=200, json=None, headers={}):
    auth_dict = json
    if not json:
        auth_dict = {
            'access': {
                'token': {
                    'id': 'some_token',
                    'tenant': {
                        'id': 'some_tenant'
                    }
                }
            }
        }

    return stub(
        status_code=code,
        json=lambda: auth_dict,
        content=dict_to_str(auth_dict),
        headers=headers
    )


def get_keystone_v3_auth_resp(code=201, json=None, headers=None):
    auth_dict = json
    if not json:
        auth_dict = {
            'token': {
                'methods': [
                    'password'
                ],
                'roles': [],
                'expires_at': '2015-02-25T18:42:16.989456Z',
                'project': {
                    'id': 'some_project',
                    'name': 'admin'
                },
                'catalog': [],
                'extras': {},
                'user': {},
                'issued_at': '2015-02-25T17:42:16.989488Z'
            }
        }

    if not headers:
        headers = {
            'X-Subject-Token': 'some_token'
        }

    return stub(
        status_code=code,
        json=lambda: auth_dict,
        content=dict_to_str(auth_dict),
        headers=headers
    )
