# Generated by Django 2.0 on 2018-04-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0004_auto_20180412_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='id_card',
            field=models.CharField(max_length=20),
        ),
    ]