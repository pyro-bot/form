# Generated by Django 2.1.7 on 2019-03-28 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20190320_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Контекст',
                'verbose_name_plural': 'Контексты',
            },
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Context', verbose_name='Контекст')),
            ],
            options={
                'verbose_name': 'Намерение',
                'verbose_name_plural': 'Намерения',
            },
        ),
        migrations.CreateModel(
            name='TrainExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example', models.TextField(verbose_name='Тренеровочный пример')),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Intent', verbose_name='Намерение')),
            ],
            options={
                'verbose_name': 'Тренеровочный пример',
                'verbose_name_plural': 'Тренеровочные примеры',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Cate',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
