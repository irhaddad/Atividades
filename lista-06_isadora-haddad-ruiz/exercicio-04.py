#gráﬁco de barras horizontal que mostre a distribuição das populações masculina e feminina lado a lado

import matplotlib.pyplot as plt
import numpy as np

def pir_etaria():
    masc = [-7016987, -7624144, -8725413, -8558868, -8630229, -8460995, -7717658, -6766664,
                     -6320568, -5692014, -4834995, -3902344, -3041035, -2224065, -1667372, -1090517,
                     -668623, -310759, -114964, -31529, -7247]
    fem = [6776171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915,
                    6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930,
                    998349, 508724, 211594, 66806, 16989]

    anos = np.arange(4, 105, 5)

    if len(masc) == len(anos):
        resp = True
        print('Os conjuntos de dados possuem o mesmo tamanho?\n', resp)

    plt.barh(anos, fem, color = 'purple', height = 4, label = r'$Feminino$')
    plt.barh(anos, masc, color = 'orange', height = 4, label = r'$Masculino$')

    plt.yticks([4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104],
               ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94',
                '95-99', '>100'])
    plt.xticks([-7500000, -5000000, -2500000, 0, 2500000, 5000000, 7500000],
               ['7.5 mi', '5 mi', '2.5 mi', '0', '2.5 mi', '5 mi', '7.5 mi'])
    plt.ylabel('Grupo de idade (anos)', fontsize = 16)
    plt.xlabel('População', fontsize = 16)

    plt.legend()

    plt.title('Distribuição da População por sexo segundo os grupos de idade – Brasil – 2010', fontsize= 20)

    return plt.show()

print(pir_etaria())

def pir_etaria2():
    masc = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664,
            6320568, 5692014, 4834995, 3902344, 3041035, 2224065, 1667372, 1090517,
            668623, 310759, 114964, 31529, 7247]
    fem = [6776171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915,
           6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930,
           998349, 508724, 211594, 66806, 16989]

    anos = np.arange(4, 105, 5)

    plt.figure(figsize = (15,8))
    plt.suptitle('Distribuição etária da população por sexo - \n Brasil - 2010', fontsize = 26, fontweight="bold")
    plt.xlabel('População')
    plt.yticks([4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104],
               ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94',
                '95-99', '>100'])

    plt.subplot(1,2,1)
    plt.barh(anos, masc, color = 'blue', linewidth = 1, edgecolor = 'black', height = 4, label = r'$Masculino$')
    plt.yticks([])
    plt.gca().invert_xaxis()
    plt.legend()
    plt.subplots_adjust(wspace=0.15)

    plt.gca().axes.yaxis.set_ticklabels([])

    plt.xticks([9000000, 6750000, 4500000, 2250000, 0],
               ['9 mi', '6.75 mi', '4.5 mi', '2.25 mi', '0'])

    plt.subplot(1,2,2)

    plt.barh(anos, fem, color = 'orange', linewidth = 1, edgecolor = 'black', height = 4, label = r'$Feminino$')
    plt.yticks([4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104],
               ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
            '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94',
            '95-99', '>100'], fontsize = 12)

    plt.xticks([0, 2250000, 4500000, 6750000, 9000000],
               ['0', '2.25 mi', '4.5 mi', '6.75 mi', '9 mi'])

    plt.legend()

    return plt.show()

print(pir_etaria2())
