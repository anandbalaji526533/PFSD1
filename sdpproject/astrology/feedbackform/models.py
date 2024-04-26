from django.db import models

class Feedback(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Firstname
