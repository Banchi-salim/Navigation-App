# Generated by Django 4.2.5 on 2023-10-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('locator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniAbujaCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Campus',
        ),
    ]
