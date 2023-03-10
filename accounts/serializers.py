from rest_framework import serializers

from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'famly',
            'otchestvo',
            'image',
            'password',
            'password2',

        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            famly=self.validated_data['famly'],
            otchestvo=self.validated_data['otchestvo'],
            image=self.validated_data['image'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match!'})
        account.set_password(password)
        account.save()
        return account


class AccountOssobennoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk', 'email', 'username', 'famly', 'otchestvo', 'image']




