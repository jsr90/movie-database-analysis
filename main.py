#!/usr/bin/ python
# -*- coding: utf-8 -*-

import os
import sys

from exercises.ejercicio_1 import Ejercicio1
from exercises.ejercicio_2 import Ejercicio2
from exercises.ejercicio_3 import Ejercicio3
from exercises.ejercicio_4 import Ejercicio4
from tests.test_1 import Test1
from tests.test_2 import Test2
from tests.test_3 import Test3
from tests.test_4 import Test4


def exercises_loop(exercises_list, word):
    """
    Ejecuta un bucle interactivo que permite seleccionar y ejecutar ejercicios o pruebas específicas.

    Parameters:
    - exercises_list (list): Una lista de clases de ejercicios o pruebas que se pueden ejecutar.
    - word (str): Una cadena que indica el tipo de elemento a ejecutar ('Ejercicio' o 'Test').

    Returns:
        - None
    """
    while True:
        print(f'\n{word.upper()}S')
        print('Elija una opción:')
        print(f'0. Todos los {word.lower()}s')
        for i in range(1, len(exercises_list) + 1):
            print(f'{i}. {word.capitalize()} {i}')
        print("Introduzca cualquier otro valor para salir.")
        opt = input('\nOpción: ')
        if opt == '0':
            for ex in exercises_list:
                ex().run_all()
            break
        else:
            try:
                exercises_list[int(opt) - 1]().run_()
            except IndexError:
                break
            except ValueError:
                break


def delete_files():
    """
    Elimina los archivos especificados en la lista 'files_to_delete'.
    Limpia los archivos descomprimidos al finalizar la ejecución del programa.
    """
    files_to_delete = ['data/TMDB_info.csv',
                       'data/TMDB_distribution.csv', 'data/TMDB_overview.csv']

    for file_path in files_to_delete:
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass


def main(*values):
    """
        Ejecuta ejercicios y pruebas interactivamente según la entrada proporcionada.

        Parameters:
        - *values: Argumentos opcionales para controlar la ejecución de ejercicios y pruebas.
          Puede contener cero, uno o dos valores.
          - Si no se proporcionan, se muestra un menú interactivo para seleccionar entre ejercicios y pruebas.
          - Si se proporciona un argumento, se ejecutan todos los ejercicios o pruebas del tipo seleccionado.
          - Si se proporcionan dos argumentos, se ejecuta un ejercicio o prueba específico según índice.
        """
    exercises = [Ejercicio1, Ejercicio2, Ejercicio3, Ejercicio4]
    tests = [Test1, Test2, Test3, Test4]
    options = [exercises, tests]
    while True:
        try:
            # Imprime error si hay demasiados argumentos
            if len(values) > 2:
                print("Número incorrecto de argumentos")
                break
            # Corre el ejercicio o test concreto si hay dos argumentos
            elif len(values) == 2:
                arg1 = int(values[0]) - 1
                arg2 = int(values[1]) - 1
                exercise = options[arg1][arg2]
                exercise().run_all()
                break
            # Corre todos los ejercicios o tests si hay un argumento
            elif len(values) == 1:
                arg = int(values[0]) - 1
                for exercise in options[arg]:
                    exercise().run_all()
                break
            # Ejecuta el bucle de selección en pantalla
            else:
                print('\nIntroduzca una opción y pulse entrar:')
                print(' 1 - Ejercicios')
                print(' 2 - Tests')
                print("Introduzca cualquier otro valor para salir.")
                choice = input("\nOpción: ")
                if choice == '1':
                    w = 'Ejercicio'
                    exercises_loop(exercises, w)
                elif choice == '2':
                    w = 'Test'
                    exercises_loop(tests, w)
                else:
                    break
        except ValueError:
            break
        except IndexError:
            break


if __name__ == "__main__":
    # Obtener los argumentos de la línea de comandos
    args = sys.argv[1:]

    # Imprime información relevante y las opciones
    print("\nPEC4 - PROGRAMACIÓN PARA LA CIENCIA DE DATOS")
    print("Alumno: Jesús Sánchez Rodríguez")
    print("-" * 50)

    # Bucle principal
    main(*args)

    # Impresión al finalizar el programa
    print('\n' + '-' * 50)
    print('¡Programa terminado con éxito!')
    print('-' * 50)

    # Borrar archivos descomprimidos
    delete_files()
