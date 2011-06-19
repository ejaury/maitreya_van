# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Class.menu_item'
        db.add_column('pages_class', 'menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True), keep_default=False)

        # Adding field 'About.menu_item'
        db.add_column('pages_about', 'menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True), keep_default=False)

        # Adding field 'PastEvent.menu_item'
        db.add_column('pages_pastevent', 'menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True), keep_default=False)

        # Adding field 'Teaching.menu_item'
        db.add_column('pages_teaching', 'menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Class.menu_item'
        db.delete_column('pages_class', 'menu_item_id')

        # Deleting field 'About.menu_item'
        db.delete_column('pages_about', 'menu_item_id')

        # Deleting field 'PastEvent.menu_item'
        db.delete_column('pages_pastevent', 'menu_item_id')

        # Deleting field 'Teaching.menu_item'
        db.delete_column('pages_teaching', 'menu_item_id')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'general.category': {
            'Meta': {'ordering': "['content_type', 'name']", 'object_name': 'Category'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'pages.about': {
            'Meta': {'object_name': 'About'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701505)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701561)', 'auto_now': 'True', 'blank': 'True'})
        },
        'pages.class': {
            'Meta': {'object_name': 'Class'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['general.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701505)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701561)', 'auto_now': 'True', 'blank': 'True'})
        },
        'pages.news': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pages.pastevent': {
            'Meta': {'object_name': 'PastEvent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701505)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701561)', 'auto_now': 'True', 'blank': 'True'})
        },
        'pages.teaching': {
            'Meta': {'object_name': 'Teaching'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['general.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701505)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 18, 17, 48, 27, 701561)', 'auto_now': 'True', 'blank': 'True'})
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
