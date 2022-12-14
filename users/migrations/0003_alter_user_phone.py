# Generated by Django 4.0.6 on 2022-07-27 17:34

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, unique=True, validators=[users.validators.validate_phone], verbose_name='휴대폰 번호'),
        ),
    ]
