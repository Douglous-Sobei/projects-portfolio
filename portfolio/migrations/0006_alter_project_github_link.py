# Generated by Django 4.2.6 on 2023-10-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_project_google_drive_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(default='unknown'),
        ),
    ]