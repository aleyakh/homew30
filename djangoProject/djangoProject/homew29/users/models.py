from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE = [("member", "Пользователь"), ("moderator", "Модератор"), ("admin", "Администратор")]

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=9, choices=ROLE, default="member")
    age = models.PositiveSmallIntegerField()
    locations = models.ManyToManyField("Location")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
