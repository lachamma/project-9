from django.contrib import admin
from app1.models import Blog,Review

# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display=['title','author','date','body']
    search_fields=['title']
class ReviewAdmin(admin.ModelAdmin):
    list_display=['blog','rating','date','reviewarea']
admin.site.register(Blog,BlogAdmin)
admin.site.register(Review,ReviewAdmin)