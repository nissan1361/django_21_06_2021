from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlparse, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile

#def save_user_profile(backend, user, response, *args, **kwargs):
#    if backend.name != 'vk-oauth2':
#        return
#    api_url = urlunparse(('https//'))
