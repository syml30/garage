import itertools

from django.shortcuts import render

from app.models import Announcement
# from sliders.models import Slider
from settings.models import SiteSetting


def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.filter()
    context = {
        "setting": site_setting
    }
    return render(request, "shared/Header.html", context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.filter()

    context = {
        "setting": site_setting

    }
    return render(request, "shared/Footer.html", context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# def home_page(request):
#     # sliders = Slider.objects.all()
#     most_visit_announcement = Announcement.objects.order_by("-visit_count").all()[:8]
#
#     latest_announcement = Announcement.objects.order_by("-id").all()[:8]
#     context = {
#         "data": "این سایت فروشگاهی با فریم ورک django نوشته شده است",
#         # "sliders": sliders,
#         "most_visit": my_grouper(4, most_visit_announcement),
#         "latest_products": my_grouper(4, latest_announcement),
#     }
#     return render(request, "home_page.html", context)


def home_page(request):
    return render(request, "home_page.html")


def about_page(request):
    site_setting = SiteSetting.objects.filter()
    context = {
        "setting": site_setting
    }
    return render(request, "about_page.html", context)
