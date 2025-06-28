from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('', include('core.urls')),  
]
