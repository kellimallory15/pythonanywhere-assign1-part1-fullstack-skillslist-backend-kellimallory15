from django.db import models

# Data model defining a skill
class Skill(models.Model):
    skill = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
