# Generated by Django 4.1.5 on 2023-01-22 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dialinginapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='brew_time',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dose',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='grind_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dialinginapi.grind'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dialinginapi.method'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='weight',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
