from django.contrib import admin
from models import AboutInfo
from models import CareerSnapshot
from models import CareerSnapshotAchievement
from models import Technology
from models import TechnologyStack


class CareerSnapshotAdmin(admin.ModelAdmin):
    list_display = ('title', 'snapshot_type', 'position', 'location',)
admin.site.register(CareerSnapshot, CareerSnapshotAdmin)


class CareerSnapshotAchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'milestone',)
admin.site.register(CareerSnapshotAchievement, CareerSnapshotAchievementAdmin)


class AboutInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(AboutInfo, AboutInfoAdmin)


class TechnologyStackAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(TechnologyStack, TechnologyStackAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology_stack', 'technology_type',)
admin.site.register(Technology, TechnologyAdmin)
