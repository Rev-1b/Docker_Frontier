# Generated by Django 4.2.7 on 2023-11-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param1', models.CharField(max_length=256)),
                ('param2', models.IntegerField()),
                ('param3', models.DateTimeField(auto_now_add=True)),
                ('param4', models.BooleanField(default=True)),
            ],
        ),
    ]