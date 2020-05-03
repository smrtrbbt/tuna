# Generated by Django 3.0.5 on 2020-05-03 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('icon_url', models.CharField(max_length=1028)),
                ('max_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('scalecolor', models.IntegerField()),
                ('displayname', models.CharField(max_length=64)),
                ('icon_url', models.CharField(max_length=1028)),
                ('shoal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoal.Shoal')),
            ],
        ),
    ]