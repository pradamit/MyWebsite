# Generated by Django 3.0.5 on 2020-05-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='first_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user_details',
            name='last_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='address_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='address_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='email_id',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
