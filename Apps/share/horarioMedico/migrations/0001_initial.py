# Generated by Django 3.2.8 on 2021-10-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='horarioMedico',
            fields=[
                ('id_horario_medico', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
            options={
                'db_table': 'horario_medico',
                'managed': False,
            },
        ),
    ]