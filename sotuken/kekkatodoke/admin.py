from django.contrib import admin

# Register your models here.
from .models import Kekka


class KekkaAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student_code', 'date')
    list_display_links = ('subject', 'student_code')


admin.site.register(Kekka, KekkaAdmin)
