# Generated by Django 4.2.7 on 2023-12-07 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_rename_descrição_vendedor_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='vedendor',
            new_name='vendedor',
        ),
    ]

