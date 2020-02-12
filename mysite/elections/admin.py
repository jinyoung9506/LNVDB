from django.contrib import admin

from . models import Candidate, Poll
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Poll)