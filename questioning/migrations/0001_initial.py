# Generated by Django 3.2.7 on 2021-12-13 18:24

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionInterestCatSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionKlimovCatStudyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InterestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категорія')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Категорія')),
                ('name_uk', models.CharField(max_length=50, null=True, verbose_name='Категорія')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Категорія')),
                ('desc', models.TextField(blank=True, verbose_name='Опис категорії')),
                ('desc_en', models.TextField(blank=True, null=True, verbose_name='Опис категорії')),
                ('desc_uk', models.TextField(blank=True, null=True, verbose_name='Опис категорії')),
                ('desc_ru', models.TextField(blank=True, null=True, verbose_name='Опис категорії')),
                ('professions', models.TextField(blank=True, verbose_name='Професії')),
                ('professions_en', models.TextField(blank=True, null=True, verbose_name='Професії')),
                ('professions_uk', models.TextField(blank=True, null=True, verbose_name='Професії')),
                ('professions_ru', models.TextField(blank=True, null=True, verbose_name='Професії')),
            ],
            options={
                'verbose_name': 'Категорія професії',
                'verbose_name_plural': 'Категорії професій',
            },
        ),
        migrations.CreateModel(
            name='KlimovCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Категорія')),
                ('name_en', models.CharField(max_length=20, null=True, verbose_name='Категорія')),
                ('name_uk', models.CharField(max_length=20, null=True, verbose_name='Категорія')),
                ('name_ru', models.CharField(max_length=20, null=True, verbose_name='Категорія')),
                ('desc', models.TextField(blank=True, verbose_name='Опис категорії')),
                ('desc_en', models.TextField(blank=True, null=True, verbose_name='Опис категорії')),
                ('desc_uk', models.TextField(blank=True, null=True, verbose_name='Опис категорії')),
                ('desc_ru', models.TextField(blank=True, null=True, verbose_name='Опис категорії')),
                ('professions', models.TextField(blank=True, verbose_name='Професії')),
                ('professions_en', models.TextField(blank=True, null=True, verbose_name='Професії')),
                ('professions_uk', models.TextField(blank=True, null=True, verbose_name='Професії')),
                ('professions_ru', models.TextField(blank=True, null=True, verbose_name='Професії')),
            ],
            options={
                'verbose_name': 'Категорія професії',
                'verbose_name_plural': 'Категорії професій',
            },
        ),
        migrations.CreateModel(
            name='QuestionsBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='Запитання')),
                ('question_en', models.TextField(blank=True, null=True, verbose_name='Запитання')),
                ('question_uk', models.TextField(blank=True, null=True, verbose_name='Запитання')),
                ('question_ru', models.TextField(blank=True, null=True, verbose_name='Запитання')),
                ('answer', models.TextField(blank=True, verbose_name='Відповіді')),
                ('answer_en', models.TextField(blank=True, null=True, verbose_name='Відповіді')),
                ('answer_uk', models.TextField(blank=True, null=True, verbose_name='Відповіді')),
                ('answer_ru', models.TextField(blank=True, null=True, verbose_name='Відповіді')),
                ('result', models.TextField(null=True, verbose_name='Результат відповідей')),
                ('type', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Запитання',
                'verbose_name_plural': 'Запитання',
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('results', models.CharField(max_length=240, validators=[django.core.validators.int_list_validator])),
                ('type', models.PositiveSmallIntegerField(default=1)),
                ('url', models.CharField(editable=False, max_length=32)),
            ],
        ),
    ]
