from django.contrib import admin

from .models import Issue, Message

admin.site.register(Message)


class IssueMessageInline(admin.TabularInline):
    model = Message
    readonly_fields = (
        "timestamp",
        "issue_id",
        "user_id",
    )
    extra = 1


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    inlines = [IssueMessageInline]
