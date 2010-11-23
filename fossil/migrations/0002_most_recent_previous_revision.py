# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Fossil.is_most_recent'
        db.add_column('fossil_fossil', 'is_most_recent', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True), keep_default=False)

        # Adding field 'Fossil.previous_revision'
        db.add_column('fossil_fossil', 'previous_revision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fossil.Fossil'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Fossil.is_most_recent'
        db.delete_column('fossil_fossil', 'is_most_recent')

        # Deleting field 'Fossil.previous_revision'
        db.delete_column('fossil_fossil', 'previous_revision_id')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fossil.fossil': {
            'Meta': {'object_name': 'Fossil'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_text': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'primary_key': 'True'}),
            'is_most_recent': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {}),
            'previous_revision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fossil.Fossil']", 'null': 'True', 'blank': 'True'}),
            'serialized': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['fossil']
