# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Class.created_at'
        db.add_column('classes_class', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 7, 22, 13, 31, 47, 621571), auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Class.updated_at'
        db.add_column('classes_class', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 7, 22, 13, 31, 47, 621666), auto_now=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Class.created_at'
        db.delete_column('classes_class', 'created_at')

        # Deleting field 'Class.updated_at'
        db.delete_column('classes_class', 'updated_at')


    models = {
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 22, 13, 31, 47, 621571)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 7, 22, 13, 31, 47, 621666)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classes']
