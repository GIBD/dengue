# -*- coding: utf-8 -*-
"""
@author: GIBD
"""

import pandas as pd
import plotly.express as px
import dash

from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import datetime as dt

##external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = 'Dengue GIBD'

server = app.server

colors = {"background": "#111111", "text": "#7FDBFF"}

####DATOS OPS
datosOPS = pd.read_csv("data/dengue_Argentina_OPS_2014_2020.csv")
casosDenguePorAño = datosOPS.iloc[::-1]


###DATOS BOLETINES
casosDengue = pd.read_csv("data/dengue_casos.csv")
casosDengueInvertido = casosDengue.iloc[::-1]

###DATAFRAME CON Pais
denguePaisAut = casosDengueInvertido.groupby(['FechaReporte','Pais'],as_index=False)['Autoctonos'].agg('sum')
denguePaisImp = casosDengueInvertido.groupby(['FechaReporte','Pais'],as_index=False)['Importados'].agg('sum')
denguePaisInv = casosDengueInvertido.groupby(['FechaReporte','Pais'],as_index=False)['Total en Inv'].agg('sum')
denguePaisNotif = casosDengueInvertido.groupby(['FechaReporte','Pais'],as_index=False)['Total notificados para dengue'].agg('sum')
denguePaisFall = casosDengueInvertido.groupby(['FechaReporte','Pais'],as_index=False)['AcumFallecidos'].agg('sum')

  
###DATAFRAME CON REGIONES
dengueRegionesAut = casosDengueInvertido.groupby(['FechaReporte','Region'],as_index=False)['Autoctonos'].agg('sum')
dengueRegionesImp = casosDengueInvertido.groupby(['FechaReporte','Region'],as_index=False)['Importados'].agg('sum')
dengueRegionesInv = casosDengueInvertido.groupby(['FechaReporte','Region'],as_index=False)['Total en Inv'].agg('sum')
dengueRegionesNotif = casosDengueInvertido.groupby(['FechaReporte','Region'],as_index=False)['Total notificados para dengue'].agg('sum')
dengueRegionesFall = casosDengueInvertido.groupby(['FechaReporte','Region'],as_index=False)['AcumFallecidos'].agg('sum')

# Lista de semanas epidemioligicas boletines
#semanaEpidem = dengueProvincias["SE"].tolist()

# GRAFICO 2014-2020 CON DATOS OPS
#dengueOPSConfirmados = casosDenguePorAño.groupby(['Año'])['Confirmados'].max()
#dengueOPSFallecidos = casosDenguePorAño.groupby(['Año'])['Confirmados'].max()

