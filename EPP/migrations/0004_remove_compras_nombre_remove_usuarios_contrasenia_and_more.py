# Generated by Django 4.1.7 on 2023-03-02 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EPP', '0003_remove_usuarios_contraseña_usuarios_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='contrasenia',
        ),
        migrations.AddField(
            model_name='compras',
            name='id_compra',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='compras',
            name='monto',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='compras',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='EPP.usuarios'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='contraseña',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EPP.clientes'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='monto',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EPP.productos')),
            ],
            options={
                'db_table': 'Carrito',
            },
        ),
    ]
