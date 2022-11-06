# Generated by Django 4.1.3 on 2022-11-05 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='Максимальная длина - 255 символов.', max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Описание товара.', null=True, verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Стоимость')),
                ('is_active', models.BooleanField(default=True, help_text='Видимость товара', verbose_name='Активный')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Фотография')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания.')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления.')),
            ],
        ),
    ]