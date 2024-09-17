
from api.views import UserViewSet, YaDiskApiViw
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('users/', UserViewSet.as_view({'get':"list", "post": "create"})),
    path('yadisk/', cache_page(60*60*5)(YaDiskApiViw.as_view())),
]