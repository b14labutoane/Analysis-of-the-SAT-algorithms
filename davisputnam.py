from resolution import resolution
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

def davis_putnam(clauze):
    while True:
        clauze_uno = set()
        for clauza in clauze:
            if len(clauza)==1:
                clauze_uno.add(next(iter(clauza)))

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

        clauze_noi = []
        mod = False
        for clauza in clauze:
            if any(lit in clauze_uno for lit in clauza):
                mod = True
                continue
            clauza_filtrata = set()
            for lit in clauza:
                if -lit not in clauze_uno and lit not in literali_puri:
                    clauza_filtrata.add(lit)
            if not clauza_filtrata:
                return "Formula NESAT"
            if clauza_filtrata !=clauza:
                mod = True
            clauze_noi.append(clauza_filtrata)
        if not mod:
            break
        clauze = clauze_noi

    return resolution(clauze)

running_example = [
    [1, -2, 3], [-1, 4, -5], [2, 3, -4], [-3, -5, 6],
    [5, -6, 7], [-7, 8, -9], [9, -10, 11], [-11, 12, -13],
    [13, -14, 15], [-15, 16], [16], [-16, 17], [-17, -18],
    [18, 19, -20], [-19, 21, 22], [-21, -22, 23], [22, -23, 24],
    [-24, 25, -26], [26, 27, 28], [-27, -28, 29], [30, 31, -32],
    [-30, -31, 33], [-33, 34, 35], [-34, -35, 36], [37, 38, -39],
    [-37, -38, 40], [-40, 41, -42], [42, -43, 44], [-44, -45, 46],
    [45, -46, 47], [-47, 48, -49], [49, -50, 51], [-50, 52, -53],
    [53, -54, 55], [-55, 56, -57], [57, -58, 59], [-59, -60, 61],
    [60, -61, 62], [-62, -63, 64], [63, -64, 65], [-65, 66, -67],
    [67, -68, 69], [-69, -70, 71], [70, -71, 72], [-72, 73, -74],
    [74, -75, 76], [-76, -77, 78], [77, -78, 79], [-79, 80, -81]
]

beginre = time.time()
dp = davis_putnam(running_example)
endre = time.time()
print(f"Rezultat DP pentru running_example: {dp}, timp de executie: {(endre - beginre):.2f} nanosecunde")