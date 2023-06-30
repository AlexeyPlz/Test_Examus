from django.conf import settings
from rest_framework.permissions import BasePermission


class TokenAccessPermission(BasePermission):

    def has_permission(self, request, view):
        return True if request.headers.get('API-Token-Access') in (settings.API_TOKEN,) else False
