# Generated by Django 3.1.2 on 2021-02-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pews', '0006_newslist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newslist',
            name='textcontent',
        ),
        migrations.AddField(
            model_name='newslist',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf'),
        ),
    ]