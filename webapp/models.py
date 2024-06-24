from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]


class Task(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.description
