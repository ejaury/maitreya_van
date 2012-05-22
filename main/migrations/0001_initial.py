# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Color'
        db.create_table('main_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('hex', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('main', ['Color'])


    def backwards(self, orm):
        # Deleting model 'Color'
        db.delete_table('main_color')


    models = {
        'main.color': {
            'Meta': {'object_name': 'Color'},
            'hex': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['main']