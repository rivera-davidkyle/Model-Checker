# Generated by Django 4.1.5 on 2023-02-01 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('csv', models.FileField(upload_to='')),
                ('hash', models.CharField(blank=True, max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'CSV',
                'verbose_name_plural': 'CSVs',
            },
        ),
        migrations.CreateModel(
            name='PredModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auc', models.IntegerField()),
                ('model', models.CharField(blank=True, max_length=40)),
                ('param', models.CharField(blank=True, max_length=100)),
                ('csv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.csv')),
            ],
            options={
                'verbose_name': 'PredModel',
                'verbose_name_plural': 'PredModels',
            },
        ),
    ]