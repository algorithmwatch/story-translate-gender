from peewee import *
import datetime

db = SqliteDatabase('translations.db')

class Translation(Model):
    concept = CharField()
    source_lang = CharField()
    target_lang = CharField()
    source_gender = CharField()
    original = CharField()
    translation = CharField()
    verified = BooleanField()
    correct = BooleanField()

    class Meta:
        database = db

db.connect()

db.create_tables([Translation], safe = True)