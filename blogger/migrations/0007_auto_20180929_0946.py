# Generated by Django 2.0 on 2018-09-29 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_auto_20180925_1900'),
    ]

    operations = [
        #migrations.RemoveField(
            #model_name='userprofile',
            #name='id',
        #),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
