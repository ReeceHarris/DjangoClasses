from django.db import models

# Create your models here.


class DjangoClasses(models.Model):
    Title = models.CharField(max_length=6)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.FloatField()

    objects = models.Manager()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.Model = None
