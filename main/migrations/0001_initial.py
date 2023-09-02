# Generated by Django 4.2.4 on 2023-08-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=30)),
                ('social_1', models.CharField(max_length=50, null=True)),
                ('social_2', models.CharField(max_length=50, null=True)),
                ('social_3', models.CharField(max_length=50, null=True)),
                ('social_4', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
