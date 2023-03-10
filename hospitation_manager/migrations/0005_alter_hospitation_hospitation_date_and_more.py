# Generated by Django 4.1.5 on 2023-02-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitation_manager', '0004_alter_academicteacher_academic_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitation',
            name='hospitation_date',
            field=models.DateField(blank=True, null=True, verbose_name='hospitation Date'),
        ),
        migrations.AlterField(
            model_name='hospitation',
            name='status',
            field=models.CharField(choices=[('Z', 'Przeprowadzona'), ('O', 'Odwołana'), ('P', 'Planowana'), ('W', 'Oczekuje na przeprowadzenie')], default='W', max_length=1, verbose_name='status'),
        ),
    ]
