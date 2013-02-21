# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LearningResource'
        db.create_table('resource_db_learningresource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=2047)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=511)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_format', self.gf('django.db.models.fields.CharField')(max_length=511, blank=True)),
        ))
        db.send_create_signal('resource_db', ['LearningResource'])


    def backwards(self, orm):
        # Deleting model 'LearningResource'
        db.delete_table('resource_db_learningresource')


    models = {
        'resource_db.learningresource': {
            'Meta': {'object_name': 'LearningResource'},
            'content_format': ('django.db.models.fields.CharField', [], {'max_length': '511', 'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['resource_db']