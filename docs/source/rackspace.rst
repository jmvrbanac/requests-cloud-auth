Rackspace Identity Authentication Extension
===========================================

This authentication extension enables simple authentication to Rackspace
Cloud endpoints.

Sample Usage
------------
::

    import requests
    from requests_cloud_auth import rackspace
    
    auth = rackspace.RackspacePasswordAuth(
        username='my_user',
        password='my_pass'
    )

    # Pre-auth as we need our project_id to list our cloud servers
    auth.authenticate()
    
    url = 'https://ord.servers.api.rackspacecloud.com/v2/{0}/servers'.format(auth.project_id)
    resp = requests.get(url, auth=auth)


Extension API Documentation
---------------------------

.. autoclass:: requests_cloud_auth.rackspace.RackspacePasswordAuth
    :inherited-members:

.. autoclass:: requests_cloud_auth.rackspace.RackspaceApiKeyAuth
    :inherited-members:
