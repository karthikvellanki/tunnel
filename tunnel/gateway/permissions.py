from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import Api
from tunnelapp.models import User


class CheckAuthentication(permissions.BasePermission):

    def has_permission(self, request, view):
        pathname = request.path_info.split('/')[2]
        apimodel = Api.objects.filter(api_name=pathname)
        authentication = apimodel[0].authentication
        if authentication == 0:
            return True
        if authentication == 1:
            if request.user.is_authenticated:
                return True
            else:
                raise PermissionDenied(
                    "No API key provided for this request")
        if authentication == 2:
            # Checking if credentials exists. Credentials are authenticated by the target endpoint.
            auth_header = request.META['HTTP_AUTHORIZATION']
            if auth_header[:5] == 'Basic':
                return True
            else:
                raise PermissionDenied(
                    "No credentials provided for this request.")

        raise NotImplementedError('Authentication hasn\'t been set')
