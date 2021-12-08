from django.shortcuts import render, redirect, reverse
from .models import Announcement, Profile, Category, CategoryAttribute, AnnouncementAttributeValue
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView


class AnnouncementList(ListView):
    model = Announcement
    queryset = Announcement.objects.all()
    template_name = "app/announcement_list.html"
    context_object_name = "announcements_list"
    paginate_by = 2


class AnnouncementDetail(DetailView):
    model = Announcement
    queryset = Announcement.objects.all()
    template_name = "app/announcement_detail.html"
    context_object_name = "announcements_detail"


@require_http_methods(["POST", "GET"])
def add_announcement_view(request):
    if request.method=='GET':
        return render(request,"app/advertisement_registration.html")
    if request.method == "POST":
        city = request.POST.get('city')
        image = request.POST.get('image')
        mobile = request.POST.get('mobile')
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        # pid = request.POST.get('pid')
        Announcement.objects.create(city=city, image=image, mobile=mobile, title=title, price=price,
                                    description=description, user_id=request.user.id)
    return redirect(reverse("announcement_list"))
