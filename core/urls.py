from django.urls import path
from .views import public_view, protected_view
from .views import home
urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('', home, name='home')

    
]
