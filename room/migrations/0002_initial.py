<<<<<<< HEAD
# Generated by Django 3.2.3 on 2021-05-31 11:00
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 3.2.3 on 2021-05-31 11:00
=======
# Generated by Django 3.2 on 2021-05-27 04:51
>>>>>>> 6770016... commit
=======
# Generated by Django 3.2 on 2021-05-27 13:24
>>>>>>> cd6ce12... social login
<<<<<<< HEAD
>>>>>>> d5fa9d3... social login
=======
=======
# Generated by Django 3.2.3 on 2021-05-29 13:21
>>>>>>> 666ebdc... auth_email
>>>>>>> b091a65... auth_email

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('user', '0001_initial'),
        ('room', '0001_initial'),
=======
        ('room', '0001_initial'),
        ('user', '0001_initial'),
>>>>>>> 666ebdc... auth_email
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='wish_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_wish', to='user.user'),
        ),
        migrations.AddField(
            model_name='roomamenity',
            name='amenity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.amenity'),
        ),
        migrations.AddField(
            model_name='roomamenity',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room'),
        ),
        migrations.AddField(
            model_name='room',
            name='able_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.abletime'),
        ),
        migrations.AddField(
            model_name='room',
            name='amenity',
            field=models.ManyToManyField(related_name='room', through='room.RoomAmenity', to='room.Amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.category'),
        ),
        migrations.AddField(
            model_name='room',
            name='disable_date',
<<<<<<< HEAD
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.disabledate'),
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.disabledate'),
=======
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.disabledate'),
>>>>>>> 6770016... commit
=======
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.disabledate'),
>>>>>>> cd6ce12... social login
<<<<<<< HEAD
>>>>>>> d5fa9d3... social login
=======
=======
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='room.disabledate'),
>>>>>>> 666ebdc... auth_email
>>>>>>> b091a65... auth_email
        ),
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='user.host'),
        ),
        migrations.AddField(
            model_name='image',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='room.room'),
        ),
    ]
