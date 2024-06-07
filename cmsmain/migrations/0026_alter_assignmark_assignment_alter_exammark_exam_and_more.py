# Generated by Django 5.0.2 on 2024-03-15 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0025_alter_assignmark_assignment_alter_testmark_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmark',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsmain.assignment'),
        ),
        migrations.AlterField(
            model_name='exammark',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exammarks', to='cmsmain.exam'),
        ),
        migrations.AlterField(
            model_name='testmark',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testmarks', to='cmsmain.test'),
        ),
    ]