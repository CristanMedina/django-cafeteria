from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Sanction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return f"Penalty for {self.user.username} until {self.end_date}"
