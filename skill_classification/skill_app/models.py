from django.db import models

# Create your models here.
class PredResults(models.Model):

    skill=models.TextField()
    classification = models.CharField(max_length=100)

    def __str__(self):
        return self.classification