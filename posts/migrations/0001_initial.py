# Generated by Django 4.0.6 on 2022-07-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('user', models.CharField(max_length=50, verbose_name='유저')),
                ('region', models.CharField(max_length=50, verbose_name='지역')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('content', models.TextField(verbose_name='컨텐츠')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
