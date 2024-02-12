from django.urls import path, include


urlpatterns = [
    path('role', include('role.urls'))
]
