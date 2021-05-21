# Generated by Django 3.2.3 on 2021-05-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_moviecomment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(blank=True)),
                ('release_date', models.DateField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
            ],
        ),
    ]
