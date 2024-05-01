# Generated by Django 5.0.2 on 2024-03-14 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0024_alter_exammark_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmark',
            name='assignment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cmsmain.assignment'),
        ),
        migrations.AlterField(
            model_name='testmark',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='testmarks', to='cmsmain.test'),
        ),
    ]
