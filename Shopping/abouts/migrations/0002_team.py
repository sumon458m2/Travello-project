# Generated by Django 3.1.1 on 2020-12-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='lesson/')),
            ],
        ),
    ]
