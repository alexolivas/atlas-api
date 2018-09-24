from django.contrib import admin
from models import AboutInfo
from models import CareerSnapshot
# from models import CareerSnapshotAchievement
# from models import Technology
from models import TechnicalSkill
from models import Expertise


class CareerSnapshotAdmin(admin.ModelAdmin):
    list_display = ('company', 'snapshot_type', 'position', 'location',)
admin.site.register(CareerSnapshot, CareerSnapshotAdmin)


# class CareerSnapshotAchievementAdmin(admin.ModelAdmin):
#     list_display = ('title', 'milestone', 'month', 'year',)
# admin.site.register(CareerSnapshotAchievement, CareerSnapshotAchievementAdmin)


class AboutInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(AboutInfo, AboutInfoAdmin)


# class TechnologyStackAdmin(admin.ModelAdmin):
#     list_display = ('name',)
# admin.site.register(TechnologyStack, TechnologyStackAdmin)
#
#
# class TechnologyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'technology_stack', 'technology_type',)
# admin.site.register(Technology, TechnologyAdmin)

# TODO: Do not save the django_admin_log or if so, set the ID to the latest

class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type',)
admin.site.register(TechnicalSkill, TechnicalSkillAdmin)


class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('area',)
admin.site.register(Expertise, ExpertiseAdmin)
