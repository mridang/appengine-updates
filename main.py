#!/usr/bin/env python
import webapp2

#trailing slahs

app = webapp2.WSGIApplication([
    webapp2.Route(r'/<uniqid:([a-zA-Z0-9]{32})>/<android:([0-9]{2})>/<device:([a-zA-Z0-9]{4,12})>/',      handler='handlers.Updates'),
], debug=True)
