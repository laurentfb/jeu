#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from lxml import etree
import io
import sys
import itertools as IT
PY2 = sys.version_info[0] == 2
StringIO = io.BytesIO if PY2 else io.StringIO

characters_to_ignore = "&"

def XmlValidate(xml_to_validate, line_number, csv_col_number):
    result = True
    # Test #1 : verification validité xml
    clean_xml_to_validate = ''.join(c for c in xml_to_validate if c not in characters_to_ignore)
    try:
        doc = etree.fromstring("<xml>" + clean_xml_to_validate + "</xml>")
    except etree.ParseError as err:
        print("  - #" + str(line_number) + " Parsing XML Error (formatage xml colonne "+str(csv_col_number)+" : " + err.msg + "\n"+xml_to_validate)
        return False
    except:
        print("  - #" + str(line_number) + " Error (formatage xml colonne "+str(csv_col_number)+" : " + xml_to_validate)
        return False

    # Test #2 : Sur chaque ligne, une seule taille de police
    # Dans chaque paragraphe, on doit avoir une seule dimension (ie une seule section)
    # ie <paragraph><section>sdsdsd</section></paragraph>
    for paragraph in doc.findall('paragraph'):
        if len(paragraph.findall('section')) > 1:
            print("  - #" + str(line_number) + " Erreur une seule section autorisée par paragraphe (colonne "+str(csv_col_number)+")\n"+xml_to_validate)
            result = False
    # Test #3 : pas de puce dans les sections
    # ie sous <section><header> puces interdites
    # Recherche des puces puis de leur parent
    found_puce = [element for element in doc.iter() if element.text is not None and '•' in element.text]
    for contenu_puce in found_puce:
        if contenu_puce.getparent().tag == 'header' or contenu_puce.getparent().tag == 'section':
            print("  - #" + str(line_number) + " Pas de puce en taille non normale (colonne "+str(csv_col_number)+")\n"+contenu_puce.text)
            result = False
    return result

# ------------ MAIN ---------------------
for file in os.listdir("."):
    if file.endswith(".csv"):
        with open(file,"r",encoding="utf8") as fp:
            print("\n* Vérification du fichier : "+file+"\n------------------------------------------------")
            nberrors = 0
            for cpt, line in enumerate(fp):
                tline = str.split(line,"\t")

                # Test avorté à cause des accents (test isascii)
                #for col_content in tline:
                #    if not col_content.isascii():
                #        print("  - #" + str(cpt + 1) + " Erreur chaine avec caractères non ascii)\n" + col_content)
                #        for c in col_content:
                #            if not c.isascii():
                #                print("  - #" + str(cpt+1) + " Caractère non ascii :" + c)
                #        nberrors += 1

                if not XmlValidate(tline[8],cpt+1,8):
                    nberrors += 1
                if not XmlValidate(tline[16], cpt + 1, 16):
                    nberrors += 1
            print("* "+str(cpt+1) + " lignes vérifiées ("+str(nberrors)+" erreur(s))")