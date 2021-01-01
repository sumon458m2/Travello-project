# Generated by Django 3.1.1 on 2020-12-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_destinate'),
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='destinate/')),
            ],
        ),
    ]
