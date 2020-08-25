from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class user_details(models.Model):
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    email_id = models.CharField(max_length=300, null=True)
    password = models.CharField(max_length=100, null=True)
    address_1 = models.CharField(max_length=200, null=True)
    address_2 = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zip = models.IntegerField()

    def __str__(self):
        return self.email_id

class user_posts(models.Model):
    STATES = [
        ('draft', 'draft'),
        ('pending', 'pending'),
        ('published', 'published'),
        ('rejected', 'rejected'),
        ('delete', 'delete'),
        ('saved', 'saved'),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=300, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    state = models.CharField(max_length=20, default='draft', choices=STATES)