app.layout = html.Div(
    [
        dbc.NavbarSimple(
            children=[
                # dbc.NavItem(dbc.NavLink("Inicio", href="#")),
                # dbc.NavItem(dbc.NavLink("Sudamérica", href="#")),
                # dbc.NavItem(dbc.NavLink("Argentina", href="#")),
                # dbc.NavItem(dbc.NavLink("Entre Ríos", href="#")),
            ],
            brand="Dengue GIBD",
            brand_href="http://www.frcu.utn.edu.ar/gibd",
            color="#000B3B",
            dark=True,
        ),
        dbc.Jumbotron(
            [
            dbc.Row(
                    [
                    dbc.Col(
                            [
                            dbc.Row(
                                    [
                                    html.A(html.Img(src=app.get_asset_url("Logo(Banner).png"),
                                                    style={
                                                    "width": "90px",
                                                    "padding": "10px",
                                                    },
                                                    ),
                                                    href="http://www.frcu.utn.edu.ar/gibd",
                                            ),
                                    html.H1("Grupo de Investigación en Bases de Datos"),
                                    ],
                                    align="center",
                                    ),
                                    html.P("Este proyecto fue creado con el objetivo de compartir información sobre la evolución de casos de Dengue en Argentina.",
                                    className="lead",
                                            ),
                                    html.Hr(className="my-2"),
                                    html.H3("Fuentes de datos"),
                                    html.P(
                                            [
                                            html.Li("Datos históricos: Organización Panamericana de la Salud"
                                                    ),
                                            html.Li("Datos de Argentina: Boletines Integrados de Vigilancia del Ministerio de Salud de la Nación."
                                                    ),
                                            ]
                                            ),
                                    ]
                                    )
                            ]
                    )
                ]
            ),
        dbc.Jumbotron(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H1("Dengue en Argentina"),
                                html.P("Analisis realizado con datos extraidos de los Boletines Integrados de Vigilancia del Ministerio de Salud de la República Argentina",
                                    className="lead",
                                ),
                                html.Hr(className="my-2"),
                                html.P("", className="lead"),
                            ]
                        )
                    ]
                )
            ]
        ),
        dbc.Col(
            [
                html.H2("Dengue en Argentina - Casos por Provincia"),
                html.P(
                    "En esta sección se presentan las visualizaciones correspondientes a la evolución de casos de dengue por provincias. Se visualizan indicadores como la cantidad total de casos notificados, la cantidad total de casos autóctonos confirmados, la incidencia acumulada, la cantidad de casos en investigación y los fallecimientos con diagnóstico de dengue confirmado. "
                ),
            ]
        ),
        dcc.Tabs(
            id="tabsProvincias",
            value="tab-1",
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Casos Autóctonos",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Incidencia Acumulada",
                    value="tab-2",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Casos Importados",
                    value="tab-3",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Notificados",
                    value="tab-5",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Fallecidos",
                    value="tab-6",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
            ],
        ),
        html.Div(id="tabsProv"),
        dbc.Col(
            [
                html.H2("Dengue en Argentina - Casos por Región"),
                html.P(
                    [
                        html.P(
                            "En esta sección se presentan las visualizaciones correspondientes a la evolución de casos de dengue para cada región del país. Se visualizan indicadores como la cantidad total de casos notificados, la cantidad total de casos autóctonos confirmados, la incidencia acumulada, la cantidad de casos en investigación y los fallecimientos con diagnóstico de dengue confirmado."
                        ),
                        html.P("Los distritos integrantes de cada región son:"),
                        html.Li(
                            "Centro: Buenos Aires, CABA, Córdoba, Entre Ríos, Santa Fe."
                        ),
                        html.Li("Cuyo: Mendoza, San Juan, San Luis."),
                        html.Li("NEA: Chaco, Corrientes, Formosa, Misiones."),
                        html.Li(
                            "NOA: Catamarca, Jujuy, La Rioja, Salta, Santiago del Estero, Tucumán."
                        ),
                        html.Li(
                            "SUR: Chubut, La Pampa, Neuquén, Río Negro, Santa Cruz, Tierra del Fuego."
                        ),
                    ]
                ),
            ]
        ),
        dcc.Tabs(
            id="tabsRegiones",
            value="tab-1",
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Casos Autóctonos",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Casos Importados",
                    value="tab-2",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="En Investigación",
                    value="tab-3",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Notificados",
                    value="tab-4",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Fallecidos",
                    value="tab-5",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
            ],
        ),
        html.Div(id="tabsReg"),
        dbc.Col([html.H2("Dengue en Argentina"), html.P("")]),
        dcc.Tabs(
            id="tabsPais",
            value="tab-1",
            parent_className="custom-tabs",
            className="custom-tabs-container",
            children=[
                dcc.Tab(
                    label="Casos Autóctonos",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Casos Importados",
                    value="tab-2",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="En Investigación",
                    value="tab-3",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Notificados",
                    value="tab-4",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Fallecidos",
                    value="tab-5",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
            ],
        ),
        html.Div(id="tabsTotal"),
        dbc.Jumbotron(
            id="jumbo",
            children=[
                html.H1("Dengue en Argentina - Comparativa de casos en los últimos años"),
                html.P(
                    "Analisis realizado con datos obtenidos de la Organización Panamericana de la Salud",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "En lo que va del año 2020 ya se han superado la cantidad total de casos reportados en el año 2016 (41.724) que fue el año con mayor número de casos. En el gráfico se puede ver la evolución comparada con años anteriores.",
                    className="lead",
                ),
            ],
        ),
        dcc.Tabs(id="tabsPaisOPS",
                 value="tab-1",
                 parent_className="custom-tabs",
                 className="custom-tabs-container",
                 children=[
                     dcc.Tab(
                         label="Casos Confirmados",
                         value="tab-1",
                         className="custom-tab",
                         selected_className="custom-tab--selected",
                     ),
                     dcc.Tab(
                         label="Fallecidos",
                         value="tab-2",
                         className="custom-tab",
                         selected_className="custom-tab--selected",
                     ),
                 ],
                 ),
        html.Div(id="tabsTotalOPS"),
    ]
)


