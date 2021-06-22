from django.contrib import admin
from .models import Task


admin.site.register(Task)


admin.site.index_title = "Django Title"

admin.site.site_header = "Django Header"

admin.site.site_title = "Django Title"
