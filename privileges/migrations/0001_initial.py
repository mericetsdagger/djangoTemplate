# Generated by Django 3.0 on 2020-09-15 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userProfile', '0002_auto_20200901_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='FishDist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtName', models.CharField(max_length=250)),
                ('localization', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'fish_dist',
            },
        ),
        migrations.CreateModel(
            name='PrvType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishingDistrictId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='privileges.FishDist')),
            ],
            options={
                'db_table': 'prv_type',
            },
        ),
        migrations.CreateModel(
            name='Prvs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.UserProfile')),
                ('prvTypeId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='privileges.PrvType')),
            ],
            options={
                'db_table': 'prvs',
            },
        ),
        migrations.CreateModel(
            name='FishAsso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associationName', models.CharField(max_length=200)),
                ('fishingDistrictId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='privileges.FishDist')),
            ],
            options={
                'db_table': 'fish_asso',
            },
        ),
    ]
