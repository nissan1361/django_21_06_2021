# Generated by Django 3.2.4 on 2021-07-27 17:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210722_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 17, 54, 56, 666400)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='возраст'),
        ),
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_line', models.CharField(blank=True, max_length=128, verbose_name='теги')),
                ('about_me', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('W', 'Ж')], max_length=1, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
