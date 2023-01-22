from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_published = models.BooleanField()
    image = models.ImageField(null=True, blank=True, upload_to="pictures")
    category_id = models.ForeignKey("Categories", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    items = models.ManyToManyField(Ads)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
