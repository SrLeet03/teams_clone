from django.contrib import admin
from .models import Team, Channel, Message
# Register your models here.

admin.site.register(Team)
admin.site.register(Channel)
admin.site.register(Message)
