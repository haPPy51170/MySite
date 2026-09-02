from django.contrib import admin

from website.models import *


class ProfileAdmin(admin.ModelAdmin):


    def short_bio_fa(self, obj):
        return obj.bio_fa[:20] + "..."

    short_bio_fa.short_description = "Summary of Bio fa"

    def short_bio_en(self, obj):
        return obj.bio_en[:20] + "..."

    short_bio_en.short_description = "Summary of Bio en"

    def short_bio_login(self, obj):
        return obj.bio_en[:20] + "..."

    short_bio_login.short_description = "Summary of Bio login"


    list_display = (
        "id",
        "name_fa",
        "name_en",
        "name_en_highlight",
        "short_bio_fa",
        "short_bio_en",
        "short_bio_login",
        "status_fa",
        "status_en",
        "email",
        "github",
        "linkedin",
        "location",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name_fa",
        "name_en",
        "bio_fa",
        "bio_en",
        "email",
        "location",
    )

    list_filter = (
        "location",
    )

    ordering = (
        "-updated_at",
    )

    list_per_page = 20


class HeadlineAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "text",
        "order",
    )

    ordering = (
        "order",
    )

    search_fields = (
        "text",
    )

    list_editable = (
        "order",
    )


class StatAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "value",
        "label",
        "order",
    )

    search_fields = (
        "value",
        "label",
    )

    ordering = (
        "order",
    )

    list_editable = (
        "order",
    )


class AboutCardAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "icon",
        "description",
        "order",
    )

    ordering = (
        "order",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "order",
    )


class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "percentage",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "percentage",
    )

    ordering = (
        "-percentage",
    )


class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "tag",
        "url",
        "description",
        "image",
    )

    search_fields = (
        "title",
        "description",
        "tag",
    )

    list_filter = (
        "tag",
    )


class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "description",
        "published_at",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-published_at",
    )

    date_hierarchy = "published_at"


class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = (
        "-created_at",
    )

    date_hierarchy = "created_at"


class SocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "url",
        "icon",
    )

    search_fields = (
        "url",
        "icon",
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Headline, HeadlineAdmin)
admin.site.register(AboutCard, AboutCardAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Stat, StatAdmin)