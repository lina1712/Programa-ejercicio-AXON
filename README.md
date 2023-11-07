# Programa-ejercicio-AXON
Un programa para buscar una señal automática en una lista de señales de un archivo csv

Titulo: Programa ejercicio AXON

Drescripcion: Este codigo busca resolver la busqueda en una archivo csv de señales, en la busqueda se pueden utilizar expresiones regulares, tambien se puede generar una expresion regular para la señal que se desee, como se puede generar una lista de expresiones regulares, para una determinada lista, tambien se puede observar los atributos de cada señal seleccionada en una lista visual cargada desde un archivo csv.

Librerias: 'csv', tkinter','re'

Funciones principales:

Carga del archivo CSV: esta funcion permite cargar un archivo csv, con separacion (;) en la interface, para luego poder visualizar su columna 1 en la interface

Buscar: esta funcion permite buscar por caracteres o expresiones regulares en una lista anidada, para encontrar una detarminada señal (o cadena de texto), luego la visualia en la interface.

Creacion de patrones: en esta funcion se crea una expresion regular (patron) apartir de una cadena con caracteres especiales o en este caso una señal automatica para facilitar su busqueda en una base de datos.

Visualizacion de datos en forma de arbol: En una lista viasualizada, se busca seleccionar un elemento y generar una visualizacion de sus atributos en forma jerarquica, para que el usuario pueda mirar sus caracteristicas

Ejemplos de uso: Puede utilizarse para buscar en una base de datos(lista de señales automaticas, listas de insumos, listas de codigos, etc) que se encuentre en formato csv una frase que contenga caracter especiales o buscar por sus expresiones regulares, acortando el tiempo de busqueda, si el usuario no recuerda exactamente como se llama la linea o cadena que se esta buscando

Notas finales: el codigo aun tiene mucho por mejorar, es apenas un inicio de lo que puede ser un programa de busqueda y creacion de patrones para base de datos. Esperamos seguir co el proyecto
