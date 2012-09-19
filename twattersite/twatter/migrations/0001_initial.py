# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Twat'
        db.create_table('twatter_twat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('mood', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('twatter', ['Twat'])


    def backwards(self, orm):
        
        # Deleting model 'Twat'
        db.delete_table('twatter_twat')


    models = {
        'twatter.twat': {
            'Meta': {'object_name': 'Twat'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mood': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['twatter']
