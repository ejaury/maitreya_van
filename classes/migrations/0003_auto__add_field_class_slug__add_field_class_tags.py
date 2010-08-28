# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Class.slug'
        db.add_column('classes_class', 'slug', self.gf('django.db.models.fields.SlugField')(default=datetime.date(2010, 8, 27), unique=True, max_length=50, db_index=True), keep_default=False)

        # Adding field 'Class.tags'
        db.add_column('classes_class', 'tags', self.gf('tagging.fields.TagField')(default=datetime.date(2010, 8, 27)), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Class.slug'
        db.delete_column('classes_class', 'slug')

        # Deleting field 'Class.tags'
        db.delete_column('classes_class', 'tags')


    models = {
        'classes.class': {
            'Meta': {'object_name': 'Class'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 8, 27, 19, 42, 29, 391864)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 8, 27, 19, 42, 29, 391920)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classes']
