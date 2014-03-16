# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field tag on 'Post'
        m2m_table_name = db.shorten_name(u'blog_post_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'tag_id'])

        # Deleting field 'Tag.post'
        db.delete_column(u'blog_tag', 'post_id')


    def backwards(self, orm):
        # Removing M2M table for field tag on 'Post'
        db.delete_table(db.shorten_name(u'blog_post_tag'))

        # Adding field 'Tag.post'
        db.add_column(u'blog_tag', 'post',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='tags', to=orm['blog.Post']),
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