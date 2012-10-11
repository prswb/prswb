from django.contrib import admin

from models import Website


class WebsiteAdmin(admin.ModelAdmin):
    class Meta:
        model = Website


admin.site.register(Website, WebsiteAdmin)