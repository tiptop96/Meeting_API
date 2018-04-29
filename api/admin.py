from django.contrib import admin
from api.models import Meeting, When, Region, Area
from django.http import HttpResponseRedirect
from django.urls import reverse


class WhenInline(admin.StackedInline):
    model = When
    verbose_name_plural = 'When'
    fk_name = 'meeting'

class AjaxedAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(AjaxedAdmin, self).save_model(request, obj, form, change)

    #Security for only allowing editing of your own objects
    def get_queryset(self, request):
        queryset = super(AjaxedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(owner=request.user)
    #Adding when to the Meeting objects in admin
    inlines = (WhenInline,)
    #Seeting upp JS for adress field
    class Media:
        js = (
            'js/region-handle.js',
            'js/geo-fetch.js',
        )
        css = {'all': ('css/admin.css',)}

class AreaInline(admin.TabularInline):
    model = Area
    
class RegionAdmin(admin.ModelAdmin):
    inlines = (AreaInline, )




admin.site.register(Meeting, AjaxedAdmin)
admin.site.register(Region, RegionAdmin)

# Register your models here.
