# Generated by Django 2.2.3 on 2019-08-31 09:08

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
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.Class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('f_Name', models.CharField(max_length=50)),
                ('cnic', models.CharField(max_length=50)),
                ('contact1', models.CharField(max_length=50)),
                ('contact2', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('religion', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('admit_date', models.DateField(auto_now_add=True)),
                ('admit_class', models.CharField(max_length=50)),
                ('current_class', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=50)),
                ('last_school', models.TextField()),
                ('image', models.ImageField(upload_to='pics/')),
                ('age', models.CharField(max_length=50)),
                ('gr', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('c_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='calc.Class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('f_Name', models.CharField(max_length=50)),
                ('cnic', models.CharField(max_length=50)),
                ('contact1', models.CharField(max_length=50)),
                ('contact2', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('religion', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('shift', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics/')),
                ('age', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('education_level', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_code', models.IntegerField()),
                ('account_number', models.CharField(max_length=50)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='calc.Class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='calc.Subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
