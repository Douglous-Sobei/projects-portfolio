# Generated by Django 4.2.6 on 2023-10-24 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(default='https://github.com'),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='unknown', upload_to='project_images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_duration',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='skills_learnt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
