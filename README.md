#**VAMOS A CREAR UN DASHBOARD INTERACTIVO USANDO PYTHON DASH**#
---

Dash es un marco de trabajo de código abierto de Python para crear interfaces de visualización de datos.
 Dash está construido sobre Plotly.js, React y Flask. Al usar Dash, no necesitamos HTML, CSS ni ningún archivo de "interfaz" para crear aplicaciones web. 
Todo lo que necesitas es un archivo de Python para procesar y visualizar los datos y configurar el diseño del panel.

##**Una Aplicacion Dash Minimalista**##

Una aplicación de tablero minimalista contiene Layout y Callback . Layout contiene componentes HTML para configurar la vista,
el diseño y el estilo de nuestra aplicación. También podemos usar componentes de arranque adicionales para mejorar el diseño 
y el estilo de nuestra aplicación. Callback se usa para hacer que nuestro tablero sea más interactivo al capturar cada evento 
en el componente de diseño como menú desplegable, radio, control deslizante, etc.

Mostraré cómo crear un panel interactivo con Dash. 
Utilizaré el conjunto de datos de calificaciones de exámenes de estudiantes de Kaggle.

Primero , vamos a instalar todos los paquetes que utilizaremos para crear el dashboard.

* Dash.
* plotly: to create graph figures in our dashboard.
* Pandas: to process the dataset
* dash_bootstrap_components: Para configura el layaout de nuestro dashboard, estilo y usar los componentes 
desde el dash bootstrap en lugar del componente por defecto de dash.


