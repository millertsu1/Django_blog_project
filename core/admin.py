from django.contrib import admin
from.models import Category, Tag, Post, About, Link

# Register your models here.

admin.site.site_header = 'Administracion de [Nom]'

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display =('name','active','created')

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display =('name','active','created')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display =('title','published','category','author', 'created')
    ordering = ('author', '-created')
    search_fields = ('title','content', 'category__name', 'author__username')
    list_filter = ('author','category', 'tags' )

    def post_tags(self, obj):
        return ' - '.join([t.name for t in obj.tags.all().order_by('name')])

    post_tags.short_description = 'Etiquetas'

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display =('description','created')
    
admin.site.register(About,AboutAdmin)

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display =('name','key','url','icon')

admin.site.register(Link, LinkAdmin)