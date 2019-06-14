from django.contrib import admin

# Register your models here.
from.models import Post,Comment
class Postadmin(admin.ModelAdmin):
    list_display = ['tittle','slug','author','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('tittle',)}
    list_filter = ('status','author','created','publish')
    search_fields = ('tittle','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
class Commentadmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']
    list_filter = ('created','active','updated')
    search_fields = ('name','email','body')
admin.site.register(Comment,Commentadmin,)
admin.site.register(Post,Postadmin)


