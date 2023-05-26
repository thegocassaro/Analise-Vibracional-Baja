import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fft import fftfreq
from scipy.fft import fft, ifft, fft2, ifft2
import re

T = 40                              #seconds
N = 100                             #measurements
t = np.linspace(0, T, N)            #cria um vetor linear com espaçamentos iguais de N, de 0 a T
dt = np.diff(t)[0]                  #acha dt


#==============================================================================================#

## Fazendo leitura dos arquivos ##

#   1500 - 2000 - 2500 - 3000 - 3500 - 4000
#
#   data/ASSOALHO/x-ASSOALHO
#   data/CORTA FOGO/x-CORTAFOGO
#   data/MOTOR/x-MOTOR
#   data/PEDAL/x-PEDAL
#   data/VOLANTE/VOLANTE

file_path = 'data/ASSOALHO/1500-ASSOALHO.txt'

with open(file_path, 'r') as file:
    for line in file:
            line = line.strip()

            if line : #checa se linha eh vazia

                time_aux = re.findall(r'[\d]+', line) #ta pegando todos os numeros, quero so o primeiro q aparece

                numbers = re.findall(r'[-]*[\d]*[.][\d]+', line)  #ok, acha todos os floats

                #if (time_aux[2] and time_aux[4] and time_aux[6]) > 1000 #acertar aqui pra quando não gravou o ponto do float


                time = time_aux[0]
                x = numbers[0]
                y = numbers[1]
                z = numbers[2]

                
                # Process the extracted values
                print("Time:", time)
                print("X:", x)
                print("Y:", y)
                print("Z:", z)
            
