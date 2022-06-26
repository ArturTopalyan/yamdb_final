# Generated by Django 2.2.16 on 2022-03-17 13:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('username',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='com_pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата комментария'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='Отзыв'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='text_comment',
            field=models.TextField(default=1, help_text='Введите коментарий на отзыв', verbose_name='Комментарий'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rev_pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата отзыва'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=1, help_text='Поставьте оценку', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Оценка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=1, help_text='Введите отзыв на произведение', verbose_name='Текст отзыва'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Title', verbose_name='Произведение'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=16, verbose_name='Роль'),
        ),
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='titles', to='reviews.Genre'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='username'),
        ),
    ]