# Generated by Django 4.2.2 on 2023-06-28 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='App.level')),
            ],
        ),
    ]
