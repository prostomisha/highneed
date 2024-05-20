from opencage.geocoder import OpenCageGeocode
from django import template




key = '9a0b248571d4434087f0a16b65793a3c'
geocoder = OpenCageGeocode(key)
register = template.Library()
@register.simple_tag
def GeoCode(ulica):
    query = str(ulica)
    results = geocoder.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    coords = [lat, lng]
    return lat, lng

