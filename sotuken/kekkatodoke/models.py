from django.db import models


# Create your models here.
class Kekka(models.Model):
    subject = models.CharField(blank=False, max_length=50)
    student_code = models.CharField(blank=True, max_length=10)
    date = models.DateField(blank=False)
    reason = models.CharField(blank=False, max_length=1000)

    def __str__(self):
        return "{} | {}".format(self.subject, self.student_code)
