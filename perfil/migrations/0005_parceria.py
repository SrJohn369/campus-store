# Generated by Django 4.2.7 on 2023-12-08 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_rename_vedendor_produto_vendedor'),
        ('perfil', '0004_delete_parceria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parceria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.vendedor')),
                ('vendedor_parceiro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parceiros', to='cadastro.vendedor')),
            ],
        ),
    ]
