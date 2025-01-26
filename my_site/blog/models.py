from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    tags = models.CharField(max_length=20)

    def __str__(self):
        return self.tags

class Author(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    Content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author ,on_delete=models.SET_NULL,null=True,related_name="posts")
    tag = models.ManyToManyField(Tag)


