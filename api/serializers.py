from .models import Skill
from rest_framework import serializers

# Serializer to create JSON data from the Skill model provided to a client
class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id','skill', 'description']
