from django.contrib import admin
from .models import Announcement, AnnouncementAttributeValue, Category, CategoryAttribute, Profile

admin.site.register(Announcement)
admin.site.register(AnnouncementAttributeValue)
admin.site.register(Category)
admin.site.register(CategoryAttribute)
admin.site.register(Profile)
