# Generated by Django 2.2.3 on 2019-09-08 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0008_salary_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others',
            name='joining_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='joining_date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_amount', models.IntegerField()),
                ('exp_date', models.DateField()),
                ('exp_description', models.TextField()),
                ('exp_mon', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]