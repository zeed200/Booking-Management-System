# Generated by Django 4.2.5 on 2024-04-15 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0022_remove_operation_customers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='user',
            field=models.ForeignKey(default='abdalrahman', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم'),
        ),
    ]
