# Generated by Django 5.0.6 on 2024-08-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isicApp', '0008_alter_application_diploma_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='diploma_category',
            field=models.CharField(blank=True, choices=[('Diplome d`ISIC', 'Diplome d`ISIC'), ('Ordinary License', 'Ordinary License'), ('Professional License', 'Professional License'), ('ISIC Diploma', 'ISIC Diploma')], max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='diploma_grade',
            field=models.CharField(blank=True, choices=[('Not Bad', 'Not Bad'), ('Good', 'Good'), ('Very Good', 'Very Good')], max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='semester_1_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='semester_2_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='semester_3_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='semester_4_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='semester_5_grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='semester_6_grade',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
