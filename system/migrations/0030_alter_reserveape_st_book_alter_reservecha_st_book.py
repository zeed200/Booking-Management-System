# Generated by Django 4.2.5 on 2024-05-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0029_alter_reserveape_st_book_alter_reservecha_st_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserveape',
            name='st_book',
            field=models.CharField(choices=[('sure', 'مؤكد'), ('notsure', 'غير مؤكد'), ('cancel', 'ملغي'), ('done', 'منتهي')], default='notsure', max_length=20, null=True, verbose_name='الحاله'),
        ),
        migrations.AlterField(
            model_name='reservecha',
            name='st_book',
            field=models.CharField(choices=[('sure', 'مؤكد'), ('notsure', 'غير مؤكد'), ('cancel', 'ملغي'), ('done', 'منتهي')], default='notsure', max_length=20, null=True, verbose_name='الحاله'),
        ),
    ]
