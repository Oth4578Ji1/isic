# Generated by Django 5.0.6 on 2024-08-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isicApp', '0012_alter_application_diploma_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='cne',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
