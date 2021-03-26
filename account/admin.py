from django.contrib import admin
from .models import MyUser, Relation


@admin.register(MyUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    # prepopulated_fields = {'slug': ('first_name', 'last_name')}

admin.site.register(Relation)