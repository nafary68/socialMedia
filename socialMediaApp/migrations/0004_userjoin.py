# Generated by Django 3.1.7 on 2021-03-01 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialMediaApp', '0003_auto_20210224_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='socialMediaApp.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='socialMediaApp.user')),
            ],
        ),
    ]