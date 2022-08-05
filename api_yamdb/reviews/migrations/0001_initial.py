# Generated by Django 2.2.16 on 2022-08-05 05:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Категория')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Название категорий',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Ваш комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Комментарий к отзыву',
                'verbose_name_plural': 'Комментарии к отзыву',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Жанр')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='slug жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Название жанров',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Я думаю это ...')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальная оценка - 1'), django.core.validators.MaxValueValidator(10, message='Максимальная оценка - 10')])),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Отзыв о произведении',
                'verbose_name_plural': 'Отзывы о произведении',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название произведения')),
                ('year', models.SmallIntegerField(validators=[reviews.utils.year_of_creation_validator], verbose_name='Год произведения')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(related_name='titles', to='reviews.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Название произведения',
                'verbose_name_plural': 'Название произведений',
            },
        ),
    ]