@app.callback(Output("tabsProv", "children"), [Input("tabsProvincias", "value")])
def render_content(tab):
    if tab == "tab-1":
        figProvinciasAutoctonos = px.line(casosDengueInvertido,x="FechaReporte",y="Autoctonos",color="Provincia",height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos autóctonos confirmados", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos autoctónos por provincia"),
                        html.P(
                            [
                                html.P(
                                    "Casos autóctonos = casos SAV + casos CAVoP ",
                                    className="lead",
                                ),
                                html.Li(
                                    "Sin Antecedentes de Viaje (SAV): casos de dengue (confirmados por laboratorio o nexo epidemiológico) sin antecedente de viaje."
                                ),
                                html.Li(
                                    "Con Antecedentes de Viaje a Otras Provincias (CAVoP): casos de dengue (confirmados por laboratorio o nexo epidemiológico) con antecedentes de viaje a provincias argentinas."
                                ),
                            ]
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figProvinciasAutoctonos), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-2":
        figProvinciasIA = px.line(casosDengueInvertido, x="FechaReporte", y="IA", color="Provincia", height=650
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Incidencia Acumulada", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Incidencia Acumulada de casos autoctónos confirmados"),
                        html.P(
                            " Incidencia Acumulada (IA) = (cantidad de casos/población)*100.000",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figProvinciasIA), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-3":
        figProvinciasImportados = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="Importados",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos importados confirmados", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos importados por provincia"),
                        html.P(
                            "Caso importado: caso confirmado de dengue Con Antecedentes de Viaje al Exterior (CAVE)",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figProvinciasImportados), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-4":
        figProvinciasEnInv = px.bar(
            casosDengueInvertido,
            x="FechaReporte",
            y="Total en Inv",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos en investigación", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos en investigación por provincia"),
                        html.P("", className="lead"),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figProvinciasEnInv), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-5":
        figProvinciasNotificados = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Provincia",
            height=650,
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos notificados", legend={'traceorder':'normal'})
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos notificados por provincia"),
                        html.P(
                            "Casos notificados: Son casos con sospecha de dengue notificados al Sistema Nacional de Vigilancia de la Salud (SNVS 2.0).",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figProvinciasNotificados), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-6":
        figProvinciasFallecidos = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="AcumFallecidos",
            color="Provincia",
            height=650,
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Fallecidos", legend={'traceorder':'normal'})
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de personas fallecidas por provincia"),
                        html.P(
                            "Fallecimientos: personas fallecidas con confirmación de dengue.",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figProvinciasFallecidos), md=10),
                    ]
                ),
            ]
        )


@app.callback(Output("tabsReg", "children"), [Input("tabsRegiones", "value")])
def render_content(tab):
    if tab == "tab-1":
        figRegionAutoctonos = px.line(dengueRegionesAut, x='FechaReporte',y='Autoctonos',color='Region'
        ).update_layout(xaxis={'tickformat': '%y/%m'},
            xaxis_title="Fecha de Reporte", yaxis_title="Casos autóctonos confirmados",  legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos autoctónos por Region"),
                        html.P(
                            [
                                html.P(
                                    "Casos autóctonos = casos SAV + casos CAVoP ",
                                    className="lead",
                                ),
                                html.Li(
                                    "Sin Antecedentes de Viaje (SAV): casos de dengue (confirmados por laboratorio o nexo epidemiológico) sin antecedente de viaje."
                                ),
                                html.Li(
                                    "Con Antecedentes de Viaje a Otras Provincias (CAVoP): casos de dengue (confirmados por laboratorio o nexo epidemiológico) con antecedentes de viaje a provincias argentinas."
                                ),
                            ]
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figRegionAutoctonos), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-2":
        figRegionImportados = px.line(dengueRegionesImp, x='FechaReporte',y='Importados',color='Region'
        ).update_layout(xaxis={'tickformat': '%y/%m'},
            xaxis_title="Fecha de Reporte", yaxis_title="Casos importados confirmados", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos importados por Region"),
                        html.P(
                            "Caso importado: caso confirmado de dengue Con Antecedentes de Viaje al Exterior (CAVE)",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figRegionImportados), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-3":
        figRegionEnInv = px.bar(dengueRegionesInv, x='FechaReporte',y='Total en Inv',color='Region'
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos en investigación", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos en investigación por Region"),
                        html.P("", className="lead"),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figRegionEnInv), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-4":
        figRegionNotificados = px.line(dengueRegionesNotif, x='FechaReporte',y='Total notificados para dengue',color='Region'
            ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos notificados", legend={'traceorder':'normal'})
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos notificados por Region"),
                        html.P(
                            "Casos notificados: Son casos con sospecha de dengue notificados al Sistema Nacional de Vigilancia de la Salud (SNVS 2.0)",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figRegionNotificados), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-5":
        figRegionFallecidos = px.line(dengueRegionesFall, x='FechaReporte',y='AcumFallecidos',color='Region'
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Fallecidos", legend={'traceorder':'normal'})
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de personas fallecidas por Region"),
                        html.P(
                            "Fallecimientos: personas fallecidas con confirmación de dengue.",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figRegionFallecidos), md=10),
                    ]
                ),
            ]
        )


