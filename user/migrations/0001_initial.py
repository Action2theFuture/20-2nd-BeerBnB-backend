import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('cleanliness', models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True)),
                ('communication', models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True)),
                ('checkin', models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True)),
                ('accuracy', models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True)),
                ('location', models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True)),
                ('cost_effectivenes', models.DecimalField(decimal_places=1, default=None, max_digits=2, null=True)),
                ('review_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_review', to='room.room')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, null=True, unique=True)),
                ('social_id', models.CharField(max_length=128, null=True, unique=True)),
                ('first_name', models.CharField(max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32, null=True)),
                ('password', models.CharField(max_length=128, null=True)),
                ('phone_number', models.CharField(max_length=32, null=True, unique=True)),
                ('birthday', models.CharField(max_length=32, null=True)),
                ('sex', models.CharField(max_length=32, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('profile_url', models.CharField(max_length=2000, null=True)),
                ('is_allowed', models.BooleanField(default=False)),
                ('review', models.ManyToManyField(related_name='user', through='user.Review', to='user.User')),
                ('wishlist', models.ManyToManyField(related_name='user', through='room.WishList', to='room.Room')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='user.user'),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_super', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='user.user')),
            ],
            options={
                'db_table': 'hosts',
            },
        ),
    ]
