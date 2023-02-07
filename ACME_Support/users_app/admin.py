from django.contrib import admin

from users_app.models import Ticket, UserProfile,Department



# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Ticket)