@app.callback(Output("tabsTotal", "children"), [Input("tabsPais", "value")])
def render_content(tab):
    if tab == "tab-1":
        figPaisAutoctonos = px.line(
            denguePaisAut, x="FechaReporte", y="Autoctonos", color="Pais"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos autóctonos confirmados", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos autoctónos en Argentina en 2020"),
                        html.P(
                            [
                                html.P(
                                    "Casos autóctonos = casos SAV + casos CAVoP ",
                                    className="lead",
                                ),
                                html.Li(
                                    "Sin Antecedentes de Viaje (SAV): casos de dengue (confirmados por laboratorio o nexo epidemiológico) sin antecedente de viaje."
                                ),
                                html.Li(
                                    "Con Antecedentes de Viaje a Otras Provincias (CAVoP): casos de dengue (confirmados por laboratorio o nexo epidemiológico) con antecedentes de viaje a provincias argentinas."
                                ),
                            ]
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figPaisAutoctonos), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-2":
        figPaisImportados = px.line(
            denguePaisImp, x="FechaReporte", y="Importados", color="Pais"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos importados confirmados", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos importados en Argentina en 2020"),
                        html.P(
                            "Caso importado: caso confirmado de dengue Con Antecedentes de Viaje al Exterior (CAVE)",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figPaisImportados), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-3":
        figPaisEnInv = px.bar(
            denguePaisInv, x="FechaReporte", y="Total en Inv", color="Pais"
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos en investigación", legend={'traceorder':'normal'}
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos en investigación en Argentina en 2020"),
                        html.P("", className="lead"),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figPaisEnInv), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-4":
        figPaisNotif = px.line(denguePaisNotif,x="FechaReporte",y="Total notificados para dengue",color="Pais",
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos notificados", legend={'traceorder':'normal'})
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos notificados en Argentina en 2020"),
                        html.P(
                            "Casos notificados: Son casos con sospecha de dengue notificados al Sistema Nacional de Vigilancia de la Salud (SNVS 2.0)",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figPaisNotif), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-5":
        figPaisFall = px.line(denguePaisFall, x="FechaReporte", y="AcumFallecidos", color="Pais"
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Fallecidos", legend={'traceorder':'normal'})
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de personas fallecidas en Argentina en 2020"),
                        html.P(
                            "Fallecimientos: personas fallecidas con confirmación de dengue.",
                            className="lead",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.H4(""), md=1),
                        dbc.Col(dcc.Graph(figure=figPaisFall), md=10),
                    ]
                ),
            ]
        )

@app.callback(Output("tabsTotalOPS", "children"), [Input("tabsPaisOPS", "value")])
def render_content3(tab):
    if tab == "tab-1":
        figOPSConf = px.line(casosDenguePorAño,x="SE", y="Confirmados", color='Año'
                            ).update_layout(
                                            xaxis_title="Semana Epidemiológica",
                                            yaxis_title="Casos confirmados",
                                            )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            "Total de casos Confirmados en Argentina entre los años 2014 y 2020"),
                        dbc.Row(
                            [
                                dbc.Col(html.H4(""), md=1),
                                dbc.Col(dcc.Graph(figure=figOPSConf), md=10),
                            ]
                        )
                    ]
                )
            ]
        )
    elif tab == "tab-2":
        figOPSFall = px.line(casosDenguePorAño,x="SE", y="Muertes",color="Año"
                            ).update_layout(
                                            xaxis_title="Semana Epidemiológica",
                                            yaxis_title="Fallecidos",
                                            )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            "Total de personas fallecidas en Argentina entre los años 2014 y 2020"),
                        dbc.Row(
                            [
                                dbc.Col(html.H4(""), md=1),
                                dbc.Col(dcc.Graph(figure=figOPSFall), md=10),
                            ]
                        )
                    ]
                )
            ]
        )

if __name__ == "__main__":
    app.run_server(debug=True)
