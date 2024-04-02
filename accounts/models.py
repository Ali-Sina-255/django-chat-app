from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save


def user_director_path(instance, filename):
    return "user_{0} / {1}".format(instance.user.id, filename)


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    bio = models.TextField()
    images = models.ImageField(
        upload_to=user_director_path, default='default.jpg')
    website = models.URLField(default='https://google.com')
    facebook = models.URLField(default='https://facebook.com')
    twitter = models.URLField(default='https://twitter.com')
    instagram = models.URLField(default='https://instagram.com')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return f"{self.full_name} - {self.user.username} - {self.user.email}"
        except:
            return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.images.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.images.path)

           
def create_user_profile(sender, created, instance, **kwargs):
    if created:
        Profiles.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profiles.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
