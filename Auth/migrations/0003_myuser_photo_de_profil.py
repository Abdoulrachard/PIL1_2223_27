# Generated by Django 4.2.2 on 2023-07-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_rename_level_myuser_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='photo_de_profil',
            field=models.ImageField(blank=True, null=True, upload_to='photos_de_profil/'),
        ),
    ]
