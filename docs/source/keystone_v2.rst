Keystone V2 Authentication Extension
====================================

This authentication extension enables simple authentication to Keystone V2
endpoints.

Sample Usage
------------
::

    import requests
    from requests_cloudauth import keystone

    keystone_auth = keystone.KeystoneV2PasswordAuth(
        endpoint='https://a.keystone.server',
        username='demo',
        password='cool',
        tenant_name='my_tenant'
    )

    resp = requests.get('http://openstack_service/', auth=keystone_auth)



Extension API Documentation
---------------------------

.. autoclass:: requests_cloudauth.keystone.KeystoneV2PasswordAuth
    :inherited-members:
