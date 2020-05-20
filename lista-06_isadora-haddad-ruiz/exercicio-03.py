#gráfico de barras horizontal - distribuição população masculina
#função barh (horizontal)

import matplotlib.pyplot as plt
import numpy as np

masc = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664,
                 6320568, 5692014, 4834995, 3902344, 3041035, 2224065, 1667372, 1090517,
                 668623, 310759, 114964, 31529, 7247]

anos = np.arange(4, 105, 5)

if len(masc) == len(anos):
    resp = True
    print('Os conjuntos de dados possuem o mesmo tamanho?\n', resp)

plt.barh(anos, masc, color = 'orange', align = 'center', height = 4)

plt.ylabel('Grupo de idade (anos)', fontsize = 16)
plt.xlabel('População masculina', fontsize = 16)

plt.title('Distribuição da população masculina - Brasil (2010)', fontsize = 20)

plt.yticks([4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104],
           ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
            '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94',
            '95-99', '>100'])

plt.xticks([ 100000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000],
           [ "100 mil", "1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi"])
plt.show()
