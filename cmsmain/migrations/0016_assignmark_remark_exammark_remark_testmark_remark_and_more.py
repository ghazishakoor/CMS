# Generated by Django 5.0.2 on 2024-03-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0015_remove_assignment_location_location_location_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmark',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exammark',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testmark',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]