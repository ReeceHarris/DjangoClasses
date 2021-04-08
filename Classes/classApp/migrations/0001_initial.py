# Generated by Django 3.2 on 2021-04-08 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=6)),
                ('Course_Number', models.IntegerField()),
                ('Instructor_Name', models.CharField(max_length=60)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]
