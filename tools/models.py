from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50, null=True)
    photo = models.URLField(null=True)

    def __str__(self):
        return self.name
        