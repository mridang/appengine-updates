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
                fields = {}
                fields['android'] = int(android)
                fields['device'] = device
                fields['country'] = self.request.headers['X-AppEngine-Country']
                fields['package'] = update['pname']
                fields['vercode'] = int(update['vcode'])
                fields['signature'] = update['cert_sig']
                fields['checksum'] = update['apk_sha1']

                rowid = uniqid + update['cert_sig'] + update['apk_sha1']
                models.Application.get_or_insert(rowid, **fields)

        except Exception, e:
            logging.exception('Error saving update %s', update)
            print e
            self.abort(500)