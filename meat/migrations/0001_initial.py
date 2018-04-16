# Generated by Django 2.0 on 2018-04-16 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='CollectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sg_no', models.CharField(max_length=50)),
                ('pay_type', models.IntegerField(default=1)),
                ('sg_price', models.FloatField(default=0)),
                ('sg_datetime', models.DateTimeField(auto_now=True)),
                ('tzq_datetime', models.DateTimeField(blank=True, null=True)),
                ('tt_datetime', models.DateTimeField(blank=True, null=True)),
                ('cz_weight', models.FloatField(default=0)),
                ('cz_weight2', models.FloatField(default=0)),
                ('cz_weight3', models.FloatField(default=0)),
                ('cz_number', models.IntegerField(default=0)),
                ('cz_number2', models.IntegerField(default=0)),
                ('cz_number3', models.IntegerField(default=0)),
                ('sg_source', models.CharField(default='', max_length=100)),
                ('c_type', models.CharField(max_length=20)),
                ('c_standard', models.CharField(max_length=20)),
                ('c_level', models.CharField(max_length=20)),
                ('state', models.IntegerField(default=1)),
                ('flow_step', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(max_length=20)),
                ('cust_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_key', models.CharField(max_length=50)),
                ('item_val', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=20)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.IntegerField(default=1)),
                ('live_buy_price', models.FloatField(default=0)),
                ('live_tare', models.FloatField(default=0)),
                ('live_weigh_number', models.IntegerField(default=5)),
                ('ketobody_weigh_number', models.IntegerField(default=5)),
                ('ketobody_buy_price', models.FloatField(default=0)),
                ('ketobody_tare', models.FloatField(default=0)),
                ('unit_of_weight', models.CharField(default='KG', max_length=10)),
                ('unit_of_number', models.CharField(default='只(头)', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='collectinfo',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meat.Customer'),
        ),
        migrations.AddField(
            model_name='collectinfo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectinfo',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectinfo',
            name='user3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accessmodule',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='meat.Module'),
        ),
    ]
