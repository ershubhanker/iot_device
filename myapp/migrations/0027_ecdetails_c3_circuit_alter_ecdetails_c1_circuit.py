# Generated by Django 4.1.5 on 2023-01-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_rename_c2ab_ecdetails_c1_circuit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecdetails',
            name='c3_circuit',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ecdetails',
            name='c1_circuit',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=30),
        ),
    ]