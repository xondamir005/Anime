from django.contrib import admin
from .models import Places, PlaceDetail, OrderPlaces, Gallarey, TravelGallarey, ContactUs, Rate, LogoutModel

admin.site.register(Places)
admin.site.register(OrderPlaces)
admin.site.register(PlaceDetail)
admin.site.register(Gallarey)
admin.site.register(TravelGallarey)
admin.site.register(ContactUs)
admin.site.register(Rate)
admin.site.register(LogoutModel)

