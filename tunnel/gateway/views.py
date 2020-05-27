import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header, BasicAuthentication
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Api
from .throttling import AssignedRateThrottle
from rest_framework.throttling import UserRateThrottle
from .permissions import CheckAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
import base64
from requests.auth import HTTPBasicAuth


class gateway(APIView):
    permission_classes = (CheckAuthentication, )
    throttle_classes = (AssignedRateThrottle, )

    def check_throttles(self, request):
        """
        Check if request should be throttled.
        Raises an appropriate exception if the request is throttled.
        """
        throttle_durations = []
        for throttle in self.get_throttles():
            throttle.set_throttle_rate(request, self)
            if not throttle.allow_request(request, self):
                throttle_durations.append(throttle.wait())

        if throttle_durations:
            # Filter out `None` values which may happen in case of config / rate
            # changes, see #1438
            durations = [
                duration for duration in throttle_durations
                if duration is not None
            ]

            duration = max(durations, default=None)
            self.throttled(request, duration)

    def send_request(self, request, upstream_url, authentication):
        headers = {}
        username = ''
        password = ''
        if authentication == 2 and request.META.get('HTTP_AUTHORIZATION'):
            auth_header = request.META['HTTP_AUTHORIZATION']
            encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
            decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
            username = decoded_credentials[0]
            password = decoded_credentials[1]

        # headers['content-type'] = request.content_type

        url = upstream_url
        method = request.method.lower()
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }

        for k, v in request.FILES.items():
            request.data.pop(k)

        if request.content_type and request.content_type.lower() == 'application/json':
            data = json.dumps(request.data)
            headers['content-type'] = request.content_type
        else:
            data = request.data

        return method_map[method](url, auth=HTTPBasicAuth(username, password), headers=headers, data=data, files=request.FILES)

    def operation(self, request):
        pathname = request.path_info.split('/')[2]

        apimodel = Api.objects.filter(api_name=pathname)
        if apimodel.count() != 1:
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)

        authentication = apimodel[0].authentication
        api_name = apimodel[0].api_name
        # get the endpoint from the request
        exclude = 9 + len(api_name)
        uri = request.path_info[exclude:]
        upstream_url = apimodel[0].target_base_uri + uri
        print(upstream_url)

        res = self.send_request(request, upstream_url, authentication)
        if res.headers.get('Content-Type', '').lower() == 'application/json':
            data = res.json()
        else:
            data = res.content
            if not data:
                raise PermissionDenied(
                    "Access is not authorized")

            data = res.json()

            # str_data = data.decode('utf-8')
            # data = json.loads(str_data)

        return Response(data=data, status=res.status_code)

    def get(self, request):
        return self.operation(request)

    def post(self, request):
        return self.operation(request)

    def put(self, request):
        return self.operation(request)

    def patch(self, request):
        return self.operation(request)

    def delete(self, request):
        return self.operation(request)
