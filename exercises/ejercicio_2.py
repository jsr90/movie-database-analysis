#!/usr/bin/ python
# -*- coding: utf-8 -*-


from exercises.base_exercise import BaseExercise
from utils.utils_2 import airtime_duration, get_ordered_dict


class Ejercicio2(BaseExercise):
    def __init__(self):
        """
        Inicializa la clase Ejercicio2.
        """
        super().__init__()
        self.exercises = [
            self.ejercicio_2_1,
            self.ejercicio_2_2
        ]
        self.exercise_order = 2
        self.ordered_dict = None

    def ejercicio_2_1(self):
        """
        Realiza el apartado 1 del ejercicio 2.
        """
        # Cargar el set de datos si no está cargado
        df = self.get_df()

        # Calcular la duración de la serie en días (si no se ha hecho)
        if 'air_days' not in self.df.columns:
            df = self.df
            df['air_days'] = df.apply(airtime_duration, axis=1).astype(int)
            self.df = df

        # Mostrar los registros que más días han estado en emisión
        print("\nRegistros que más días han estado en emisión")
        print(df.sort_values(by='air_days', ascending=False)
              [['id', 'name', 'air_days']].head(10))

    def ejercicio_2_2(self):
        """
        Realiza el apartado 2 del ejercicio 2.
        """
        # Cargar el set de datos si no está cargado
        df = self.get_df()

        # Obtener el diccionario ordenado
        ordered_dic = get_ordered_dict(df) if self.ordered_dict is None else self.ordered_dict
        self.ordered_dict = ordered_dic

        # Mostrar los primeros 5 registros del diccionario
        print("\n5 primeros registros del diccionario ordenado")
        for key, value in list(ordered_dic.items())[:5]:
            print('-', key, ':', value)
