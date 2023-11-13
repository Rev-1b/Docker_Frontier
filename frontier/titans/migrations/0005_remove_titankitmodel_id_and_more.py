# Generated by Django 4.2.7 on 2023-11-08 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titans', '0004_alter_chaptermodel_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titankitmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='titankitmodel',
            name='mp_descr',
        ),
        migrations.RemoveField(
            model_name='titankitmodel',
            name='mp_image',
        ),
        migrations.RemoveField(
            model_name='titankitmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='titankitmodel',
            name='slug',
        ),
        migrations.AddField(
            model_name='titankitmodel',
            name='abstractequipmentmodel_ptr',
            field=models.OneToOneField(auto_created=True, default=12, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='titans.abstractequipmentmodel'),
            preserve_default=False,
        ),
    ]
