from rest_framework import serializers
from .models import *

class Student(serializers.ModelSerializer):
    class Meta:
        model=Pure
        fields='__all__'