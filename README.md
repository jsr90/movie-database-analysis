# PEC4 - Programación para la Ciencia de Datos

## Cabecera

- **Nombre:** Jesús Sánchez Rodríguez
- **Email:** jessanrod3@uoc.edu
- **Licencia:** MIT

## Índice

1. [Introducción](#introducción)
2. [Contenido de la Base de Datos](#contenido-de-la-base-de-datos)
3. [Estructura de Carpetas](#estructura-de-carpetas)
4. [Requisitos Previos](#requisitos-previos)
5. [Ejecución del Programa](#ejecución-del-programa)
   - [Opción sin argumentos](#opción-sin-argumentos)
   - [Opción con argumentos](#opción-con-argumentos)
      - [Un único argumento](#un-único-argumento)
      - [Dos argumentos](#dos-argumentos)
6. [Licencia](#licencia)

## Introducción

El proyecto de Análisis de Contenido TMDB se centra en proporcionar a la Open Broadcast Corporation 
información detallada sobre más de 159,000 programas de televisión contenidos en la base de datos 
*The Movie Database (TMDB)*.

Trabajo realizado durante el curso 2023-2024 en la UOC, en mis estudios de Ingeniería Informática.

## Contenido de la Base de Datos

La información está distribuida en tres ficheros que contienen variables sobre cada serie:

1. **TMDB_info.csv**: Proporciona detalles generales, como el nombre, número de temporadas, idioma original, duración de episodios, fecha de la primera y última emisión, y más.

2. **TMDB_overview.csv**: Contiene información detallada sobre la trama, el eslogan publicitario, y las rutas de imágenes como backdrop y poster de cada serie.

3. **TMDB_distribution.csv**: Ofrece datos sobre géneros, creadores, plataformas de emisión, empresas productoras y países relacionados con cada serie.

Los ficheros se encuentran comprimidos en `data/TMDB.zip`.

## Estructura de Carpetas

La organización del proyecto sigue el siguiente esquema:

```
- activity_4
  - exercises
    - base_exercise.py
    - ejercicio_1.py
    - ejercicio_2.py
    - ejercicio_3.py
    - ejercicio_4.py
  - tests
    - base_test.py
    - test_1.py
    - test_2.py
    - test_3.py
    - test_4.py
  - utils
    - utils_1.py
    - utils_2.py
    - utils_3.py
    - utils_4.py
  - data
    - TMDB.zip
  - main.py
  - requirements.txt
  - Informe_PEC4.pdf
  - README.md
```


El archivo `main.py` contiene la ejecución de los ejercicios y los tests, 
permitiendo la selección individual o en conjunto a través de la línea de comandos. 
Cada carpeta en el proyecto sigue una estructura similar, con archivos etiquetados 
según el número del ejercicio correspondiente (por ejemplo, `ejercicio_1.py`, `test_1.py`, y 
`utils_1.py` corresponden al ejercicio 1). Los ejercicios y tests están implementados
como clases, que heredan de una clase de base. Esta organización facilita la modularidad y evita
la repetición de código, con funciones y métodos compartidos entre subclases y/o a través de `utils`.

El archivo `requirements.txt` incluye las librerías necesarias para el correcto funcionamiento 
del programa junto con sus ejercicios y tests. Por último, `Informe_PEC4.pdf` contiene las conclusiones
de los resultados obtenidos de la ejecución de los ejercicios.

## Requisitos Previos

Para garantizar el correcto funcionamiento del proyecto, se requiere tener instalado Python 3.10 
o una versión superior.

Se recomienda crear un entorno virtual para gestionar las dependencias de manera aislada. 
A continuación, se proporcionan instrucciones sobre cómo crear un entorno virtual utilizando `venv`,
aunque existen otras opciones.

1. Abre una terminal y cambia el directorio a la carpeta principal del proyecto.
2. Ejecuta el siguiente comando para crear un entorno virtual:

    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual (Ubuntu):

    ```bash
    source venv/bin/activate
    ```

4. Instala las dependencias necesarias utilizando el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

En este punto el proyecto ya está listo para ejecutar.

## Ejecución del programa

Se puede ejecutar de dos formas:

### Opción sin argumentos

Para ello solo es necesario ejecutar el siguiente comando:

```bash
python main.py
```

Luego, siga las instrucciones que aparecerán en la interfaz.

### Opción con argumentos

En esta opción se puede pasar argumentos a través de la línea de comandos. El programa acepta uno o dos argumentos.

#### Un único argumento

Se puede utilizar un único argumento para ejecutar todos los ejercicios o todos los tests. Utiliza los siguientes comandos:

Ejecutar todos los ejercicios:

```bash
python main.py 1
```

Ejecutar todos los test:

```bash
python main.py 2
```

#### Dos argumentos

Si se pasan dos argumentos, el programa ejecutará un ejercicio o un test específico. En este caso, se ejecutarán todos 
los subapartados del ejercicio seleccionado. A diferencia del modo sin argumentos, aquí no se pueden ejecutar 
subapartados de forma individual. El primer argumento podrá tomar el valor 1 para ejercicios y 2 para test,
mientras que el segundo será el número del ejercicio o test que se desea lanzar.

Ejemplo para ejecutar el ejercicio 1 al completo:

```bash
python main.py 1 1
```

Ejemplo para ejecutar el test 3:

```bash
python main.py 2 3
```

En caso de seleccionar un ejercicio o test que no existe se mostrará únicamente la cabecera y el *footer*.

```bash
python main.py 6 5
```

Para más información y especificaciones sobre los ejercicios y los tests, puede dirigirse a los 
*docstrings* de las diferentes funciones.

## Cobertura de los tests

De forma adicional, si se desea comprobar la cobertura de los tests se deben seguir los siguientes pasos:

1. Instalar el paquete `coverage`
   ```bash
   pip install coverage
   ```
2. Llevar a cabo el test de cobertura
    ```bash
   coverage run -m unittest tests/test_1.py tests/test_2.py tests/test_3.py tests/test_4.py
    ```
3. Guardar el resultado en formato html
    ```bash
   coverage html
    ```

Una vez ejecutados los comandos se podrá comprobar que se ha creado una carpeta `htmlcov` con un archivo 
`index.html`, con el resumen del test. Para más información sobre su uso, diríjase a la web oficial de 
[coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/).

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](https://opensource.org/license/mit/). Consulta el archivo LICENSE.txt para obtener más detalles.
