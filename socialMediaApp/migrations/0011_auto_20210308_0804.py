# Generated by Django 3.1.7 on 2021-03-08 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialMediaApp', '0010_comment_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likepost', to='socialMediaApp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likeuser', to='socialMediaApp.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]