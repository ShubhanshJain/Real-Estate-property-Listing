# Generated by Django 5.1.4 on 2025-01-06 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('property_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('amenities', models.JSONField(default=list)),
                ('status', models.CharField(choices=[('available', 'Available'), ('sold', 'Sold')], default='available', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
