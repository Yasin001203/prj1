from django.db import models
from django.contrib.auth.models import User


class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.from_user} followed {self.to_user}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=1)
    bio = models.TextField(null=True, blank=True)