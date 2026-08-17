from django.contrib import admin
from website.models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    #list_disply
    def short_bio(self, obj):
        return obj.bio[:20] + '...'



    #ModelAdmin
    list_display = ('id','name','headline', 'short_bio', 'email')
    search_fields = ('id','name','headline', 'bio', 'email')
    list_filter = ('id','name','headline', 'bio', 'email')
    list_per_page = 20


admin.site.register(Profile, ProfileAdmin)