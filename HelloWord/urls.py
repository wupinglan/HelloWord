from django.contrib import admin
from django.urls import path
from web.views import Login
from web.views import uploads
from web.views import Login_install
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login),
    path('uploads/', uploads),
    path('login_install/', Login_install),
]
