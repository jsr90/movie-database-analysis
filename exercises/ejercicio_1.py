#!/usr/bin/ python
# -*- coding: utf-8 -*-

from exercises.base_exercise import BaseExercise

import os

from utils.utils_1 import (unzip, get_execution_time,
                           merge_csv_with_csv_module, merge_csv_with_pandas)


class Ejercicio1(BaseExercise):
    def __init__(self):
        """
        Inicializa la clase Ejercicio1.
        """
        super().__init__()
        self.exercises = [
            self.ejercicio_1_1,
            self.ejercicio_1_2,
            self.ejercicio_1_3,
            self.ejercicio_1_4,
        ]
        self.dic = None
        self.exercise_order = 1
        self.t1 = 0
        self.t2 = 0

    def ejercicio_1_1(self):
        """
        Realiza el apartado 1 del ejercicio 1.
        Descomprime el archivo y muestra un mensaje.
        """
        self.csv_files = unzip(self.path_to_zip)
        print(
            f"Archivo correctamente descomprimido en ./{os.path.dirname(self.path_to_zip)}/.")

    def ejercicio_1_2(self):
        """
        Realiza el apartado 2 del ejercicio 1.
        Actualiza la variable compartida df y muestra el tiempo de ejecución con Pandas.
        """
        csv_files = self.get_csv_files()
        df, self.t1 = get_execution_time(merge_csv_with_pandas, csv_files)
        self.df = df
        print(
            f"La integración de los ficheros con Pandas ha tardado {self.t1:.4f}s.")

    def ejercicio_1_3(self):
        """
        Realiza el apartado 3 del ejercicio 1.
        Muestra el tiempo de ejecución con el módulo csv.
        """
        csv_files = self.get_csv_files()
        dic, self.t2 = get_execution_time(merge_csv_with_csv_module, csv_files)
        self.dic = dic
        print(
            f"La integración de los ficheros con el módulo csv ha tardado {self.t2:.4f}s.")

    def ejercicio_1_4(self):
        """
        Realiza el apartado 4 del ejercicio 1.
        Muestra la comparación de tiempos entre Pandas y el módulo csv.
        """
        if self.t1 * self.t2 != 0:
            percentage = (self.t1 / self.t2) * 100
            print(f'La integración de los ficheros con la librería Pandas ha sido un {percentage:.2f}% más rápida '
                  'que con el módulo csv.')
        print("Si los archivos son muy grandes, el uso del módulo 'csv' podría ser más eficiente que Pandas.\n"
              "Esto se debe a que 'csv' trabaja con secuencias, permitiendo la lectura incremental sin cargar todo\n"
              "el archivo en memoria, a diferencia de Pandas, que carga los datos en su totalidad y, en caso de\n"
              "limitaciones de memoria, requiere operaciones intermedias.")
