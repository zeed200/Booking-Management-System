# Generated by Django 4.2.5 on 2024-04-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0020_alter_reservecha_st_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserveape',
            name='st_book',
            field=models.CharField(choices=[('sure', 'مؤكد'), ('notsure', 'غير مؤكد'), ('cancel', 'ملغي')], max_length=20, null=True, verbose_name='الحاله'),
        ),
    ]
