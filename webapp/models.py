from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]


class Task(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(blank=True, null=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"
