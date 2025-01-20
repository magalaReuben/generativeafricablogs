from django.contrib import admin
from .models import Blog, Section, SubSection, Tag

# Register your models here.
admin.site.register(Blog)
admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(Tag)
