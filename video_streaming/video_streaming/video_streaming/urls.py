from django.contrib import admin
from django.urls import path, include

from apps.users.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('users/',include('apps.users.api.routers')),
]
