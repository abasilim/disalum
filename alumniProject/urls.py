
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumniapp.urls')),
    path('alumniapp/user/', include('users.urls', namespace='users')),
    path('alumniapp/', include('alumni_api.urls',)),
    # Adds Rest framework Authenticaion or login interface
    path('alumniapp-auth/', include('rest_framework.urls')),
    path('alumniapp/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('alumniapp/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
