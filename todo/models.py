from django.db import models
from django.urls import reverse_lazy


# Create your models here.
#Todo category
class Category(models.Model):
    name=models.CharField(
        max_length=63,
        blank=False,
        null=False,
        unique=True
    )
    def __str__(self):
        return self.name

# Todo tag
class Tag(models.Model):
    name=models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    def __str__(self):
        return self.name

# Todo const status
class Status(models.Model):
    name=models.CharField(
        max_length=63,
        blank=False,
        null=False,
        unique=True
    )
    def __str__(self):
        return self.name

# Todo const confidentioal level
class Confidentioal(models.Model):
    name=models.CharField(
        max_length=63,
        blank=False,
        null=False,
        unique=True,
    )
    def __str__(self):
        return self.name



# Todo
class Todo(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False
    )
    '''
    target = models.DateTimeField(
        editable=False,
        blank=True,
        null=True
    )'''

    title=models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    body=models.TextField(
        blank=False,
        null=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
    status=models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    confidentioal=models.ForeignKey(
        Confidentioal,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])
