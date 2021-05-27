# Generated by Django 3.2 on 2021-05-27 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('reservation', '0001_initial'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.status'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]