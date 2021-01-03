from django.contrib import admin
from .models import User, Country, City, District, Town


admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Town)
