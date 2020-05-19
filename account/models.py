from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)
    photo = models.ImageField('Фото',upload_to='media/avatar', default='media/default.JPG', blank=True)
    email = models.EmailField('Почта')
    number = models.CharField('Номер', max_length=20)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        instance.profile.save()