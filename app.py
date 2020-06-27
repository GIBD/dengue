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
casosDenguePorAño = pd.read_csv("data/dengue_Argentina_OPS_2014_2020.csv")

###DATOS BOLETINES
casosDengue = pd.read_csv("data/dengue_casos.csv")
casosDengueInvertido = casosDengue.iloc[::-1]


dengueProvincias = casosDengueInvertido.loc[
    casosDengueInvertido["Provincia"].isin(
        [
            "Buenos Aires",
            "CABA",
            "Córdoba",
            "Entre Ríos",
            "Santa Fe",
            "Mendoza",
            "San Juan",
            "San Luis",
            "Chaco",
            "Corrientes",
            "Formosa",
            "Misiones",
            "Catamarca",
            "Jujuy",
            "La Rioja",
            "Salta",
            "Santiago del Estero",
            "Tucuman",
            "Chubut",
            "La Pampa",
            "Neuquén",
            "Río Negro",
            "Santa Cruz",
            "Tierra del Fuego",
        ]
    )
]  ###DATAFRAME CON PROVINCIAS

dengueTotalPais = casosDengueInvertido.loc[
    casosDengueInvertido["Provincia"].isin(["Total PAIS"])
]  ###DATAFRAME CON TOTAL

dengueRegiones = casosDengueInvertido.loc[
    casosDengueInvertido["Provincia"].isin(["Centro", "Cuyo", "NEA", "NOA", "Sur"])
]  ###DATAFRAME CON REGIONES

# Lista de semanas epidemioligicas boletines
semanaEpidem = dengueProvincias["SE"].tolist()

# GRAFICO 2014-2020 CON DATOS OPS


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
                                        html.A(
                                            html.Img(
                                                src=app.get_asset_url(
                                                    "Logo(Banner).png"
                                                ),
                                                style={
                                                    "width": "90px",
                                                    "padding": "10px",
                                                },
                                            ),
                                            href="http://www.frcu.utn.edu.ar/gibd",
                                        ),
                                        # html.A(html.Img(src=app.get_asset_url("GIBD(Banner).png"),height="90px"), href='http://www.frcu.utn.edu.ar/gibd'),
                                        html.H1(
                                            "Grupo de Investigación en Bases de Datos"
                                        ),
                                    ],
                                    align="center",
                                ),
                                html.P(
                                    "Este proyecto fue creado con el objetivo de compartir información sobre la evolución de casos de Dengue en Argentina.",
                                    className="lead",
                                ),
                                html.Hr(className="my-2"),
                                html.H2("Fuentes de datos"),
                                html.P(
                                    [
                                        html.Li(
                                            "Los datos históricos son obtenidos de la Organización Panamericana de la Salud"
                                        ),
                                        html.Li(
                                            "Los datos a nivel Nacional son extraídos de los Boletines Integrados de Vigilancia del Ministerio de Salud de la República Argentina."
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
                                html.P(
                                    "Analisis realizado con datos extraidos de los Boletines Integrados de Vigilancia del Ministerio de Salud de la República Argentina",
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
                    label="Incidencia Acumulada",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Casos Autóctonos",
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
                    label="En Investigación",
                    value="tab-4",
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
                html.H1(
                    "Dengue en Argentina - Comparativa de casos en los últimos años"
                ),
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
        dbc.Row(
            [
                dbc.Col(html.P(""), md=1),
                dbc.Col(
                    dcc.Graph(
                        figure=px.line(
                            casosDenguePorAño,
                            x=casosDenguePorAño["SE"],
                            y="Confirmados",
                            color="Año",
                        ).update_layout(
                            xaxis_title="Semana Epidemiológica",
                            yaxis_title="Casos confirmados",
                        )
                    ),
                    md=10,
                ),
            ]
        ),
    ]
)


@app.callback(Output("tabsProv", "children"), [Input("tabsProvincias", "value")])
def render_content(tab):
    if tab == "tab-1":
        figProvinciasIA = px.line(
            dengueProvincias, x="FechaReporte", y="IA", color="Provincia", height=650
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Incidencia Acumulada"
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
    elif tab == "tab-2":
        figProvinciasAutoctonos = px.line(
            dengueProvincias,
            x="FechaReporte",
            y="Autoctonos",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos autóctonos confirmados"
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
    elif tab == "tab-3":
        figProvinciasImportados = px.line(
            dengueProvincias,
            x="FechaReporte",
            y="Importados",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos importados confirmados"
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
        figProvinciasEnInv = px.line(
            dengueProvincias,
            x="FechaReporte",
            y="Total en Inv",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos en investigación"
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
            dengueProvincias,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Provincia",
            height=650,
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos notificados")
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
            dengueProvincias,
            x="FechaReporte",
            y="AcumFallecidos",
            color="Provincia",
            height=650,
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Fallecidos")
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
        figRegionAutoctonos = px.line(
            dengueRegiones, x="FechaReporte", y="Autoctonos", color="Provincia"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos autóctonos confirmados"
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
        figRegionImportados = px.line(
            dengueRegiones, x="FechaReporte", y="Importados", color="Provincia"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos importados confirmados"
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
        figRegionEnInv = px.line(
            dengueRegiones, x="FechaReporte", y="Total en Inv", color="Provincia"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos en investigación"
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
        figRegionNotificados = px.line(
            dengueRegiones,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Provincia",
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos notificados")
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
        figRegionFallecidos = px.line(
            dengueRegiones, x="FechaReporte", y="AcumFallecidos", color="Provincia"
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Fallecidos")
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
            dengueTotalPais, x="FechaReporte", y="Autoctonos", color="Provincia"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos autóctonos confirmados"
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
        figPaisImportadod = px.line(
            dengueTotalPais, x="FechaReporte", y="Importados", color="Provincia"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos importados confirmados"
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
                        dbc.Col(dcc.Graph(figure=figPaisImportadod), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-3":
        figPaisEnInv = px.line(
            dengueTotalPais, x="FechaReporte", y="Total en Inv", color="Provincia"
        ).update_layout(
            xaxis_title="Fecha de Reporte", yaxis_title="Casos en investigación"
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
        figPaisNotificados = px.line(
            dengueTotalPais,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Provincia",
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Casos notificados")
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
                        dbc.Col(dcc.Graph(figure=figPaisNotificados), md=10),
                    ]
                ),
            ]
        )
    elif tab == "tab-5":
        figPaisFallecidos = px.line(
            dengueTotalPais, x="FechaReporte", y="AcumFallecidos", color="Provincia"
        ).update_layout(xaxis_title="Fecha de Reporte", yaxis_title="Fallecidos")
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
                        dbc.Col(dcc.Graph(figure=figPaisFallecidos), md=10),
                    ]
                ),
            ]
        )


if __name__ == "__main__":
    app.run_server(debug=True)
