import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fft import fftfreq
from scipy.fft import fft, ifft, fft2, ifft2
import re

#==============================================================================================#

## Fazendo leitura dos arquivos ##

#   1500 - 2000 - 2500 - 3000 - 3500 - 4000
#
#   data/ASSOALHO/x-ASSOALHO
#   data/CORTA FOGO/x-CORTAFOGO
#   data/MOTOR/x-MOTOR
#   data/PEDAL/x-PEDAL
#   data/VOLANTE/VOLANTE



file_path = 'data/ASSOALHO/2000-ASSOALHO.txt'

vetor_time  = []
vetor_x     = []
vetor_y     = []
vetor_z     = []

with open(file_path, 'r') as file:

    next(file)              #pula a primeira linha

    for line in file:

            line = line.strip()

            if line :                                 #checa se linha eh vazia

                time_aux = re.findall(r'[\d]+', line) #ta pegando todos os numeros

                numbers = re.findall(r'[-]*[\d]*[.][\d]+', line)  #ok, acha todos os floats

                if len(numbers) < 3 :
                    numbers.append("0.00000")           #preenche vetor numbers quando não consegue index 3 na leitura com 0 (gambiarra)

                lista_float = [float (i) for i in time_aux] #cria uma lista de floats com os valores str de time_aux


                if len(lista_float) < 7 :                   #verifica os casos que falta ponto no numero float
                                                            #ou que nao possui o primeiro algarismo
                    for i in range(len(lista_float)) : 

                        if lista_float[i] > 1000 :

                            contador = 0
                            
                            while lista_float[i] > 0 :

                                lista_float[i] /= 10

                                contador += 1
                                if contador == 8 : break            #as vezes dava loop infinito (gambiarra)

                            
                            if i == 1 :
                                numbers[0] = lista_float[i]

                            if i == 3 :
                                numbers[1] = lista_float[i]

                            if i == 5 :
                                numbers[2] = lista_float[i]


                time = float(time_aux[0])
                x = float(numbers[0])
                y = float(numbers[1])
                z = float(numbers[2])

                vetor_time.append(time)
                vetor_x.append(x)
                vetor_y.append(y)
                vetor_z.append(z)



    #print("Time:", vetor_time)
    #print("X:", vetor_x)
    #print("Y:", vetor_y)
    #print("Z:", vetor_z)


#==============================================================================================#


def apply_fft(time, x, y, z):
    # Perform FFT on x, y, and z vectors
    x_fft = np.fft.fft(x)
    y_fft = np.fft.fft(y)
    z_fft = np.fft.fft(z)
    
    # Frequency domain
    freq = np.fft.fftfreq(len(time), time[1] - time[0])
    
    return freq, x_fft, y_fft, z_fft

def plot_fft(freq, x_fft, y_fft, z_fft):
    # Plotting x, y, and z FFT results
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(freq, np.abs(x_fft))
    plt.title('FFT of x')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 2)
    plt.plot(freq, np.abs(y_fft))
    plt.title('FFT of y')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    
    plt.subplot(3, 1, 3)
    plt.plot(freq, np.abs(z_fft))
    plt.title('FFT of z')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    
    plt.tight_layout()
    plt.show()



n = len(vetor_time)  # Number of measurements
time = np.linspace(0, 1, n)  # Time vector
x = np.sin(2 * np.pi * time)  
y = np.sin(2 * np.pi * time)  
z = np.sin(2 * np.pi * time)  

freq, x_fft, y_fft, z_fft = apply_fft(vetor_time, vetor_x, vetor_y, vetor_z)
plot_fft(freq, x_fft, y_fft, z_fft)



#==============================================================================================#

'''

T = 30                                              #seconds
N = vetor_time[len(vetor_time) - 1]                 #measurements
t = np.linspace(0, T, N)                            #cria um vetor linear com N espaçamentos iguais(len = N), valores de 0 a T (T/N começando do 0)
dt = np.diff(t)[0]                                  #dt = T/N

f_x = vetor_x/(N*dt)
f_y = vetor_y/(N*dt)
f_z = vetor_z/(N*dt)
print(f_x)

x1 = np.sin(2*np.pi*f_x*t)
x2 = np.sin(2*np.pi*f_y*t)
x3 = np.sin(2*np.pi*f_z*t)

plt.plot(t, x1)
plt.xlabel('$t$ [seconds]', fontsize=20)
plt.ylabel('Signal [arb]')
plt.show()

f = fftfreq(len(t), np.diff(t)[0])
x1_FFT = fft(x1)

plt.plot(f[:N//2], np.abs(x1_FFT[:N//2]))
plt.xlabel('$f_n$ [$s^{-1}$]', fontsize=20)
plt.ylabel('|$\hat{x}_n$|', fontsize=20)
plt.show()



#==============================================================================================#



f_prov = [3, 4, 5, 8, 13, 23, 56, 7, 1, 10]

n_medidas_provisorio = 10

T = 30                                              
N = n_medidas_provisorio                       
t = np.linspace(0, T, N)                #cria um vetor linear com N espaçamentos iguais(len = N), valores de 0 a T (T/N começando do 0)
dt = np.diff(t)[0] 

n = len(t)
fhat = np.fft.fft(f_prov, n)
PSD = fhat * np.conj(fhat) / n
freq = (1 / (dt * n)) * np.arrange(n)
L = np.arrange(1, np.floor(n/2), dtype = 'int')

fig,axs = plt.subplots(2,1)

'''