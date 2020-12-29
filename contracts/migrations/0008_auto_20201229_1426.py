# Generated by Django 3.1.4 on 2020-12-29 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20201229_1235'),
        ('contracts', '0007_auto_20201229_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='dep_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.department'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='emp_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='pos_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.position'),
        ),
    ]
