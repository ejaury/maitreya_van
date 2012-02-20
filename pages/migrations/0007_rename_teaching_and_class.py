# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Class'
        db.delete_table('pages_class')

        # Removing M2M table for field categories on 'Class'
        db.delete_table('pages_class_categories')

        # Deleting model 'Teaching'
        db.delete_table('pages_teaching')

        # Removing M2M table for field categories on 'Teaching'
        db.delete_table('pages_teaching_categories')

        # Adding model 'Maitreya'
        db.create_table('pages_maitreya', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('parent_menu_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['treemenus.MenuItem'])),
            ('menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 18, 0, 3, 37, 527452), auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 18, 0, 3, 37, 527476), auto_now=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('pages', ['Maitreya'])

        # Adding M2M table for field categories on 'Maitreya'
        db.create_table('pages_maitreya_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('maitreya', models.ForeignKey(orm['pages.maitreya'], null=False)),
            ('category', models.ForeignKey(orm['general.category'], null=False))
        ))
        db.create_unique('pages_maitreya_categories', ['maitreya_id', 'category_id'])

        # Adding model 'Story'
        db.create_table('pages_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('parent_menu_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['treemenus.MenuItem'])),
            ('menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 18, 0, 3, 37, 527452), auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 2, 18, 0, 3, 37, 527476), auto_now=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('pages', ['Story'])

        # Adding M2M table for field categories on 'Story'
        db.create_table('pages_story_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm['pages.story'], null=False)),
            ('category', models.ForeignKey(orm['general.category'], null=False))
        ))
        db.create_unique('pages_story_categories', ['story_id', 'category_id'])


    def backwards(self, orm):
        
        # Adding model 'Class'
        db.create_table('pages_class', (
            ('menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 18, 17, 48, 27, 701561), auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_menu_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['treemenus.MenuItem'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 18, 17, 48, 27, 701505), auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pages', ['Class'])

        # Adding M2M table for field categories on 'Class'
        db.create_table('pages_class_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('class', models.ForeignKey(orm['pages.class'], null=False)),
            ('category', models.ForeignKey(orm['general.category'], null=False))
        ))
        db.create_unique('pages_class_categories', ['class_id', 'category_id'])

        # Adding model 'Teaching'
        db.create_table('pages_teaching', (
            ('menu_item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['treemenus.MenuItem'], unique=True, null=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 18, 17, 48, 27, 701561), auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_menu_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['treemenus.MenuItem'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 18, 17, 48, 27, 701505), auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pages', ['Teaching'])

        # Adding M2M table for field categories on 'Teaching'
        db.create_table('pages_teaching_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teaching', models.ForeignKey(orm['pages.teaching'], null=False)),
            ('category', models.ForeignKey(orm['general.category'], null=False))
        ))
        db.create_unique('pages_teaching_categories', ['teaching_id', 'category_id'])

        # Deleting model 'Maitreya'
        db.delete_table('pages_maitreya')

        # Removing M2M table for field categories on 'Maitreya'
        db.delete_table('pages_maitreya_categories')

        # Deleting model 'Story'
        db.delete_table('pages_story')

        # Removing M2M table for field categories on 'Story'
        db.delete_table('pages_story_categories')


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
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527452)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527476)', 'auto_now': 'True', 'blank': 'True'})
        },
        'pages.maitreya': {
            'Meta': {'object_name': 'Maitreya'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['general.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527452)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527476)', 'auto_now': 'True', 'blank': 'True'})
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
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527452)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527476)', 'auto_now': 'True', 'blank': 'True'})
        },
        'pages.story': {
            'Meta': {'object_name': 'Story'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['general.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527452)', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['treemenus.MenuItem']", 'unique': 'True', 'null': 'True'}),
            'parent_menu_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['treemenus.MenuItem']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 2, 18, 0, 3, 37, 527476)', 'auto_now': 'True', 'blank': 'True'})
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
