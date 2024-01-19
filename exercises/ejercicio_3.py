#!/usr/bin/ python
# -*- coding: utf-8 -*-

from exercises.base_exercise import BaseExercise
from utils.utils_3 import get_filtered_df


class Ejercicio3(BaseExercise):
    def __init__(self):
        """
        Inicializa la clase Ejercicio3.
        """
        super().__init__()
        self.exercises = [
            self.ejercicio_3_1,
            self.ejercicio_3_2,
            self.ejercicio_3_3
        ]
        self.exercise_order = 3
        self.filtered_df = None
        self.filtered_df2 = None
        self.filtered_df3 = None

    def ejercicio_3_1(self):
        """
        Realiza el apartado 1 del ejercicio 3.
        Filtra y muestra nombres de series en inglés que contienen 'mystery' o 'crime'.
        """
        # Cargar el set de datos si no está cargado
        df = self.get_df()

        print("\nNombres de series en inglés que contienen 'mystery' o 'crime':")
        if self.filtered_df is None:
            kwargs = {'original_language': 'en'}
            regex_pattern = '(?i)mystery|crime'
            self.filtered_df = get_filtered_df(df, ('overview', regex_pattern), **kwargs)
        for name in self.filtered_df.name.unique():
            print('-', name)

    def ejercicio_3_2(self):
        """
        Realiza el apartado 2 del ejercicio 3.
        Filtra y muestra 20 series empezadas en 2023 y canceladas.
        """
        # Cargar el set de datos si no está cargado
        df = self.get_df()

        print("\n20 series empezadas en 2023 y canceladas:")
        if self.filtered_df2 is None:
            kwargs = {'status': 'Canceled'}
            self.filtered_df2 = get_filtered_df(df, ('first_air_date', '2023'), **kwargs)
        print(self.filtered_df2.head(20))

    def ejercicio_3_3(self):
        """
        Realiza el apartado 3 del ejercicio 3.
        Filtra y muestra 20 series disponibles en japonés.
        """
        # Cargar el set de datos si no está cargado
        df = self.get_df()

        # Muestra las series en japonés
        print("\n20 series disponibles en japonés:")
        if self.filtered_df3 is None:
            self.filtered_df3 = get_filtered_df(df, ('languages', 'ja'))
        columns = ['name', 'original_name', 'networks', 'production_companies']
        print(self.filtered_df3[columns].head(20))
