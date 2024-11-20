# Encuestas de Consumo de Alcohol

## Índice

1. [Introducción](#introducción)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Descripción del Proyecto](#descripción-del-proyecto)
4. [Características](#características)
    - [Funciones principales](#funciones-principales)
    - [Interfaz gráfica de usuario (GUI)](#interfaz-gráfica-de-usuario-gui)
    - [Exportación de Datos](#exportación-de-datos)
    - [Gráficos y Visualización de Datos](#gráficos-y-visualización-de-datos)
    - [Filtrado de Encuestas](#filtrado-de-encuestas)
5. [Instalación](#instalación)
    - [Requisitos del sistema](#requisitos-del-sistema)
    - [Pasos para instalar](#pasos-para-instalar)
    - [Configurar la base de datos](#configurar-la-base-de-datos)
    - [Configuración del entorno virtual](#configuración-del-entorno-virtual)
    - [Ejecutar la aplicación](#ejecutar-la-aplicación)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [Cómo Contribuir](#cómo-contribuir)
    - [Guía para crear un Pull Request](#guía-para-crear-un-pull-request)
    - [Requisitos para contribuciones](#requisitos-para-contribuciones)
8. [Licencia](#licencia)
9. [Agradecimientos](#agradecimientos)
10. [Soporte y Contacto](#soporte-y-contacto)

## Introducción

Este proyecto es una aplicación de escritorio para gestionar encuestas sobre el consumo de alcohol. El sistema permite ingresar, consultar, modificar, eliminar, y exportar los resultados de las encuestas, todo desde una interfaz gráfica amigable. La aplicación utiliza una base de datos MySQL para almacenar los registros de las encuestas, y se enfoca en ser una herramienta útil para investigadores, profesionales de la salud, y cualquier persona interesada en analizar patrones de consumo de alcohol en diferentes poblaciones.

## Tecnologías Utilizadas

El proyecto está desarrollado en Python, utilizando diversas bibliotecas para crear una aplicación interactiva y potente. A continuación se detallan las tecnologías principales:

- **Python**: Lenguaje de programación principal utilizado para desarrollar la lógica del proyecto.
- **Tkinter**: Biblioteca de Python para crear la interfaz gráfica de usuario (GUI). Tkinter es liviana, fácil de usar y compatible con la mayoría de plataformas.
- **pymysql**: Biblioteca que permite a Python interactuar con bases de datos MySQL, encargada de realizar operaciones CRUD sobre la base de datos.
- **pandas**: Librería para la manipulación y análisis de datos. Utilizada principalmente para exportar los resultados a archivos Excel.
- **matplotlib**: Biblioteca para crear gráficos y visualizaciones en Python. Se usa para representar los datos de consumo en forma de gráficos de barras.
- **MySQL**: Sistema de gestión de bases de datos utilizado para almacenar la información de las encuestas.

## Descripción del Proyecto

El objetivo principal de este proyecto es crear una herramienta que permita a los usuarios realizar encuestas sobre el consumo de alcohol, almacenar los resultados en una base de datos, y analizarlos posteriormente. La aplicación permite realizar tareas como la creación, edición y eliminación de encuestas, y genera gráficos para facilitar el análisis de los datos.

### Objetivos Específicos

1. **Recolección de datos**: Registrar las respuestas a preguntas sobre el consumo de alcohol, la edad, el género y otras características.
2. **Análisis**: Mostrar los datos de manera comprensible a través de tablas y gráficos.
3. **Exportación de datos**: Permitir exportar los resultados a archivos Excel para facilitar el análisis fuera de la aplicación.
4. **Interactividad**: Crear una interfaz gráfica fácil de usar que permita a los usuarios gestionar encuestas sin dificultades.

### Casos de Uso

- **Investigadores en salud pública**: Analizan los patrones de consumo de alcohol en diferentes grupos demográficos.
- **Estudios de comportamiento**: Realizan investigaciones sobre los efectos del consumo de alcohol y las posibles correlaciones con problemas de salud.
- **Educadores**: Usan el sistema como ejemplo de cómo trabajar con bases de datos, gráficos y exportación de datos en Python.

## Características

### Funciones principales

- **Registro de Encuestas**: Permite crear nuevas encuestas introduciendo información del encuestado como edad, sexo, cantidad de alcohol consumido, y otros factores relacionados.
- **Consulta de Encuestas**: Muestra todos los registros en una tabla, permitiendo consultar la información almacenada de manera eficiente.
- **Modificación de Encuestas**: Los usuarios pueden actualizar las respuestas de encuestas ya existentes.
- **Eliminación de Encuestas**: Permite borrar encuestas si ya no son necesarias o si contienen datos incorrectos.

### Interfaz gráfica de usuario (GUI)

La aplicación cuenta con una interfaz gráfica sencilla y bien estructurada:

1. **Formulario de Entrada de Encuesta**: Permite al usuario ingresar nuevos registros con campos claros y fáciles de completar.
2. **Tabla de Encuestas**: Muestra todas las encuestas en una tabla organizada, que se puede ordenar y buscar.
3. **Botones de Acción**: Los usuarios pueden realizar acciones como agregar, modificar o eliminar encuestas con simples clics en botones.
4. **Fácil Navegación**: La interfaz está organizada en pestañas y secciones para mejorar la experiencia del usuario.

### Exportación de Datos

- **Exportar a Excel**: Los usuarios pueden exportar los resultados de las encuestas a archivos Excel, permitiendo una fácil manipulación de los datos en programas como Excel o Google Sheets. Esta función es útil para análisis más avanzados.
- **Formato Personalizado**: Los datos exportados incluyen todos los campos de la encuesta y se ordenan de manera lógica para su interpretación.

### Gráficos y Visualización de Datos

- **Gráficos de Barras**: La aplicación genera gráficos de barras que permiten visualizar el consumo de alcohol según diferentes criterios (por ejemplo, por edad, sexo, tipo de bebida, etc.).
- **Interactividad en Gráficos**: Los usuarios pueden interactuar con los gráficos, obteniendo información detallada sobre cada barra o conjunto de datos.
- **Estadísticas**: Los gráficos no solo muestran los datos de manera visual, sino que también proporcionan estadísticas básicas como el promedio de consumo de alcohol por grupo de edad.

### Filtrado de Encuestas

La aplicación incluye filtros que permiten a los usuarios buscar encuestas específicas basadas en criterios como:

- **Sexo**: Filtrar encuestas por sexo (masculino o femenino).
- **Edad**: Filtrar encuestas por rangos de edad.
- **Consumo de Alcohol**: Filtrar según la cantidad de alcohol consumido.

## Instalación

### Requisitos del sistema

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados en tu máquina:

- **Python 3.x** (recomendado Python 3.7 o superior).
- **MySQL** o **MariaDB** instalado y en funcionamiento.
- Acceso a la terminal o línea de comandos para instalar dependencias.

### Pasos para instalar

1. **Clonar el repositorio**

   Clona este repositorio en tu máquina local con Git:

   ```bash
   git clone https://github.com/tu_usuario/encuestas-alcohol.git
   cd encuestas-alcohol
