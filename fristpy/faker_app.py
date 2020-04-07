import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fristpy.settings')

import django
django.setup()

import random

from fristpy_app.models import Topic,webpage,accessrecord

from faker import Faker
fakegen  = Faker()

topics = ['Search','Social','News','Games']

def add_topic():
    t= Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t

def populate (n = 4):

    for entry in range(n):
        top = add_topic()

        faker_url = fakegen.url()
        fake_date  =  fakegen.date()
        fake_name =  fakegen.company()
        webbage = webpage.objects.get_or_create(topic= top,url = faker_url,name = fake_name)[0]
        acc = accessrecord.objects.get_or_create(name=webbage,date=fake_date)[0]



if __name__=='__main__':
    print('POPULATION SCRIPT IS RUNNING')
    populate(20)
    print('---POPULATING IS COMPLET--LS')


