# Generated by Django 3.1.7 on 2021-04-15 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_page', '0002_auto_20210402_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admitting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='An_object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category_of_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entrusted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer_work_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team_members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='To_observer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Work_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='employee_time',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.employee'),
        ),
        migrations.CreateModel(
            name='create_e_naryad_table_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_preparedness_time', models.DateField()),
                ('start_work', models.DateField()),
                ('finish_work', models.DateField()),
                ('workplace_preparation_text1', models.TextField()),
                ('workplace_preparation_text2', models.TextField()),
                ('workplace_preparation_text3', models.TextField()),
                ('admitting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.admitting')),
                ('an_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.an_object')),
                ('category_of_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.category_of_work')),
                ('entrusted', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.entrusted')),
                ('manufacturer_work_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.manufacturer_work_manager')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.organization')),
                ('plot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.plot')),
                ('subdivision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.subdivision')),
                ('team_members', models.ManyToManyField(to='a_page.Team_members')),
                ('to_observer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.to_observer')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.employee')),
                ('work_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_page.work_manager')),
            ],
        ),
    ]
