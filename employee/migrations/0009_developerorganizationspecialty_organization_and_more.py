# Generated by Django 4.1.5 on 2023-01-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('employee', '0008_developerorganizationspecialty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerorganizationspecialty',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AddField(
            model_name='developerorganizationspecialty',
            name='organization_developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='specialty',
            field=models.ManyToManyField(to='employee.developerorganizationspecialty'),
        ),
    ]
