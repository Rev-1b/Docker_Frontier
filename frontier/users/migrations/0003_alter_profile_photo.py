# Generated by Django 5.0 on 2023-12-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_is_email_verified_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/%Y/%m/%d', verbose_name='Фотография пользователя'),
        ),
    ]