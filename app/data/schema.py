from peewee import *

database = SqliteDatabase('aids.db')

class Patient(Model):
    pidnum = IntegerField(primary_key=True)
    cid = BooleanField()
    time = IntegerField()
    trt = IntegerField()
    age = IntegerField()
    wtkg = FloatField()
    hemo = BooleanField()
    homo = BooleanField()
    drugs = BooleanField()
    karnof = IntegerField()
    oprior = BooleanField()
    z30 = BooleanField()
    zprior = BooleanField()
    preanti = IntegerField()
    race = BooleanField()
    gender = BooleanField()
    str2 = BooleanField()
    strat = IntegerField()
    symptom = BooleanField()
    treat = BooleanField()
    offtrt = BooleanField()
    cd40 = IntegerField()
    cd420 = IntegerField()
    cd80 = IntegerField()
    cd820 = IntegerField()
    class Meta:
        database = database
