# Generated by Django 5.0.2 on 2024-03-11 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0021_remove_exammark_student_alter_assignmark_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammark',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exammarks', to='cmsmain.student'),
        ),
    ]
