# Generated by Django 4.1.7 on 2023-04-01 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=25, verbose_name='Telegram user ID')),
                ('topic', models.CharField(blank=True, max_length=250, verbose_name='Topic')),
                ('summary', models.CharField(blank=True, max_length=1000, verbose_name='Summary')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last update')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=25, verbose_name='Telegram user ID')),
                ('username', models.CharField(max_length=250, null=True, verbose_name='Username')),
                ('request', models.TextField(max_length=10000, verbose_name='Request')),
                ('response', models.TextField(max_length=10000, verbose_name='Response')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('completion_tokens', models.IntegerField(verbose_name='Completion tokens')),
                ('prompt_tokens', models.IntegerField(verbose_name='Prompt tokens')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='chats.chat', verbose_name='Chat')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
            },
        ),
    ]
