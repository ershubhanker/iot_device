# Generated by Django 4.1.5 on 2023-01-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_ecdetails_c1'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecdetails',
            name='c1ab',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecdetails',
            name='c2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecdetails',
            name='c2ab',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecdetails',
            name='c3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecdetails',
            name='c3ab',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecdetails',
            name='c4',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecdetails',
            name='c4ab',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
