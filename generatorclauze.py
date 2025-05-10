import random
import pandas as pd

def generare_clauze(nrclauze, nrlit):
     clauze = []
     for _ in range(nrclauze):
         clauza = set(random.sample(range(-nrlit, nrlit+1), random.randint(3, nrlit//2)))
         clauze.append(clauza)
     return clauze

def salvarecsv(filename, nrclauze, nrlit):
    clauze = generare_clauze(nrclauze, nrlit)
    data = pd.DataFrame({"Clauze":[list(clauza) for clauza in clauze]})
    data.to_csv(f"analysis/test_data/{filename}.csv", index=False)

salvarecsv("clauzemici", 10000, 200)
salvarecsv("clauzemedii", 15000, 500)
salvarecsv("clauzemari", 20000, 1000)

