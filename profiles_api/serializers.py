from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serialize a name field for testing our api view"""
    name =  serializers.CharField(max_length=20)
    