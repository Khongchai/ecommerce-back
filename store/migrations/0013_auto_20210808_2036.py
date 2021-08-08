# Generated by Django 3.2.5 on 2021-08-08 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210808_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='composers',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('composers', models.ManyToManyField(related_name='compositions', to='store.Composer')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='store.composition'),
        ),
    ]
