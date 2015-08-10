from django.contrib import admin

# Register your models here.
from UserManager.models import UserInformation


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'createTime')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('username',)
    date_hierarchy = 'createTime'
    ordering = ('-username',)
    fields = ('username', 'password', 'first_name', 'last_name', 'email', 'createTime')


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'createTime')
#     list_filter = ('createTime',)
#     date_hierarchy = 'createTime'
#     ordering = ('-createTime',)
#     fields = ('username', 'password', 'createTime', 'userInfo')

admin.site.register(UserInformation, UserInfoAdmin)
# admin.site.register(User, UserAdmin)
# admin.site.register(UserInformation)
# admin.site.register(User)
#
# admin.site.register(TestUser)
# admin.site.register(TestGroup)
