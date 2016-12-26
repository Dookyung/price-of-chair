import os

__author__ = 'jslvtr'

# URL = "https://api.mailgun.net/v3/sandboxa6ce3010d71e467fa7bc850fd033c90b.mailgun.org/messages"
# API_KEY = "key-32c9803892c114850ec4124d9f3ef435"
# FROM = "Mailgun Sanbox <postmaster@sandboxa6ce3010d71e467fa7bc850fd033c90b>.mailgun.org"
# ALERT_TIMEOUT = 10
# COLLECTION = "alerts"


URL = os.environ.get("MAILGUN_URL")
API_KEY = os.environ.get("MAILGUN_API_KEY")
FROM = os.environ.get("MAILGUN_FROM")
ALERT_TIMEOUT = 10
COLLECTION = "alerts"