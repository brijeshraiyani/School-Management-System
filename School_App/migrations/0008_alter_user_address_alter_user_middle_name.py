# Generated by Django 4.1.5 on 2023-01-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_App', '0007_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
