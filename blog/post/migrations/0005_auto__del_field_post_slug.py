# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.slug'
        db.delete_column(u'post_post', 'slug')


    def backwards(self, orm):
        # Adding field 'Post.slug'
        db.add_column(u'post_post', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=40, unique=True),
                      keep_default=False)


    models = {
        u'post.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_content': ('django.db.models.fields.CharField', [], {'max_length': '6000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['post']