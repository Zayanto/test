# Generated by Django 3.1.4 on 2020-12-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201210_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astrologer',
            name='consultancy_types',
            field=models.CharField(blank=True, choices=[('Astrology', 'Astrology'), ('Numerology', 'Numerology'), ('Palmistry', ' Palmistry'), ('Facereading', 'Facereading'), ('Tarot reading', 'Tarot reading'), ('Feng shui', 'Feng shui'), ('Tarot', 'Tarot'), ('Reiki crystal ', 'Reiki crystal '), ('Pranic healing', 'Pranic healing'), ('Other', 'Other')], default='Other', max_length=100),
        ),
        migrations.AlterField(
            model_name='astrologer',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='astrologers_profile_image'),
        ),
        migrations.AlterField(
            model_name='client',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='clients_profile_image'),
        ),
    ]
