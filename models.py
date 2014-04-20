from google.appengine.ext import db

class Application(db.Model):
    """
    Model for storing the the applications and the device details - model, country, build and budid
    Each application that is stored needs to have the name of the package, the version number of the
    package, the version code of the package, the signature of the package cerfificate, and the SHA1
    checksum of the APK.
    """
    uniqid = db.StringProperty(required = True)
    android = db.IntegerProperty(required = True)
    device = db.StringProperty(required = True)
    country = db.StringProperty(required = True)
    package = db.StringProperty(required = True)
    vercode = db.IntegerProperty(required = True)
    vername = db.StringProperty(required = True)
    signature = db.StringProperty(required = True)
    checksum = db.StringProperty(required = True)