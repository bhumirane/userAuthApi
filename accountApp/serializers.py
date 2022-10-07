from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from accountApp.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email','name','password','password2','tc']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
#validating password and confirm password while registration
def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't Match")
    return attrs

def create(self,validate_data):
    return User.objects.create_user(**validate_data)