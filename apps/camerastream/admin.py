from django.contrib import admin
from .models import *




admin.site.register(Camers)
admin.site.register(EntryLog)
admin.site.register(FalseEntryLog)

admin.site.site_title = 'Админ-панель сайта Video Control'
admin.site.site_header = 'Админ-панель сайта Video Control'

