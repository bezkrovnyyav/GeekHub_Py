# Generated by Django 4.0.1 on 2022-01-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asksrories',
            fields=[
                ('by', models.CharField(max_length=200)),
                ('descendants', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('kids', models.TextField(null=True)),
                ('score', models.IntegerField()),
                ('text', models.TextField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jobstories',
            fields=[
                ('by', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Newstories',
            fields=[
                ('by', models.CharField(max_length=200)),
                ('descendants', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('kids', models.TextField(null=True)),
                ('score', models.CharField(max_length=200)),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Showstories',
            fields=[
                ('by', models.CharField(max_length=200)),
                ('descendants', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('kids', models.TextField(null=True)),
                ('score', models.IntegerField()),
                ('text', models.TextField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
