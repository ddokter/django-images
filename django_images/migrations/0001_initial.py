# Generated by Django 2.0 on 2019-06-27 15:12

from django.db import migrations, models
import django.db.models.deletion
import django_images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', max_length=255, upload_to=django_images.models.hashed_upload_to, width_field='width')),
                ('height', models.PositiveIntegerField(default=0, editable=False)),
                ('width', models.PositiveIntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', max_length=255, upload_to=django_images.models.hashed_upload_to, width_field='width')),
                ('size', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField(default=0, editable=False)),
                ('width', models.PositiveIntegerField(default=0, editable=False)),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_images.Image')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='thumbnail',
            unique_together={('original', 'size')},
        ),
    ]
