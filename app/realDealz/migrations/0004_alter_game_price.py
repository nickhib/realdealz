# Generated by Django 4.1.7 on 2023-04-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realDealz', '0003_alter_game_cover_alter_game_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.IntegerField(default='-1'),
        ),
    ]