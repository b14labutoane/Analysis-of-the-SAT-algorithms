from davisputnam import davis_putnam
from resolution import citire_clauze
import time

def propagarea_unitatii(clauze):
    clauze_noi = clauze[:]
    while True:
        clauze_uno = {next(iter(c)) for c in clauze_noi if len(c) == 1}
        if not clauze_uno:
            break
        clauze_temp = []
        modificare = False
        for clauza in clauze_noi:
            if not clauza or any(lit in clauze_uno for lit in clauza):
                modificare = True
                continue
            clauza_filtrata = {lit for lit in clauza if -lit not in clauze_uno}
            if not clauza_filtrata:
                return None
            if clauza_filtrata != clauza:
                modificare = True
            clauze_temp.append(clauza_filtrata)
        if not modificare:
            break
        clauze_noi = clauze_temp
    return clauze_noi

def literal_pur(clauze):
    literali = {}
    for clauza in clauze:
        for lit in clauza:
            if lit in literali:
                literali[lit]+=1
            else:
                literali[lit]=1
    literali_puri = set()
    for lit in literali:
        if -lit not in literali:
            literali_puri.add(lit)

    clauze_reduse = []
    schimbare = False
    for clauza in clauze:
        clauza_filtrata = set(lit for lit in clauza if lit not in literali_puri)
        if clauza_filtrata != clauza:
            schimbare = True
        if clauza_filtrata:
            clauze_reduse.append(clauza_filtrata)

    if schimbare:
        return literal_pur(clauze_reduse)
    return clauze_reduse


def davis_putnam_ll(clauze, asign=None):
    if asign is None:
        asign = set()

    clauze = propagarea_unitatii(clauze)
    if clauze is None:
        return False

    clauze = literal_pur(clauze)
    if not clauze:
        return True

    frecventa_literali = {}
    for clauza in clauze:
        for lit in clauza:
            frecventa_literali[lit] = frecventa_literali.get(lit, 0) + 1
    lit = max(frecventa_literali, key=frecventa_literali.get)

    clauze_noi = [{lit}]
    for clauza in clauze:
        if lit not in clauza and -lit not in clauza:
            clauze_noi.append(clauza)
    if davis_putnam_ll(clauze_noi, asign | {lit}):
        return True

    clauze_noi = [{-lit}]
    for clauza in clauze:
        if lit not in clauza and -lit not in clauza:
            clauze_noi.append(clauza)

    return davis_putnam_ll(clauze_noi, asign | {-lit})