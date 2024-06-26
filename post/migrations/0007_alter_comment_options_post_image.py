# Generated by Django 5.0.3 on 2024-04-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'التعليق', 'verbose_name_plural': 'التعليقات'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts', verbose_name='الصورة'),
        ),
    ]
