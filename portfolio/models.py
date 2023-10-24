from django.db import models

DURATION_CHOICES = [
    ('years', 'Years'),
    ('months', 'Months'),
    ('days', 'Days'),
]


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_duration = models.PositiveIntegerField(default=0)
    duration_unit = models.CharField(
        max_length=10, choices=DURATION_CHOICES, default='years')
    skills_learnt = models.TextField(null=True, blank=True)
    github_link = models.URLField(default='unknown')
    image = models.ImageField(upload_to='project_images/', default='unknown')

    def __str__(self):
        return self.title
