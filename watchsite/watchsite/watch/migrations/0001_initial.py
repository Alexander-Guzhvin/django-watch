# Generated by Django 4.0.2 on 2022-02-28 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='img/')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='URL')),
                ('price', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watch.category')),
            ],
        ),
    ]
