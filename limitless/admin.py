from django.conf import settings
from django.contrib import admin

admin.site.site_title = "Limitless Admin"
admin.site.site_header = f"Limitless - v{settings.VERSION}"
admin.site.index_title = "Site Administration"
