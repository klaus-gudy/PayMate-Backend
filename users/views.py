from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):

#         refresh_token = request.data.get('refresh_token')
#         if refresh_token:
#             try:
#                 token = RefreshToken(refresh_token)
#                 token.blacklist()
#                 return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Revoke the access token
#         try:
#             del request.session['access_token']
#         except KeyError:
#             pass
        
#         return Response(status=status.HTTP_204_NO_CONTENT)