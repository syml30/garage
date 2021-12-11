from django.db import models
from utils import upload_image_path, get_file_name
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_access = models.BooleanField(default=True)

    # class Meta:
    #     managed = False

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.ForeignKey("self", null=True, blank=True, related_name="child_category",
                                  on_delete=models.SET_NULL)

    # class Meta:
    #     managed = False

    def __str__(self):
        return self.name


class Announcement(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path)
    mobile = models.CharField(max_length=50)
    price = models.BigIntegerField()
    title = models.TextField()
    description = models.TextField()
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    # class Meta:
    #     managed = False

    def __str__(self):
        return self.title


class CategoryAttribute(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=500)
    field_type = models.CharField(max_length=200)
    max = models.IntegerField()
    min = models.IntegerField()
    limiting = models.IntegerField()

    # class Meta:
    #     managed = False

    def __str__(self):
        return f"{self.attribute}-{self.field_type}"


class AnnouncementAttributeValue(models.Model):
    category_attribute_id = models.ForeignKey(CategoryAttribute, on_delete=models.CASCADE)
    announcement_id = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    value = models.CharField(max_length=500)

    # class Meta:
    #     managed = False

    def __str__(self):
        return self.value
