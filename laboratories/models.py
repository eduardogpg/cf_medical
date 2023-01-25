from django.db import models

class Laboratory(models.Model):
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def created_date(self):
        return 'Fecha de creación'