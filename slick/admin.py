from django.contrib import admin
from models import *
from adminsortable.admin import SortableInlineAdminMixin

class ElementAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Element


class SlickAdmin(admin.ModelAdmin):
    inlines = [ElementAdmin]


admin.site.register(Slick, SlickAdmin)