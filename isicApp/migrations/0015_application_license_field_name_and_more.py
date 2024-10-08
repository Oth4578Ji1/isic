# Generated by Django 5.0.6 on 2024-08-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isicApp', '0014_rename_cne_application_cne'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='license_field_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='université',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('AR', 'Arabic')], default='AR', max_length=2),
        ),
    ]
