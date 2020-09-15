# Generated by Django 3.1.1 on 2020-09-08 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('expired_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productsize')),
            ],
            options={
                'db_table': 'asks',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('expired_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productsize')),
            ],
            options={
                'db_table': 'bids',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.ask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_asks',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.ask')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.bid')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.AddField(
            model_name='bid',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.status'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='ask',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.status'),
        ),
    ]
