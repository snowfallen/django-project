# Generated by Django 4.2.1 on 2023-05-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=models.TextField(null=True),
        ),
    ]
