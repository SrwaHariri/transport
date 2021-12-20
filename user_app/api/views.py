from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import LogoutSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class LogoutApiView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)