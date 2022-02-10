from django.contrib import admin
from django.contrib.auth.models import Group

from applications.user.models import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.unregister(Group)
