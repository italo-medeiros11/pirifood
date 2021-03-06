# Generated by Django 2.0.13 on 2019-09-09 22:55

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('piripirifood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='picture01_estabecimento',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='estabelecimentoImagens/'),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='picture02_estabecimento',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='estabelecimentoImagens/'),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='picture03_estabecimento',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='estabelecimentoImagens/'),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='picture04_estabecimento',
            field=models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='estabelecimentoImagens/'),
        ),
    ]
