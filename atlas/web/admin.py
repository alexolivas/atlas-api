from django.contrib import admin
from atlas.web.models import AboutInfo
from atlas.web.models import CareerSnapshot
# from models import CareerSnapshotAchievement
# from models import Technology
from atlas.web.models import TechnicalSkill
from atlas.web.models import Expertise


class CareerSnapshotAdmin(admin.ModelAdmin):
    list_display = ('company', 'snapshot_type', 'position', 'location',)


# class CareerSnapshotAchievementAdmin(admin.ModelAdmin):
#     list_display = ('title', 'milestone', 'month', 'year',)
# admin.site.register(CareerSnapshotAchievement, CareerSnapshotAchievementAdmin)


class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('location',)


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


class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('area',)


admin.site.register(CareerSnapshot, CareerSnapshotAdmin)
admin.site.register(AboutInfo, AboutInfoAdmin)
admin.site.register(TechnicalSkill, TechnicalSkillAdmin)
admin.site.register(Expertise, ExpertiseAdmin)
