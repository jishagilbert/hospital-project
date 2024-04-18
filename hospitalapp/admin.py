from django.contrib import admin

from hospitalapp.models import Department, Doctors, Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Booking)
