from django.urls import path, include


urlpatterns = [
    path('', include('braddock_counter_app.urls')),
]
