from django.db import models
from django.urls import reverse_lazy

from . import const
from . import parameter
from .parameter import TODO_CONFIDENTIAL_DEFAULT

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

#comment
class Comment(models.Model):
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
    body=models.TextField(
        blank=False,
        null=False,
    )
    next=models.ForeignKey(
        'self',
        on_delete=models.CASCADE

    )


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

    target = models.DateTimeField(
        editable=False,
        blank=True,
        null=True
    )

    title=models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    body=models.TextField(
        blank=True,
        null=False
    )
    type=models.IntegerField(
        default=0,
        blank=False,
        null=False
    )
    stage=models.IntegerField(
        default=0,
        blank=False,
        null=False
    )
    confident=models.IntegerField(
        default=TODO_CONFIDENTIAL_DEFAULT,
        blank=False,
        null=False
    )
    # old
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        'self',
        blank=True
    )

    freetags = models.ManyToManyField(
        Tag,
        blank=True
    )
    #old
    status=models.ForeignKey(
        Status,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    #old
    confidentioal=models.ForeignKey(
        Confidentioal,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    comment=models.ForeignKey(
        Comment,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

    def get_type_list(self):
        return TODO_TYPE

    def get_tags_list(self):
        return self.tags.all()

    def is_regularwork(self):
        if self.category.name == "Regular work":
            #print("is_regularowrk:category",self.category,self.title)
            return True
        else:
            return False
    def is_mission(self):
        if self.category.name == "Mission":
            #print("is_mission:category",self.category,self.title)
            return 1
        else:
            return 0
    def is_todo(self):
        #print("is_todo:category:|{}|".format(str(self.category)),type(self.category),type("Todo"))
        if self.category.name == "Todo" and not(self.status.name == "06.Closing"):
            #print("is_todo:categorslf.category,self.title)
            return True
        else:
            return False

    def promote(self) -> bool:
        print("promote:{}".formant(self.stage))
        if self.stage<MAX_TODO_STAGE-1:
            self.stage+=1
            return True
        else:
            print("No update")
            return False

    def demote(self) -> bool:
        print("demote:{}".formant(self.stage))
        if self.stage>0:
            self.stage-=1
            return True
        else:
            print("No update")
            return False
    def insert_comment(self,new_comment) -> bool:
        new_comment.comment=self.comment
        self.comment=new_comment
        return True
