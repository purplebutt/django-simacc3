from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django.shortcuts import reverse
from media.api.manager import resize_image, delete_model_image

class Profile(models.Model):
    _img_path = 'images/profile/'
    _img_def_path = 'images/default/profile.png'
    _gender = [('female', 'Female'), ('male', 'Male')]
    _level = [
        (0, 'Magang'),
        (1, 'Outsource'),
        (2, 'Training'),
        (3, 'Junior Staff'),
        (4, 'Staff'),
        (5, 'Senior Staff'),
        (6, 'Junior Manager'),
        (7, 'Manager'),
        (8, 'Senior Manager'),
        (9, 'Junior Director'),
        (10, 'Director'),
        (11, 'Senior Director'),
        (12, 'Owner'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=_img_path, default=_img_def_path)
    gender = models.CharField(max_length=6, choices=_gender, blank=True)
    address = models.CharField(max_length=125, blank=True)
    city = models.CharField(max_length=63, blank=True)
    phone = models.CharField(max_length=18, blank=True)
    level = models.SmallIntegerField("level", choices=_level, default=4)
    dob = models.DateTimeField(verbose_name='date of birth', blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return f'{self.user.username.capitalize()} profile'

    def get_detail_url(self):
        return reverse("accounts:profile_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)

        if settings.DEBUG:
            delete_model_image(self, Profile, Profile._img_def_path) 
            super(Profile, self).save(*args, **kwargs)
            resize_image(self.image.path)
        else:
            super(Profile, self).save(*args, **kwargs)
