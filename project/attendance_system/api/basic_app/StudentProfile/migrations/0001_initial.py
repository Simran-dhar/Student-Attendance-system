# Generated by Django 2.0.8 on 2019-01-04 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.CharField(default='', max_length=7, unique=True)),
                ('profile_pic', models.ImageField(default='', upload_to='profilepic/')),
                ('mobile_number', models.BigIntegerField(blank=True, default=9999999999)),
            ],
        ),
    ]