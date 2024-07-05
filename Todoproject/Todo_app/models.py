from django.db import models

class TodoTask(models.Model):
    title = models.CharField(max_length=100 )
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.title)