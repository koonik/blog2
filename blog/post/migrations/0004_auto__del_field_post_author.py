# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.author'
        db.delete_column(u'post_post', 'author_id')


    def backwards(self, orm):
        # Adding field 'Post.author'
        db.add_column(u'post_post', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['author.User']),
                      keep_default=False)


    models = {
        u'post.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_content': ('django.db.models.fields.CharField', [], {'max_length': '6000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['post']