# Generated by Django 4.1.5 on 2023-01-06 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name='datepublished')),
                ('note', models.TextField(blank=True, max_length=450, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='toDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(verbose_name='datepublished')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('master', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='todolist.list')),
            ],
        ),
    ]
