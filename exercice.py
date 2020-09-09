#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    nom_list = nom.split()
    if len(nom_list) == 1:
        return (nom_list[0].lower()).capitalize()
    else:
        for i, mot in enumerate(nom_list):
            if mot.lower() == "and":
                nom_list[i] = mot.lower()
            else :
                nom_list[i] = (mot.lower()).capitalize()
        return " ".join(nom_list)


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
