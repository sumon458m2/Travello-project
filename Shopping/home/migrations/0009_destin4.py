# Generated by Django 3.1.1 on 2021-01-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_destin3'),
    ]

    operations = [
        migrations.CreateModel(
            name='destin4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
