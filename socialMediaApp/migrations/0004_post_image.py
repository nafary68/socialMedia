# Generated by Django 3.1.7 on 2021-03-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialMediaApp', '0003_auto_20210326_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]