import webapp2
import json
import logging

from google.appengine.api import memcache

import models

class Updates(webapp2.RequestHandler):
    """
    Handler for saving anf fetching the list of updates. Whn updates are requested, the GET method
    is invoked and updates are added, the POST method is invoked
    """
    def post(self, uniqid, android, device):
        """
        Saves the list of installed applications to the datastore. It iterates over each of the
        objects in the JSON payload and saves them.
        """
        try:

            for update in json.loads(self.request.body):

                query = models.Application.all()
                query.filter('uniqid =', uniqid)
                query.filter('android =', int(android))
                query.filter('device =', device)
                query.filter('country =', self.request.headers['X-AppEngine-Country'])
                query.filter('package =', update['pname'])
                query.filter('vercode =', int(update['vcode']))
                query.filter('vername =', update['vname'])
                query.filter('signature =', update['cert_sig'])
                query.filter('checksum =', update['apk_sha1'])

                if not query.fetch(1):
                    fields = {}
                    fields['uniqid'] = uniqid
                    fields['android'] = int(android)
                    fields['device'] = device
                    fields['country'] = self.request.headers['X-AppEngine-Country']
                    fields['package'] = update['pname']
                    fields['vercode'] = int(update['vcode'])
                    fields['vername'] = update['vname']
                    fields['signature'] = update['cert_sig']
                    fields['checksum'] = update['apk_sha1']

                    record = models.Application(**fields)
                    record.put()

        except Exception, e:
            logging.exception('Error saving update %s', update)
            print e
            self.abort(500)