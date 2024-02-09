from django.contrib import admin
from .models import Skill
# Registration of the Skill and skills list views on the admin site
class SkillsList(admin.ModelAdmin):
    list_display = ('id', 'skill', 'description')
    list_filter = ('skill', 'description')
    search_fields = ('skill', 'description')


admin.site.register(Skill, SkillsList)
