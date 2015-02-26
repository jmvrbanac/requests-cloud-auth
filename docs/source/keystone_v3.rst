Keystone V3 Authentication Extension
====================================

This authentication extension enables simple authentication to Keystone V3
endpoints.

Sample Usage
------------
::

    import requests
    from requests_cloud_auth import keystone

    keystone_auth = keystone.KeystoneV3PasswordAuth(
        endpoint='https://a.keystone.server',
        username='demo',
        password='cool',
        project_name='my_project'
    )

    resp = requests.get('http://openstack_service/', auth=keystone_auth)



Extension API Documentation
---------------------------

.. autoclass:: requests_cloud_auth.keystone.KeystoneV3PasswordAuth
    :inherited-members:
