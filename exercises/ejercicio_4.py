#!/usr/bin/ python
# -*- coding: utf-8 -*-

import pandas as pd

from exercises.base_exercise import BaseExercise
from utils.utils_4 import get_plot


class Ejercicio4(BaseExercise):
    def __init__(self):
        """
        Inicializa la clase Ejercicio4.
        """
        super().__init__()
        self.exercises = [
            self.ejercicio_4_1,
            self.ejercicio_4_2,
            self.ejercicio_4_3
        ]
        self.exercise_order = 4
        self.prepared_df = None

    def ejercicio_4_1(self):
        """
        Realiza el apartado 1 del ejercicio 4.
        Muestra un gráfico de barras para el recuento de series por primer año de emisión.
        """
        print("\nGráfico de barras para el recuento de series por primer año de emisión")
        # Preparar el dataframe
        if self.prepared_df is None:
            df = self.get_df()

            # Add 'debut_year' and 'decade' columns to the DataFrame
            debut_year = df.first_air_date.str[:4]
            df['debut_year'] = debut_year
            df['decade'] = debut_year.str[:3] + '0\'s'
            self.prepared_df = df

        # Crear un gráfico de barras para mostrar la cantidad de series por año de debut
        get_plot(self.prepared_df, plot_kind='bar', columns=[
            'debut_year'], label_rotation=90, label_step=4, save_path='bar_plot.png')

    def ejercicio_4_2(self):
        """
        Realiza el apartado 2 del ejercicio 4.
        Muestra un gráfico de líneas para el recuento de series por década y tipo.
        """
        print("\nGráfico de líneas para el recuento de series por década y tipo")
        # Crear un gráfico de líneas para mostrar la cantidad de series por década y tipo
        get_plot(self.prepared_df, plot_kind='line', columns=[
            'decade', 'type'], title='Recuento por tipo', save_path='line_plot.png')

    def ejercicio_4_3(self):
        """
        Realiza el apartado 3 del ejercicio 4.
        Muestra un gráfico circular para mostrar la distribución por géneros.
        """
        print("\nGráfico circular para mostrar la distribución por géneros\n")
        # Filtrar y procesar los datos para crear un gráfico de pastel por género
        df_filtered = self.prepared_df.dropna(subset=['genres'])
        series_per_genre = df_filtered.genres.str.split(',').explode().str.strip()
        counts = series_per_genre.value_counts()

        # Establecer un umbral para agrupar géneros menos comunes como 'Other'
        threshold = counts.sum() / 100
        genres = counts.index[counts < threshold]
        genres = {genre: 'Other' for genre in genres}
        series_per_genre.replace(genres, inplace=True)
        series_per_genre = pd.DataFrame(series_per_genre, columns=['genres'])

        # Crear un gráfico circular para mostrar la distribución por géneros
        get_plot(series_per_genre, plot_kind='pie', columns=[
            'genres'], title='Gráfico circular por género', autopct='%1.2f%%', save_path='pie_chart.png')
