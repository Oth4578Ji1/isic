# Generated by Django 5.0.6 on 2024-08-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isicApp', '0010_alter_application_diploma_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='baccalaureate_grade',
            field=models.FloatField(null=True),
        ),
    ]
