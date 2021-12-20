from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()
    default_error_messages = {
        'invalid_token': 'token is expired'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return self

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('invalid_token')
