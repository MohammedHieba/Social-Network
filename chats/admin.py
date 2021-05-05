from django.contrib import admin

from chats.models import Chat, Message


class MessagesContent(admin.TabularInline):
    model = Message


class DisplayUser(admin.ModelAdmin):
    list_display = ('id', 'first_user', 'second_user', 'last_updated_at')
    search_fields = ('id', 'first_user__username', 'second_user__username')
    inlines = [MessagesContent]
    ordering = ['id']

    class Meta:
        model = Chat


admin.site.register(Chat, DisplayUser)
