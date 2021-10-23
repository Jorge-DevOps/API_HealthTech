# Generated by Django 3.2.8 on 2021-10-19 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_usuario', models.OneToOneField(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='usuario.usuario')),
            ],
            options={
                'db_table': 'medico',
                'managed': False,
            },
        ),
    ]