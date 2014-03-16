# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.author'
        db.delete_column(u'blog_post', 'author_id')


    def backwards(self, orm):
        # Adding field 'Post.author'
        db.add_column(u'blog_post', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='posts', to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'blog.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {'max_length': '6000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['blog.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']