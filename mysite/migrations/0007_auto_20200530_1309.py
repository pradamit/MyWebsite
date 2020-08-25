# Generated by Django 3.0.5 on 2020-05-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20200527_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_posts',
            name='state',
            field=models.CharField(choices=[('draft', 'draft'), ('pending', 'pending'), ('published', 'published'), ('rejected', 'rejected'), ('delete', 'delete')], default='draft', max_length=20),
        ),
    ]
