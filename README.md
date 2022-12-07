# example_automation_web
Ejemplo de automatización para una web usando selenium, implementando tiempos implicitos, separando localizadores de los metodos principales con el fin de ser reutilizados.

## Librerias necesarias
```bash
pip3 install selenium
```

## Ejecución 
Se requiere descargar la versión del driver para Chrome según la versión del navegador que se encuentre ne uso, para descargarlo lo puede realizar desde el siguiente link:
https://chromedriver.chromium.org/downloads.

El driver descargado se debe dejar en la misma ruta del script.

Para ejecutar el Script puede hacerlo mediante la terminal ejecutando:

```bash
python3 -m unittest test.py 
```

## Conclusiones
La web con la que se realiza la prueba tiene un inicio con una carga bastante larga, por lo cual el iniciar la prueba toma hasta 1 minuto, la página no cuenta con localizadores con id's que faciliten la automatización del proceso, por lo cual es necesario implementar otras formas de acceder a estos.
También considero que actualmente existen otros frameworks que optimizan tiempos implicitos como Cypress y que permiten de forma más facíl ejecutarlos en otros navegadores eliminando la dependencia de los WebDrivers.

