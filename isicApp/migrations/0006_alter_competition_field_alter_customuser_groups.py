# Generated by Django 5.0.6 on 2024-08-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('isicApp', '0005_alter_customuser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='field',
            field=models.CharField(choices=[('Political Communication', 'Political Communication'), ('Sports Journalism', 'Sports Journalism'), ('Creativity', 'Creativity')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', related_query_name='customuser', to='auth.group'),
        ),
    ]
