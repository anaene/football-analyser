import csv
import os

from django.shortcuts import get_object_or_404

from .models import *


def get_association_list(associations):
    temp = str(associations).strip('"')
    return temp.split(',')


def save_confederations():
    with open(os.path.join(os.getcwd(), 'data/confederation.csv'), newline='', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            abb = row['abbreviation']
            name = str(row['name']).strip('"')
            region = row['region']
            con = Confederation(name=name, abbreviation=abb, region=region)

            try:
                con.save()
            except:
                con = get_object_or_404(Confederation, abbreviation=abb)

            associations = row['association_countries']
            association_list = get_association_list(associations)
            for ac in association_list:
                association = Association(name=ac, confederation=con)
                try:
                    association.save()
                except:
                    pass

    f.close()
