from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)

    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="blogs")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    Published_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
