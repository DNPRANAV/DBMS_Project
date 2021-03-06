# Generated by Django 2.1.3 on 2019-05-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=15)),
                ('dob', models.DateField()),
                ('birthPlace', models.CharField(max_length=1000)),
                ('biography', models.CharField(max_length=1000)),
                ('photo', models.ImageField(blank=True, upload_to='actors')),
                ('maritalStatus', models.CharField(max_length=120)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=15)),
                ('dob', models.DateField()),
                ('birthPlace', models.CharField(max_length=1000)),
                ('biography', models.CharField(max_length=1000)),
                ('photo', models.ImageField(blank=True, upload_to='actors')),
                ('maritalStatus', models.CharField(max_length=120)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=15)),
                ('dob', models.DateField()),
                ('birthPlace', models.CharField(max_length=1000)),
                ('biography', models.CharField(max_length=1000)),
                ('photo', models.ImageField(blank=True, upload_to='actors')),
                ('maritalStatus', models.CharField(max_length=120)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='producer',
            name='profession',
            field=models.ManyToManyField(to='cast.profession'),
        ),
        migrations.AddField(
            model_name='director',
            name='profession',
            field=models.ManyToManyField(to='cast.profession'),
        ),
        migrations.AddField(
            model_name='cast',
            name='profession',
            field=models.ManyToManyField(to='cast.profession'),
        ),
    ]
