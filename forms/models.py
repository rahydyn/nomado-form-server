from django.db import models


class Form(models.Model):
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    userId = models.CharField(max_length=50)
    formId = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title