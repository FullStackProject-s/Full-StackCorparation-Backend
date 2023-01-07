# Generated by Django 4.1.5 on 2023-01-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_developer_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='skill_level',
            field=models.CharField(choices=[('jun', 'Junior'), ('jun_pl', 'Junior Plus'), ('middle', 'Middle'), ('mid_pl', 'Middle Plus'), ('sen', 'Senior')], default='jun', max_length=200),
        ),
    ]
