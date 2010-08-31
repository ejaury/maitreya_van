# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Class'
        db.create_table('pages_class', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('parent_menu_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['treemenus.MenuItem'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 8, 31, 16, 35, 32, 79768), auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2010, 8, 31, 16, 35, 32, 79816), auto_now=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('pages', ['Class'])

        # Adding M2M table for field categories on 'Class'
        db.create_table('pages_class_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['pages.class'], null=False)),
            ('category', models.ForeignKey(orm['general.category'], null=False))
        ))
        db.create_unique('pages_class_categories', ['class_id', 'category_id'])


    def backwards(self, orm):
        
        # Deleting model 'Class'
        db.delete_table('pages_class')

        # Removing M2M table for field categories on 'Class'
        db.delete_table('pages_class_categories')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'general.category': {
            'Meta': {'object_name': 'Category'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'pages.class': {
            'Meta': {'object_name': 'Class'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['general.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 8, 31, 16, 35, 32, 79768)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 8, 31, 16, 35, 32, 79816)', 'auto_now': 'True', 'blank': 'True'})
        },
        'treemenus.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'root_item': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'is_root_item_of'", 'null': 'True', 'to': "orm['treemenus.MenuItem']"})
        },
        'treemenus.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contained_items'", 'null': 'True', 'to': "orm['treemenus.Menu']"}),
            'named_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['treemenus.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']
