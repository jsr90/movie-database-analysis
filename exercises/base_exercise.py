#!/usr/bin/ python
# -*- coding: utf-8 -*-

from utils.utils_1 import merge_csv_with_pandas, unzip


def execute(exercise_func, exercise_order, i):
    """
    Ejecuta una función y muestra un mensaje.
    """
    print('-'*50)
    print(f"Apartado {exercise_order}.{i}:")
    print('-' * 50)
    exercise_func()
    print(f"\n...apartado {exercise_order}.{i} ejecutado con éxito.\n")


class BaseExercise:
    path_to_zip = 'data/TMDB.zip'
    csv_files = None
    df = None

    def __init__(self):
        """
        Inicializa la clase BaseExercise.
        """
        self.exercises = []
        self.exercise_order = None

    def run_(self):
        """
        Función principal para ejecutar ejercicios según la entrada del usuario.
        """
        while True:
            print('\n', '*' * 50)
            print(f"Ejercicio {self.exercise_order}")
            print("*" * 50)
            print("Elija una opción:")
            print("0 - Todos los apartados")
            for i in range(1, len(self.exercises)+1):
                print(f"{i} - Apartado {self.exercise_order}.{i}")
            print("Introduzca cualquier otro valor para salir.\n")
            option = input("Opción:")
            if option == '0':
                self.run_all()
                break
            else:
                try:
                    execute(self.exercises[int(option) - 1], self.exercise_order, option)
                except IndexError:
                    print("Saliendo...\n")
                    break
                except ValueError:
                    print("Saliendo...\n")
                    break

    def run_all(self):
        """
        Ejecuta todas las funciones de ejercicio.
        """
        print('\n', '*' * 50)
        print(f"Ejercicio {self.exercise_order}")
        print("*" * 50)
        for i, exercise_func in enumerate(self.exercises):
            execute(exercise_func, self.exercise_order, i + 1)

    def set_df(self, df):
        """
        Actualiza el valor del dataframe. Usado para testing.
        """
        self.df = df

    def set_path_to_zip(self, path_to_zip):
        """
        Actualiza la ruta al directorio del archivo zip.
        Usado en testing.
        """
        self.path_to_zip = path_to_zip

    def set_csv_files(self, csv_files):
        """
        Actualiza la lista de archivos csv.
        """
        self.csv_files = csv_files

    def get_csv_files(self):
        """
        Obtiene la lista de archivos CSV. Si no están guardados, los obtiene a través de unzip.

        Returns:
        list: lista de los archivos CSV.
        """
        if self.csv_files is not None:
            return self.csv_files
        else:
            csv_files = unzip(self.path_to_zip)
            self.csv_files = csv_files
            return csv_files

    def get_df(self):
        """
        Devuelve el dataframe. Si no está disponible, lo obtiene y actualiza.
        Returns:
        pandas DataFrame: DataFrame combinado de archivos CSV.
        """
        if self.df is not None:
            return self.df
        else:
            self.csv_files = self.get_csv_files()
            df = merge_csv_with_pandas(self.csv_files)
            self.df = df
            return df
