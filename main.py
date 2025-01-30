# importamos las librerias involucradas en el proyeco

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


from dash import Dash, html,dcc, callback , Output , Input

# load and process the data

df = pd.read_csv('data/data.csv')

avg_math_score =  round(df["MathScore"].mean(),2)
avg_reading_score = round(df["ReadingScore"].mean(),2)
avg_writing_score = round(df["WritingScore"].mean(),2)

# Initialize app

app = Dash(__name__,external_stylesheet=[dbc.themes.BOOTSTRAP])

# Crear Paleta de Colores

color_discrete_sequence= ['#0a9396','#94d2bd','#e9d8a6','#ee9b00', '#ca6702', '#bb3e03', '#ae2012']


# DISPOSICIO  Y CONFIGURACION DEL DISEÑO

app.layout = html.Div([
                       html.H1('Evaluacion de Examenes Estudiantes',style={'textAlign':'center','padding-bottom':'20px'}),
                       dbc.Row([
                            get_card_component('Total de Estudiantes','{:,}'.format(len(df.index))),
                            get_card_component('Promedio Score Matematica',str(avg_math_score)),
                            get_card_component('Promedio Score Ensayo',str(avg_writing_score)),
                            get_card_component('Avg Reading Score',str(avg_reading_score)),
                       ]),
                       dbc.Row(
                           dbc.Col([
                                html.H4("Distribucion de Score"),
                                html.Div(
                                   dbc.RadioItems(
                                       id = "score-distribution-radios",
                                       className="btn-group",
                                       inputClassName = "btn-check",
                                       labelClassName = "btn btn-outline-dark",
                                       labelCheckedClassName = "active",
                                       options = [
                                           {'label':'Score Matematica','valor'.'MathScore'},
                                           {}
                                       ],
 




                                    )
                       


