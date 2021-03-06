# Generated by Django 3.0.4 on 2020-03-16 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0002_auto_20200316_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
            preserve_default=False,
        ),
    ]
