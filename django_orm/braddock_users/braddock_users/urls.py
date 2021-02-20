from django.urls import path, include
urlpatterns = [
    path('', include('braddock_users_app.urls')),
]
