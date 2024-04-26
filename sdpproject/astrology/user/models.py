from django.db import models

gender_choices = {
    ('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')
}


# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(blank=False, choices=gender_choices, max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=8, blank=False)
    contact = models.BigIntegerField(blank=False,max_length=10)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "register_table"

    def __str__(self):
        return f"{self.name}--registerd_date-- {self.date}"


# astrology_app/models.py

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
