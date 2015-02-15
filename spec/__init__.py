from json import dumps as dict_to_str

from pretend import stub


def get_auth_resp(code=200, json=None):
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
        content=dict_to_str(auth_dict)
    )
