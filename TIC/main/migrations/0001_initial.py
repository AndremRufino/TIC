# Generated by Django 3.2.4 on 2021-06-21 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=7)),
                ('complement', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'login_data',
            },
        ),
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=11)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.address')),
                ('initial_data', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.login')),
            ],
            options={
                'db_table': 'create_user',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.login'),
        ),
    ]
