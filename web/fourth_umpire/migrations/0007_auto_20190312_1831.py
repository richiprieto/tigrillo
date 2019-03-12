# Generated by Django 2.1.7 on 2019-03-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourth_umpire', '0006_auto_20190312_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='datasets/'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.CharField(choices=[('1', 'Ing. Electrónica'), ('2', 'Med. Veterinaria'), ('3', 'Ing. Eléctrica'), ('4', 'Ing. Sistemas'), ('5', 'Ing. Mecatrónica')], max_length=1),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.CharField(choices=[('1', '1er Ciclo'), ('2', '2do Ciclo'), ('3', '3er Ciclo'), ('4', '4to Ciclo'), ('5', '5to Ciclo'), ('6', '6to Ciclo'), ('7', '7mo Ciclo'), ('8', '8vo Ciclo'), ('9', '9no Ciclo'), ('10', '10mo Ciclo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue',
            field=models.CharField(choices=[('1', 'Cuenca'), ('2', 'Quito'), ('3', 'Guayaquil')], default='1', max_length=1),
        ),
    ]
