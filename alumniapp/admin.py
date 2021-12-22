from django.contrib import admin
from . import models
from users.models  import NewUser


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'first_name')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'town', 'city', 'state', 'slug')

class SetAdmin(admin.ModelAdmin):
    list_display = ('set_Name', 'school_Name', 'date_created', 'members')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile', 'profile_Picture')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('last_Name','first_Name', 'email', 'school_Name', 'year_Graduated')


admin.site.register(NewUser, UserAdmin)
admin.site.register(models.School, SchoolAdmin)
# admin.site.register(Set, SetAdmin)
# admin.site.register( Administrator)
# admin.site.register(Member, MemberAdmin)
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Year)