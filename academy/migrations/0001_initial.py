# Generated by Django 3.2.5 on 2022-12-30 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dater', models.DateTimeField(auto_now_add=True, verbose_name='dater_claim')),
                ('details', models.TextField(verbose_name='claim_details')),
                ('result', models.TextField(blank=True, null=True, verbose_name='result')),
            ],
            options={
                'db_table': 'claim',
                'ordering': ['dater'],
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='group_title')),
                ('details', models.TextField(verbose_name='group_details')),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daten', models.DateTimeField(verbose_name='daten')),
                ('title', models.CharField(max_length=256, verbose_name='title_news')),
                ('details', models.TextField(verbose_name='details_news')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='photo_news')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['daten'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datep', models.DateTimeField(verbose_name='datep')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='amount')),
            ],
            options={
                'db_table': 'payment',
                'ordering': ['datep'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dater', models.DateTimeField(auto_now_add=True, verbose_name='dater_reviews')),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='rating')),
                ('details', models.TextField(verbose_name='details_reviews')),
            ],
            options={
                'db_table': 'reviews',
                'ordering': ['dater'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateTimeField(verbose_name='dates')),
            ],
            options={
                'db_table': 'schedule',
                'ordering': ['dates'],
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64, verbose_name='surname')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('patronymic', models.CharField(blank=True, max_length=64, null=True, verbose_name='patronymic')),
                ('details', models.TextField(verbose_name='details_teachers')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='photo_teachers')),
            ],
            options={
                'db_table': 'teachers',
                'ordering': ['surname', 'name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=196, unique=True, verbose_name='training_title')),
                ('details', models.TextField(verbose_name='training_details')),
            ],
            options={
                'db_table': 'training',
                'ordering': ['title'],
            },
        ),
        migrations.AddIndex(
            model_name='training',
            index=models.Index(fields=['title'], name='training_title_312555_idx'),
        ),
        migrations.AddIndex(
            model_name='teachers',
            index=models.Index(fields=['surname'], name='teachers_surname_36eaa9_idx'),
        ),
        migrations.AddIndex(
            model_name='teachers',
            index=models.Index(fields=['name'], name='teachers_name_13cfbe_idx'),
        ),
        migrations.AddIndex(
            model_name='teachers',
            index=models.Index(fields=['patronymic'], name='teachers_patrony_9556b0_idx'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_groups', to='academy.groups'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['daten'], name='news_daten_a29edb_idx'),
        ),
        migrations.AddField(
            model_name='members',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members_groups', to='academy.groups'),
        ),
        migrations.AddField(
            model_name='members',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='teachers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_teachers', to='academy.teachers'),
        ),
        migrations.AddField(
            model_name='groups',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_training', to='academy.training'),
        ),
        migrations.AddField(
            model_name='claim',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim_training', to='academy.training'),
        ),
        migrations.AddField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='schedule',
            index=models.Index(fields=['dates'], name='schedule_dates_e4c9cc_idx'),
        ),
        migrations.AddIndex(
            model_name='schedule',
            index=models.Index(fields=['groups'], name='schedule_groups__4da881_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('dates', 'groups')},
        ),
        migrations.AddIndex(
            model_name='reviews',
            index=models.Index(fields=['dater'], name='reviews_dater_c1460a_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['datep'], name='payment_datep_7a7c2a_idx'),
        ),
        migrations.AddIndex(
            model_name='members',
            index=models.Index(fields=['groups'], name='members_groups__c2c5cd_idx'),
        ),
        migrations.AddIndex(
            model_name='members',
            index=models.Index(fields=['user'], name='members_user_id_7f6dd9_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='members',
            unique_together={('groups', 'user')},
        ),
        migrations.AddIndex(
            model_name='groups',
            index=models.Index(fields=['training'], name='groups_trainin_b008c9_idx'),
        ),
        migrations.AddIndex(
            model_name='claim',
            index=models.Index(fields=['dater'], name='claim_dater_23c8ed_idx'),
        ),
    ]