from rest_framework import throttling
from .models import Api


class AssignedRateThrottle(throttling.UserRateThrottle):

    def set_throttle_rate(self, request, view):
        pathname = request.path_info.split('/')[2]
        apimodel = Api.objects.filter(api_name=pathname)
        user_throttle_rate = apimodel[0].userthrottlevalue + '/' + apimodel[0].userthrottleunit
        anon_throttle_rate = apimodel[0].anonthrottlevalue + '/' + apimodel[0].anonthrottleunit
        AssignedRateThrottle.THROTTLE_RATES['user'] = user_throttle_rate
        AssignedRateThrottle.THROTTLE_RATES['anon'] = anon_throttle_rate
        return True
