# Generated by Django 3.2.4 on 2021-07-15 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('qty', models.IntegerField(verbose_name='quantity')),
                ('discount', models.IntegerField(default=0)),
                ('orderdate', models.DateField()),
                ('ordertype', models.CharField(max_length=10)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.products')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
