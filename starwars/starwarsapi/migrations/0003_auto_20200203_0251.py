# Generated by Django 3.0.2 on 2020-02-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0002_species'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(blank=True, max_length=200)),
                ('planet', models.CharField(blank=True, max_length=200)),
                ('species', models.CharField(blank=True, max_length=200)),
                ('image', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('episode', models.IntegerField()),
                ('opening_crawl', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(blank=True, max_length=200)),
                ('max_speed', models.IntegerField(blank=True)),
                ('passengers', models.IntegerField(blank=True)),
                ('starship_class', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(blank=True, max_length=200)),
                ('max_speed', models.IntegerField(blank=True)),
                ('passengers', models.IntegerField(blank=True)),
                ('vehicle_class', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='planet',
            name='climate',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='planet',
            name='terrain',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='classification',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='language',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
