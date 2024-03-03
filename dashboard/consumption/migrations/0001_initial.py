# Generated by Django 2.2.15 on 2024-03-01 01:03

import consumption.utils.time_utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TariffPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plan_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField(unique=True, verbose_name='ユーザID')),
                ('user_status', models.CharField(choices=[('continuing', 'continuing'), ('stopped', 'stopped'), ('withdrawn', 'withdrawn')], default='continuing', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserContractHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contract_start_at', models.DateTimeField(default=consumption.utils.time_utils.get_local_now_time)),
                ('contract_end_at', models.DateTimeField(blank=True, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.Area')),
                ('tariff_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.TariffPlan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserConsumptionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_at', models.DateTimeField()),
                ('consumption_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.User')),
            ],
        ),
        migrations.AddConstraint(
            model_name='usercontracthistory',
            constraint=models.UniqueConstraint(fields=('user', 'area', 'tariff_plan'), name='user_contract_history_unique'),
        ),
        migrations.AddConstraint(
            model_name='userconsumptionhistory',
            constraint=models.UniqueConstraint(fields=('user', 'measurement_at'), name='user_consumption_history_unique'),
        ),
    ]
