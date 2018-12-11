from django.http import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from backweb.models import MyBlogUser


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path in ['/backweb/login/', '/backweb/register/']:
            return None

        user_id = request.session.get('user_id')
        if user_id:
            user = MyBlogUser.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect('/backweb/login/')


    def process_response(self, request, response):
        return response