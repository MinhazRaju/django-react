# Generated by Django 4.0.1 on 2022-07-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rating_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
