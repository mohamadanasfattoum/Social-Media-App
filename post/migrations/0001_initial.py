# Generated by Django 5.0.3 on 2024-03-28 01:15

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
                ('p_type', models.CharField(choices=[('question', 'سؤال'), ('post', 'منشور'), ('article', 'مقالة')], max_length=500, verbose_name='نوع المنشور')),
                ('title', models.CharField(max_length=500, verbose_name='عنوان المنشور')),
            ],
        ),
    ]
