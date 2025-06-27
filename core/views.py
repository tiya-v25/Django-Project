from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from core.tasks import print_username  

# PUBLIC API 
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    print_username.delay("tiya")  
    return Response({'message': 'Background task triggered!'})

# PROTECTED API 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': f'Hello {request.user.username}, this is a protected API!'})
