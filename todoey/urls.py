from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('trello.urls'), name="trello"),
    path('', include('user_auth_pages.urls')),
    path('admin/', admin.site.urls),
]
