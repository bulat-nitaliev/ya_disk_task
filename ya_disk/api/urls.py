
from api.views import UserViewSet, YaDiskApiViw
from django.urls import path

urlpatterns = [
    path('users/', UserViewSet.as_view({'get':"list", "post": "create"})),
    path('yadisk/', YaDiskApiViw.as_view()),
]