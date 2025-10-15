from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


class LoginView(TokenObtainPairView):
    """Login view returns access and refresh tokens."""
    pass


class RefreshView(TokenRefreshView):
    """Refresh access token using refresh token."""
    pass


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'detail': 'Refresh token required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            # Token may already be blacklisted or malformed; treat as idempotent success
            return Response(status=status.HTTP_204_NO_CONTENT)
