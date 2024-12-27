from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"title: {self.title}"
