# Generated by Django 3.1.3 on 2020-11-30 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('real_estate_api', '0011_auto_20201130_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='real_estate_api_company_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='company',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='real_estate_api_company_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='estate',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='real_estate_api_estate_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='estate',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='real_estate_api_estate_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
    ]