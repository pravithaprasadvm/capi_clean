# Generated by Django 4.1.7 on 2023-03-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capiclean', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Email',
            field=models.CharField(max_length=20),
        ),
    ]
