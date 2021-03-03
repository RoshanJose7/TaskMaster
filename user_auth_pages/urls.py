from user_auth_pages.views import dashboard, register, user_login, user_logout
from django.urls import path

urlpatterns = [
	path('register/', register, name="register"),
	path('login/', user_login, name="login"),
	path('logout/', user_logout, name="logout"),
	path('dashboard/', dashboard, name="dashboard")
]
