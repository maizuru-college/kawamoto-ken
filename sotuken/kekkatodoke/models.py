from django.db import models


# Create your models here.
class Notification(models.Model):
    student_code = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    absent_date = models.DateField()
    reason = models.CharField(max_length=1000)

    def __str__(self):
        return "{} | {} | {}".format(self.student_code, self.subject,
                                     self.absent_date)


class Student(models.Model):
    student_code = models.CharField(max_length=10)
    student_class = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "{} | {} | {}".format(self.student_name, self.student_code,
                                     self.student_class)
