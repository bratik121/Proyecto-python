# Proyecto-Python-Bryant-Mitchell
- Desarrollado por:
	- [Bryant Mckale Mtichell Cisneros](https://github.com/bratik121)
# Competencias
Una empresa que organiza competiciones le ha contratado a usted para que le desarrolle una
aplicación que le permita analizar los resultados de su última competencia. Ha requerimiento suyo
los datos de la competencia le serán suministrado en un archivo txt, el cual contendrá en cada línea
los datos separados por coma de cada participante.
Para dar cumplimiento al requerimiento, usted va a desarrollar una aplicación que implementará la
siguiente funcionalidad:

- La lógica funcional (reglas de negocio) que permitirán analizar los datos y suministrar los
  resultados
  
- La lógica del modelo de datos (obtenida del archivo txt suministrado)
- El manejo de las excepciones en caso que el usuario coloque un archivo incorrecto de manera de facilitar el desarrollo de la aplicación, a continuación se le indica algunas instrucciones y clases y métodos que le podrían ser de utilidad.

## Funcionalidades del proyecto
El Proyecto debe tener cierta funcionalidad implementada que le permita cumplir con los siguientes requerimientos:
1. Cargar el archivo con los participantes
2. Mostrar la cantidad total de los participantes
3.  Mostrar la lista de los participantes con sus datos (En formato de tabla)
4. Cantidad de participantes por grupo etario (En formato de tabla)
5. Cantidad de participantes por sexo (En formato de tabla)
6. Ganadores por sexo (En formato de tabla)
7. Ganadores por Grupo Etario y sexo (En formato de tabla)
8. Ganador General
9. Historigrama de Participantes por grupo Etario
	- El formato del histograma debe ser el siguiente:
	```
		Junior (x): |****************************************
    	Senior (y): |******************************************************
    	Master (z): |**********************************************
	```	
    Donde `x`, `y` y `z` representan a la cantidad de participantes por grupo etario.

-   Después de presentar cada acción del menú debe existir una opción para retornar al menú principal.
-   La aplicación debe estar activa mientras el usuario no seleccione la opción de salir del menú Archivos
## Requerimientos para la ejecucion del proyecto
A continuacion se listaran los requerimientos tecnicos para poder ejecutar el proyecto de manera exitosa:
- Tener instalada la librería pandas para poder realizar la lectura y escritura del archivo, comando para la instalación:
```pip install panda```
- Tener instalada la librería tabulate para la generación de las tablas, comando para la instalación:
```pip install tabulate```
- En la carpeta "data" que tiene el proyecto se debe encontrar el archivo con todos los participantes, el archivo debe seguir el siguiente formato: 
```
|   CI    | 1er Apellido | 2do Apellido | Nombre | Inicial 2do Nombre | Sexo | Edad | Horas | Minutos | Segundos |
```
## Pasos para la ejecucion del proyecto
Para ejecutar el proyecto de manera correcta se debe:
1. Descargar el proyecto o clonarlo
2. Abrir la terminal en el la raiz del proyecto
3. Ejecutar el comando:
	```python main.py```
----
¡Gracias por utilizar nuestro programa! Esperamos que te haya sido de utilidad. Si tienes algún problema o sugerencia para mejorar el programa, no dudes en abrir un issue en nuestro repositorio de GitHub. ¡Que tengas un excelente día!
