#imports necesarios

import json
import os
import shutil
from PERSISTENCIA.db_rutas_connect import *


'''
Dada el id de una ruta, este método devuelve un objeto 
con la información necesaria para realizar la optimización.

1. ID de la ruta.

2. Lista de contenedores de la ruta.

3. Matriz de distancias con los contenedores.
'''

def generateInputData(ruta):
    #1º depUrb, ult->epq
    contenedores=getContsOfRoute(ruta,2020)
    matriz=getDMGraphhopper(contenedores)
    output={}
    output['ruta']=ruta
    output['contenedores']=contenedores
    output['matriz']=matriz
    return output


'''

Para todas las rutas del 2020, genera un archivo con el contenido del método
generateInputData(ruta) que servirá como input para la optimización.

'''
def includeInputFiles():
    for ruta in getRutas2020():
        input_data=generateInputData(ruta)
        with open('input_data/'+ruta+'.json','w') as file:
            json.dump(input_data,file)


'''

Para todas las rutas del 2020, este método genera la estructura de 
directorios que luego se usará para la optimización.
Crea un directorio para cada ejecución para que a él vayan los archivos de 
logs.

En cada uno de estos directotios se copia un archivo de formulación del TSP
modificado en cada caso para tomar el input_data correspondiente., además del 
archivo "sbatch.cmd" que es el encargado de llevar a la cola de slurm la
ejecución.

'''

def generateDirStructure():
    rutas2020=['ENV-RA-INV-SAB-I', 'ENV-RM-VER-SAB-1', 'ENV-RM-VER-MIE', 'ENV-RM-VER-SAB-3', 'ENV-RM-INV-SAB', 'ENV-RB-INV-SAB', 'ENV-RA-VER-MIE', 'ENV-RR-VER-JUE', 'ENV-RM-INV-VIE-I', 'ENV-RB-VER-MAR', 'ENV-RM-VER-LUN', 'ENV-RM-INV-JUE-P', 'ENV-RB-INV-LUN-P', 'ENV-RA-VER-MAR', 'ENV-RB-VER-SAB', 'ENV-RM-INV-MIE-I', 'ENV-RA-VER-VIE', 'ENV-RA-VER-SAB', 'ENV-RM-INV-JUE-I', 'ENV-RA-INV-VIE-P', 'ENV-RA-VER-LUN', 'ENV-RA-INV-JUE-P', 'ENV-RM-INV-VIE-P', 'ENV-RM-INV-MIE-P', 'ENV-RA-INV-VIE-I', 'ENV-RM-INV-MAR', 'ENV-RA-VER-JUE', 'ENV-RB-VER-LUN', 'ENV-RM-INV-SAB-2', 'ENV-RB-INV-MIE-P', 'ENV-RB-VER-VIE', 'ENV-RM-INV-LUN', 'ENV-RM-VER-JUE', 'ENV-RM-VER-VIE', 'ENV-RA-INV-SAB-P', 'ENV-RR-VER-LUN', 'ENV-RA-INV-LUN', 'ENV-RB-INV-VIE', 'ENV-RA-INV-JUE-I', 'ENV-RA-INV-MAR', 'ENV-RB-INV-LUN-I', 'ENV-RB-INV-JUE', 'ENV-RM-VER-MAR', 'ENV-RA-INV-MIE-I', 'ENV-RB-INV-MAR', 'ENV-RB-INV-MIE-I', 'ENV-RR-VER-MIE', 'ENV-RB-VER-JUE', 'ENV-RM-VER-SAB-2', 'ENV-RR-VER-VIE', 'ENV-RB-VER-MIE', 'ENV-RA-INV-MIE-P']

    for ruta in rutas2020:
        exec_path='exec_files/'+ruta
        os.mkdir(exec_path)
        with open('plantilla_formulacion_tsp.py') as file:
            data=str(file.read())
        #print(data)
        data=data.replace('*****',ruta)
        print('*****' in data)
        with open(exec_path+'/tsp.py','w') as file:
            file.write(data)
        file.close()
        shutil.copyfile('sbatch.cmd',exec_path+'/'+ruta+'sbatch.cmd')

