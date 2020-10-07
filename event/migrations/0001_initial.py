# Generated by Django 3.1 on 2020-10-07 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eviteapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eviteapi.event')),
            ],
        ),
    ]
