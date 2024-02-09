from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import SkillSerializer
from .models import Skill
from rest_framework.permissions import AllowAny

# List all skills view - does not include create option
class skillsList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# create a new skill view
class skillsListCreate(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# retrieve, update, or destroy a skill
class skillRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
