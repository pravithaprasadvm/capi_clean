# Generated by Django 4.1.7 on 2023-03-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capiclean', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=100)),
                ('Salary', models.IntegerField()),
                ('Qualification', models.CharField(max_length=200)),
            ],
        ),
    ]