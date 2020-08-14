from django.db import models


class User(models.Model):
    user = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return f"{self.user} {self.created_at}"


class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "message"

    def __str__(self):
        return f"{self.user.user} : {self.content}"
