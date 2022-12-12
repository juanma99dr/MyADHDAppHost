# Generated by Django 4.1.3 on 2022-11-26 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_post_downvotes_alter_post_upvotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(help_text='Select a tag for this post', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.forumtag'),
        ),
    ]