# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.post_content'
        db.alter_column(u'post_post', 'post_content', self.gf('django.db.models.fields.TextField')(max_length=6000))

    def backwards(self, orm):

        # Changing field 'Post.post_content'
        db.alter_column(u'post_post', 'post_content', self.gf('django.db.models.fields.CharField')(max_length=6000))

    models = {
        u'post.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_content': ('django.db.models.fields.TextField', [], {'max_length': '6000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['post']