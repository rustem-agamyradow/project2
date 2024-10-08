# Generated by Django 5.1 on 2024-09-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='kurs adyny yazyn', max_length=200, unique=True, verbose_name='Kurs ady')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='courses/', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
