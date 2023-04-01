from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# ======{ Профиль }======
class Nationality(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Гражданство"
        verbose_name_plural = "Гражданство"

    def __str__(self):
        return self.title


class Gender(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Гендер"
        verbose_name_plural = "Гендер"

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(verbose_name="Пользователь", to=User, on_delete=models.CASCADE)
    nationality = models.ForeignKey(to=Nationality, on_delete=models.SET_NULL, null=True, verbose_name="Гражданство")
    gender = models.ForeignKey(to=Gender, on_delete=models.SET_NULL, null=True, verbose_name="Гендер")
    birth_year = models.IntegerField()

    class Meta:
        verbose_name = "Расширенный пользователь"
        verbose_name_plural = "Расширенные пользователи"

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user).save()

