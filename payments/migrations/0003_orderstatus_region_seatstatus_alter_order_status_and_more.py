# Generated by Django 4.2.19 on 2025-02-10 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_seatclass_order_count_seats_alter_order_status_seat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeatStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold')], max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='payments.orderstatus'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='payments.seatstatus'),
        ),
        migrations.AlterField(
            model_name='seatclass',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.region'),
        ),
    ]
