from django.contrib import admin
from .models import userProfile, tag, post

# Register your models here.
@admin.register(tag)
class tagAdmin(admin.ModelAdmin):
    model = tag

@admin.register(userProfile)
class userProfileAdmin(admin.ModelAdmin):
    model = userProfile
    
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    model = post

    list_display = (
        "id", "title", "subtitle", "slug", "publish_date", "published"
    )

    list_editable = (
        "title", "subtitle", "slug", "published"
    )   

    search_fields = (
        "title", "subtitle", "slug", 
    )

    readonly_fields = (
        "publish_date",
    )

    prepopulated_fields = {
        "slug": ("title","subtitle")
    }

    date_hierarchy = "publish_date"

    save_on_top = True

    
