# Generated by Django 3.2.12 on 2022-06-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
