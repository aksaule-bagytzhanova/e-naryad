# Generated by Django 3.1.7 on 2021-05-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_page', '0012_create_e_naryad_table_3_create_e_naryad_table_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сreate_e_naryad_table_1',
            name='signature',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
