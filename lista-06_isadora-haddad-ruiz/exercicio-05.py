#gráﬁco informativo - dados de interesse
#dados: média anual precipitação por satélite x estações fluviométricas do DAEE
#série temporal: 2001-2017
#satélites: CHIRPS, TRMM e GPM

import matplotlib.pyplot as plt
import numpy as np

ano = np.arange(2001, 2018)
pluv = np.array([74.65, 73.00, 118.7, 140.45, 117.35, 113.9, 104.9, 131.85,
                 187.1, 78.6, 172.1, 107.5, 108.55, 53.8, 99.85, 161.85, 109.4])
chirps = np.array([119.46, 130.15, 137.84, 147.59, 126.20, 132.66, 122.66,
                   139.03, 174.94, 111.93, 122.11, 128.22, 128.19, 103.89,
                   133.98, 134.46, 118.95])
trmm = np.array([113.83, 126.24, 131.59, 162.83, 149.67, 160.12, 128.90,
                 152.93, 191.73, 122.69, 142.32, 128.67, 136.28, 88.47,
                 121.59, 131.20, 109.05])
gpm = np.array([112.52, 117.78, 127.62, 156.94, 140.58, 146.63, 128.04,
                145.55, 188.45, 125.60, 142.24, 130.57, 141.04, 86.35,
                122.39, 126.13, 104.24])

def individual():
    plt.subplot(311)
    plt.plot(ano, chirps, 'blue', label=r"$CHIRPS$")
    plt.plot(ano, pluv, 'grey', linestyle ='--', label=r"$Estação C4001$")
    plt.ylabel('Precipitação média (mm/ano)', fontsize=10)
    plt.xticks([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
                2012, 2013, 2014, 2015, 2016, 2017])
    plt.yticks([60, 80, 100, 120, 140, 160, 180, 200])
    plt.legend()

    plt.subplot(312)
    plt.plot(ano, trmm, 'cyan', label=r"$TRMM$")
    plt.plot(ano, pluv, 'grey', linestyle ='--', label=r"$Estação C4001$")
    plt.ylabel('Precipitação média (mm/ano)', fontsize = 10)
    plt.xticks([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
                2012, 2013, 2014,2015, 2016, 2017])
    plt.yticks([60, 80, 100, 120, 140, 160, 180, 200])
    plt.legend()

    plt.subplot(313)
    plt.plot(ano, gpm, 'olive', label=r"$GPM$")
    plt.plot(ano, pluv, 'grey', linestyle ='--', label=r"$Estação C4001$")
    plt.xlabel('Ano', fontsize = 10)
    plt.ylabel('Precipitação média (mm/ano)', fontsize = 10)
    plt.xticks([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
                2012, 2013, 2014,2015, 2016, 2017])
    plt.yticks([60, 80, 100, 120, 140, 160, 180, 200])
    plt.legend()

    plt.suptitle("Média anual precipitação por satélite (2001-2017)", fontsize=24)

    return plt.show()

print(individual())

def unico():
    ano = np.arange(2001, 2018)
    pluv = np.array([74.65, 73.00, 118.7, 140.45, 117.35, 113.9, 104.9, 131.85,
                     187.1, 78.6, 172.1, 107.5, 108.55, 53.8, 99.85, 161.85, 109.4])
    chirps = np.array([119.46, 130.15, 137.84, 147.59, 126.20, 132.66, 122.66,
                       139.03, 174.94, 111.93, 122.11, 128.22, 128.19, 103.89,
                       133.98, 134.46, 118.95])
    trmm = np.array([113.83, 126.24, 131.59, 162.83, 149.67, 160.12, 128.90,
                     152.93, 191.73, 122.69, 142.32, 128.67, 136.28, 88.47,
                     121.59, 131.20, 109.05])
    gpm = np.array([112.52, 117.78, 127.62, 156.94, 140.58, 146.63, 128.04,
                    145.55, 188.45, 125.60, 142.24, 130.57, 141.04, 86.35,
                    122.39, 126.13, 104.24])

    plt.plot(ano, chirps, 'blue', label=r"$CHIRPS$")
    plt.plot(ano, trmm, 'cyan', label=r"$TRMM$")
    plt.plot(ano, gpm, 'olive', label=r"$GPM$")
    plt.plot(ano, pluv, 'grey', linestyle='--', label=r"$Estação C4001$")
    plt.xlabel('Ano', fontsize=16)
    plt.yticks([60, 80, 100, 120, 140, 160, 180, 200], fontsize=12)
    plt.ylabel('Precipitação média (mm/ano)', fontsize=16)
    plt.xticks([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
                2012, 2013, 2014, 2015, 2016, 2017], fontsize=12)
    plt.legend()

    plt.suptitle("Média anual precipitação por satélite (2001-2017)", fontsize=24)

    return plt.show()

print(unico())

