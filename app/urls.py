from django.urls import path
from .views import AnnouncementList, AnnouncementDetail, add_announcement_view

urlpatterns = [
    path('announcement-list/', AnnouncementList.as_view(), name="announcement_list"),
    path('announcement-detail/<int:pk>/', AnnouncementDetail.as_view(), name="announcement_detail"),

    path('add-announcement-view/', add_announcement_view, name="add_announcement"),
]
