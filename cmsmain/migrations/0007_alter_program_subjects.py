# Generated by Django 5.0.2 on 2024-02-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0006_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='subjects',
            field=models.ManyToManyField(to='cmsmain.subject'),
        ),
    ]
