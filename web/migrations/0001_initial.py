# Generated by Django 3.2.12 on 2022-05-16 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Nomi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Rasmi')),
                ('is_available', models.BooleanField(default=True)),
                ('printing_required', models.BooleanField(default=False)),
                ('printer', models.CharField(blank=True, max_length=250, null=True, verbose_name='Printer')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ExpenseReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Nomi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Foods/', verbose_name='Rasmi')),
                ('price', models.IntegerField(verbose_name="Narxi (so'm)")),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
            ],
            options={
                'verbose_name': 'Taom',
                'verbose_name_plural': 'Taomlar',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Sanasi')),
                ('order_type', models.CharField(choices=[('table', 'Stol'), ('pickup', 'Olib ketish')], default='table', max_length=25)),
                ('is_completed', models.BooleanField(default=False)),
                ('spent_time', models.IntegerField(default=0)),
                ('waiter_fee', models.IntegerField(default=0)),
                ('place_fee', models.IntegerField(default=0)),
                ('paid_money', models.IntegerField(blank=True, null=True, verbose_name="To'langan summa")),
                ('cash_money', models.IntegerField(default=0)),
                ('credit_card', models.IntegerField(default=0)),
                ('debt_money', models.IntegerField(default=0)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Xona',
                'verbose_name_plural': 'Xonalar',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=25, verbose_name='Familiya')),
                ('position', models.CharField(choices=[('waiter', 'Offitsant'), ('admin', 'Admin')], max_length=20, verbose_name='Lavozim')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Xodim',
                'verbose_name_plural': 'Xodimlar',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Raqami')),
                ('tax_required', models.BooleanField(default=False)),
                ('time_required', models.BooleanField(default=False)),
                ('time_service_cost', models.IntegerField(default=0)),
                ('initial_payment', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.room')),
            ],
            options={
                'verbose_name': 'Stol',
                'verbose_name_plural': 'Stollar',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Soni')),
                ('paid_amount', models.IntegerField(null=True)),
                ('abstract_amount', models.IntegerField(null=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.order')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='web.table', verbose_name='Stol'),
        ),
        migrations.AddField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.worker', verbose_name='Offitsant'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Sanasi')),
                ('amount', models.IntegerField(verbose_name='Sarflangan summa')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.worker')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.expensereason')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
