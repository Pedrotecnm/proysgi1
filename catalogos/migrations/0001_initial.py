# Generated by Django 4.2.2 on 2023-06-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RFC', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apPaterno', models.CharField(max_length=30)),
                ('apMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('CURP', models.CharField(max_length=14)),
                ('calle', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=40)),
                ('CP', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIV', models.CharField(help_text='NIV del vehiculo', max_length=20)),
                ('noMotor', models.CharField(blank=True, max_length=30)),
                ('modelo', models.CharField(max_length=4)),
                ('marca', models.CharField(max_length=40)),
                ('linea', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Placa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('numTC', models.CharField(max_length=20)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estatus', models.BooleanField(default=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.oficina')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.propietario')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.vehiculo')),
            ],
        ),
    ]
