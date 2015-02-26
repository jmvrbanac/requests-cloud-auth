from specter import Spec, expect

import requests_cloud_auth


class AuthStorage(Spec):

    def before_each(self):
        # Clean storage before testing
        requests_cloud_auth.STORED_AUTHENTICATION = None

    def can_handle_credentials_via_the_auth_base(self):
        base = requests_cloud_auth.RequestsCloudAuthBase()
        base.stored_auth.set_credentials(
            category='trace',
            name='boom',
            data={'something': 'in here'}
        )

        creds = base.stored_auth.get_credentials(category='trace', name='boom')

        expect(creds.get('something')).to.equal('in here')

    def can_set_credentials_twice_via_the_auth_base(self):
        base = requests_cloud_auth.RequestsCloudAuthBase()
        base.stored_auth.set_credentials(
            category='trace',
            name='boom',
            data={'something': 'in here'}
        )

        creds = base.stored_auth.get_credentials(category='trace', name='boom')
        expect(creds.get('something')).to.equal('in here')

        # Attempt to overwrite creds. We should only get the old creds back
        base.stored_auth.set_credentials(
            category='trace',
            name='boom',
            data={'something': 'else in here'}
        )

        creds = base.stored_auth.get_credentials(category='trace', name='boom')

        expect(creds.get('something')).to.equal('in here')
