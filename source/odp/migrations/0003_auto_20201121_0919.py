# Generated by Django 3.1.2 on 2020-11-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odp', '0002_auto_20201121_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, unique=True)),
                ('group_description', models.CharField(blank=True, max_length=5000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='processcatalogue',
            name='group_id',
            field=models.ManyToManyField(to='odp.ProcessGroup'),
        ),
    ]
