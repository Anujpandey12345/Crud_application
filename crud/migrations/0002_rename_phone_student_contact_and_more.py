# Generated by Django 5.1.7 on 2025-03-30 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Phone',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='FirstName',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='LastName',
            new_name='Lastname',
        ),
    ]
