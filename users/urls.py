from django.contrib import admin
from django.urls import path, include

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def logout(request):
    request.user.auth_token.delete() # Token Sil.
    return Response({"message": 'User Logout: Token Deleted'})


urlpatterns = [
    path('auth', include('dj_rest_auth.urls')),
    path('logout', logout),
]
