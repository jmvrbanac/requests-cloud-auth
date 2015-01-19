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

    return stub(status_code=200, json=lambda: auth_dict)
