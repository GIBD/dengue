# -*- coding: utf-8 -*-
"""
@author: GIBD
"""

from dash_html_components.S import S
from dash_html_components.Strong import Strong
import pandas as pd
import plotly.express as px
import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import datetime as dt

with open("data/info/infoRegiones.md", "r", encoding="utf-8") as input_file:
    infoRegiones = input_file.read()

with open("data/info/infoCasosAutoctonos.md", "r", encoding="utf-8") as input_file:
    infoCasosAutoctonos = input_file.read()

with open("data/info/infoFuenteDeDatos.md", "r", encoding="utf-8") as input_file:
    infoFuentesDeDatos = input_file.read()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dengue GIBD"
server = app.server
colors = {"background": "#111111", "text": "#7FDBFF"}


def generate_table(dataframe, max_rows=24):
    return html.Table(
        [
            html.Thead(html.Tr([html.Th(col) for col in dataframe.columns])),
            html.Tbody(
                [
                    html.Tr(
                        [html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]
                    )
                    for i in range(min(len(dataframe), max_rows))
                ]
            ),
        ]
    )


# Datos históricos OPS
datosOPS = pd.read_csv("data/dengue_Argentina_OPS_2014_2020.csv")
casosDenguePorAño = datosOPS.iloc[::-1]


# Datos actuales BIV
casosDengue = pd.read_csv("data/dengue_casos.csv")
casosDengueInvertido = casosDengue.iloc[::-1]

# País
denguePaisAut = casosDengueInvertido.groupby(["FechaReporte", "Pais"], as_index=False)[
    "Autoctonos"
].agg("sum")
denguePaisImp = casosDengueInvertido.groupby(["FechaReporte", "Pais"], as_index=False)[
    "Importados"
].agg("sum")
denguePaisInv = casosDengueInvertido.groupby(["FechaReporte", "Pais"], as_index=False)[
    "Total en Inv"
].agg("sum")
denguePaisNotif = casosDengueInvertido.groupby(
    ["FechaReporte", "Pais"], as_index=False
)["Total notificados para dengue"].agg("sum")
denguePaisFall = casosDengueInvertido.groupby(["FechaReporte", "Pais"], as_index=False)[
    "AcumFallecidos"
].agg("sum")

# Regiones
dengueRegionesAut = casosDengueInvertido.groupby(
    ["FechaReporte", "Region"], as_index=False
)["Autoctonos"].agg("sum")
dengueRegionesImp = casosDengueInvertido.groupby(
    ["FechaReporte", "Region"], as_index=False
)["Importados"].agg("sum")
dengueRegionesInv = casosDengueInvertido.groupby(
    ["FechaReporte", "Region"], as_index=False
)["Total en Inv"].agg("sum")
dengueRegionesNotif = casosDengueInvertido.groupby(
    ["FechaReporte", "Region"], as_index=False
)["Total notificados para dengue"].agg("sum")
dengueRegionesFall = casosDengueInvertido.groupby(
    ["FechaReporte", "Region"], as_index=False
)["AcumFallecidos"].agg("sum")


app.layout = html.Div(
    [
        # dbc.NavbarSimple(
        #     children=[
        #         # dbc.NavItem(dbc.NavLink("Inicio", href="#")),
        #         # dbc.NavItem(dbc.NavLink("Sudamérica", href="#")),
        #         # dbc.NavItem(dbc.NavLink("Argentina", href="#")),
        #         # dbc.NavItem(dbc.NavLink("Entre Ríos", href="#")),
        #     ],
        #     brand="Dengue GIBD",
        #     brand_href="http://www.frcu.utn.edu.ar/gibd",
        #     color="#000B3B",
        #     dark=True,
        # ),
        html.Header(
            dbc.Jumbotron(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.A(
                                    html.Img(
                                        src=app.get_asset_url("LogoUTN(Banner).png"),
                                        style={"width": "110px"},
                                    ),
                                    href="http://www.frcu.utn.edu.ar",
                                ),
                                className="utn-header",
                            ),
                            dbc.Col(
                                html.A(
                                    html.Img(
                                        src=app.get_asset_url("Logo(Banner).png"),
                                        style={"width": "60px"},
                                    ),
                                    href="http://www.frcu.utn.edu.ar/gibd",
                                ),
                                className="gibd-header",
                                width=1,
                            ),
                            dbc.Col(
                                html.A(
                                    html.Img(
                                        src=app.get_asset_url(
                                            "logo-bombieri-blanco.png"
                                        ),
                                        style={"width": "210px"},
                                    ),
                                    href="https://www.bombieri.com.ar/",
                                ),
                                className="bombieri-header",
                            ),
                        ],
                        className="header-nav",
                    ),
                    dbc.Row(
                        [
                            html.H1(
                                "Grupo de Investigación en Bases de Datos",
                                className="titulo",
                            ),
                            html.H2(
                                "Evolución de casos de Dengue en Argentina",
                                className="lead subtitulo",
                            ),
                            html.Ul(
                                [
                                    html.H3(
                                        "Fuentes de datos",
                                        style={
                                            "font-family": "Roboto",
                                            "font-style": "italic",
                                            "font-weight": "normal",
                                            "font-size": "18px",
                                            "line-height": "25px",
                                        },
                                    ),
                                    html.Li(
                                        [
                                            "Datos históricos: ",
                                            html.Strong(
                                                "Organización Panamericana de la Salud"
                                            ),
                                        ],
                                    ),
                                    html.Li(
                                        [
                                            "Datos de Argentina: ",
                                            html.Strong(
                                                "Boletines Integrados de Vigilancia del Ministerio de Salud de la Nación"
                                            ),
                                        ],
                                    ),
                                ],
                                className="fdatos",
                            ),
                        ]
                    ),
                ]
            ),
            className="header",
        ),
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H2(
                            children=["Casos por Provincia"],
                            style={"textAlign": "center"},
                        ),
                        html.P(
                            "Indicadores presentados: Casos Notificados, Casos Autóctonos confirmados, Incidencia Acumulada (Confirmados c/100.000 habitantes), Casos en Investigación y Fallecimientos por dengue confirmado.",
                            className="card-text",
                        ),
                    ]
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.Tabs(
                                                [
                                                    dbc.Tab(
                                                        label="Casos Autóctonos",
                                                        tab_id="tab-1",
                                                    ),
                                                    dbc.Tab(
                                                        label="Incidencia Acumulada",
                                                        tab_id="tab-2",
                                                    ),
                                                    dbc.Tab(
                                                        label="Casos Importados",
                                                        tab_id="tab-3",
                                                    ),
                                                    dbc.Tab(
                                                        label="Notificados",
                                                        tab_id="tab-5",
                                                    ),
                                                    dbc.Tab(
                                                        label="Fallecidos",
                                                        tab_id="tab-6",
                                                    ),
                                                ],
                                                id="tabsProvincias",
                                                active_tab="tab-1",
                                            ),
                                            html.Div(id="tabsProv"),
                                        ]
                                    ),
                                    width=12,
                                    lg=6,
                                ),
                                dbc.Col(
                                    html.Div(
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    dbc.Tabs(
                                                        [
                                                            dbc.Tab(
                                                                label="Mapa",
                                                                tab_id="tab-1",
                                                            ),
                                                            dbc.Tab(
                                                                label="Tabla",
                                                                tab_id="tab-2",
                                                            ),
                                                        ],
                                                        id="tabsMapa",
                                                        active_tab="tab-1",
                                                    ),
                                                    html.Div(id="tabsMapaYTabla"),
                                                ]
                                            )
                                        )
                                    ),
                                    width=12,
                                    lg=6,
                                ),
                            ],
                            no_gutters=True,
                        ),
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    html.H2(
                                        children=["Casos por Región"],
                                        style={"textAlign": "center"},
                                    ),
                                ),
                                dbc.CardBody(
                                    [
                                        html.H4(
                                            dbc.Button(
                                                "Detalles",
                                                id="collapse-button-info-regiones",
                                                color="link",
                                            )
                                        ),
                                        dbc.Collapse(
                                            id="collapse-info-regiones",
                                            children=[
                                                dcc.Markdown(infoRegiones),
                                            ],
                                        ),
                                        dbc.Tabs(
                                            [
                                                dbc.Tab(
                                                    label="Casos Autóctonos",
                                                    tab_id="tab-1",
                                                ),
                                                dbc.Tab(
                                                    label="Casos Importados",
                                                    tab_id="tab-2",
                                                ),
                                                dbc.Tab(
                                                    label="En Investigación",
                                                    tab_id="tab-3",
                                                ),
                                                dbc.Tab(
                                                    label="Notificados", tab_id="tab-4"
                                                ),
                                                dbc.Tab(
                                                    label="Fallecidos", tab_id="tab-5"
                                                ),
                                            ],
                                            id="tabsRegiones",
                                            active_tab="tab-1",
                                        ),
                                        html.Div(id="tabsReg"),
                                    ]
                                ),
                            ]
                        )
                    ],
                    width=12,
                    lg=6,
                ),
                dbc.Col(
                    [
                        dbc.CardHeader(
                            html.H2(
                                children=["Casos en todo el País"],
                                style={"textAlign": "center"},
                            )
                        ),
                        dbc.CardBody(
                            [
                                dbc.Tabs(
                                    [
                                        dbc.Tab(
                                            label="Casos Autóctonos", tab_id="tab-1"
                                        ),
                                        dbc.Tab(
                                            label="Casos Importados", tab_id="tab-2"
                                        ),
                                        dbc.Tab(
                                            label="En Investigación", tab_id="tab-3"
                                        ),
                                        dbc.Tab(label="Notificados", tab_id="tab-4"),
                                        dbc.Tab(label="Fallecidos", tab_id="tab-5"),
                                    ],
                                    id="tabsPais",
                                    active_tab="tab-1",
                                ),
                                html.Div(id="tabsTotal"),
                            ]
                        ),
                    ],
                    width=12,
                    lg=6,
                ),
            ],
            no_gutters=True,
        ),
        dbc.Card(
            [
                dbc.CardHeader(
                    children=[html.H2("Comparativa 2014-2020")],
                    style={"textAlign": "center"},
                ),
                dbc.Row(
                    children=[
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H4(
                                        children=["Casos confirmados"],
                                        style={"padding": "10px"},
                                    ),
                                    dcc.Graph(
                                        figure=px.line(
                                            casosDenguePorAño,
                                            x="SE",
                                            y="Confirmados",
                                            color="Año",
                                        ).update_layout(
                                            xaxis_title="Semana Epidemiológica",
                                            yaxis_title="Casos confirmados",
                                        )
                                    ),
                                ]
                            ),
                            width=12,
                            lg=6,
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H4(
                                        children=["Fallecimientos"],
                                        style={"padding": "10px"},
                                    ),
                                    dcc.Graph(
                                        figure=px.line(
                                            casosDenguePorAño,
                                            x="SE",
                                            y="Muertes",
                                            color="Año",
                                        ).update_layout(
                                            xaxis_title="Semana Epidemiológica",
                                            yaxis_title="Fallecidos",
                                        )
                                    ),
                                ]
                            ),
                            width=12,
                            lg=6,
                        ),
                    ],
                    style={"textAlign": "center"},
                    no_gutters=True,
                ),
            ],
        ),
        dbc.CardFooter(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.P(
                                [
                                    "Realizado por el ",
                                    html.Strong(
                                        "Grupo de Investigación en Bases de Datos de UTN FRCU"
                                    ),
                                    " y la empresa de innovación digital ",
                                    html.Strong("Bombieri."),
                                ],
                                className="footer-text",
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            [
                                dbc.Col(
                                    html.A(
                                        html.Img(
                                            src=app.get_asset_url(
                                                "LogoUTN(Banner).png"
                                            ),
                                            style={"width": "130px"},
                                        ),
                                        href="http://www.frcu.utn.edu.ar",
                                    ),
                                    className="utn-footer",
                                    width=4,
                                ),
                                dbc.Col(
                                    html.A(
                                        html.Img(
                                            src=app.get_asset_url("Logo(Banner).png"),
                                            style={"width": "70px"},
                                        ),
                                        href="http://www.frcu.utn.edu.ar/gibd",
                                    ),
                                    className="gibd-footer",
                                    width=4,
                                ),
                                dbc.Col(
                                    html.A(
                                        html.Img(
                                            src=app.get_asset_url(
                                                "logo-bombieri-blanco.png"
                                            ),
                                            style={"width": "260px"},
                                        ),
                                        href="https://www.bombieri.com.ar/",
                                    ),
                                    className="bombieri-footer",
                                    width=4,
                                ),
                            ],
                            width=6,
                            className="footer-logos",
                        ),
                    ]
                )
            ],
            className="footer",
        ),
    ]
)


# permite llamar un callback desde otro callback
app.config["suppress_callback_exceptions"] = True


@app.callback(
    Output("collapse-provincias", "is_open"),
    [Input("collapse-button-provincias", "n_clicks")],
    [State("collapse-provincias", "is_open")],
)
def toggle_collapse_provincias(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse-regiones", "is_open"),
    [Input("collapse-button-regiones", "n_clicks")],
    [State("collapse-regiones", "is_open")],
)
def toggle_collapse_regiones(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse-pais", "is_open"),
    [Input("collapse-button-pais", "n_clicks")],
    [State("collapse-pais", "is_open")],
)
def toggle_collapse_pais(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse-info-regiones", "is_open"),
    [Input("collapse-button-info-regiones", "n_clicks")],
    [State("collapse-info-regiones", "is_open")],
)
def toggle_collapse_info_regiones(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output("tabsProv", "children"), [Input("tabsProvincias", "active_tab")])
def tab_provincias(tab):
    if tab == "tab-1":
        figProvinciasAutoctonos = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="Autoctonos",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos autóctonos confirmados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos autoctónos por provincia",
                                id="collapse-button-provincias",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-provincias",
                            children=[dcc.Markdown(infoCasosAutoctonos)],
                        ),
                    ]
                ),
                dcc.Graph(figure=figProvinciasAutoctonos),
            ]
        )
    elif tab == "tab-2":
        figProvinciasIA = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="IA",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Incidencia Acumulada",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Incidencia Acumulada de casos autoctónos confirmados",
                                id="collapse-button-provincias",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-provincias",
                            children=[
                                html.P(
                                    "Incidencia Acumulada (IA) = (cantidad de casos/población)*100.000",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figProvinciasIA),
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
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos importados confirmados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos importados por provincia",
                                id="collapse-button-provincias",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-provincias",
                            children=[
                                html.P(
                                    "Caso importado: caso confirmado de dengue Con Antecedentes de Viaje al Exterior (CAVE)",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figProvinciasImportados),
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
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos en investigación",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos en investigación por provincia"),
                        html.P("", className="lead"),
                    ]
                ),
                dcc.Graph(figure=figProvinciasEnInv),
            ]
        )
    elif tab == "tab-5":
        figProvinciasNotificados = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos notificados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos notificados por provincia",
                                id="collapse-button-provincias",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-provincias",
                            children=[
                                html.P(
                                    "Casos notificados: Son casos con sospecha de dengue notificados al Sistema Nacional de Vigilancia de la Salud (SNVS 2.0).",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figProvinciasNotificados),
            ]
        )
    elif tab == "tab-6":
        figProvinciasFallecidos = px.line(
            casosDengueInvertido,
            x="FechaReporte",
            y="AcumFallecidos",
            color="Provincia",
            height=650,
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Fallecidos",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de personas fallecidas por provincia",
                                id="collapse-button-provincias",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-provincias",
                            children=[
                                html.P(
                                    "Fallecimientos: personas fallecidas con confirmación de dengue.",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figProvinciasFallecidos),
            ]
        )


@app.callback(Output("tabsMapaYTabla", "children"), [Input("tabsMapa", "active_tab")])
def tab_mapa_y_tabla(tab):
    if tab == "tab-1":
        maximaSE = casosDengue["SE"].max()
        df = casosDengue[casosDengue["SE"] == maximaSE]
        fig = px.scatter_mapbox(
            df,
            lat="lat",
            lon="lon",
            color="Autoctonos",
            size="Autoctonos",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=3,
            mapbox_style="carto-positron",
            height=650,
            text="Provincia",
        )

        return html.Div(
            [
                dbc.Container(
                    children=[
                        html.H4(
                            children=["Casos autóctonos por provincia"],
                            style={"padding": "10px"},
                        )
                    ],
                    style={"textAlign": "center"},
                ),
                dcc.Graph(figure=fig),
            ]
        )
    elif tab == "tab-2":
        maximaSE = casosDengue["SE"].max()
        ultimaFecha = casosDengue["FechaReporte"].max()
        casosSemanaSeleccionada = casosDengue[casosDengue.SE == maximaSE]
        dataFrameDengue = casosSemanaSeleccionada[["Provincia", "Autoctonos", "IA"]]
        # dataFrameDengue.IA.round()
        dataFrameDengue.sort_values(by="IA", ascending=False).round(2)
        return html.Div(
            [
                dbc.Container(
                    children=[
                        html.H4(
                            children=["Datos actualizados al {}".format(ultimaFecha)],
                            style={"padding": "10px"},
                        ),
                        dbc.Card(generate_table(dataFrameDengue)),
                    ],
                    style={"textAlign": "center"},
                )
            ]
        )


@app.callback(Output("tabsReg", "children"), [Input("tabsRegiones", "active_tab")])
def tab_regiones(tab):
    if tab == "tab-1":
        figRegionAutoctonos = px.line(
            dengueRegionesAut, x="FechaReporte", y="Autoctonos", color="Region"
        ).update_layout(
            xaxis={"tickformat": "%y/%m"},
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos autóctonos confirmados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos autoctónos por Region",
                                id="collapse-button-regiones",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-regiones",
                            children=[dcc.Markdown(infoCasosAutoctonos)],
                        ),
                    ]
                ),
                dcc.Graph(figure=figRegionAutoctonos),
            ]
        )
    elif tab == "tab-2":
        figRegionImportados = px.line(
            dengueRegionesImp, x="FechaReporte", y="Importados", color="Region"
        ).update_layout(
            xaxis={"tickformat": "%y/%m"},
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos importados confirmados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos importados por Region",
                                id="collapse-button-regiones",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-regiones",
                            children=[
                                html.P(
                                    "Caso importado: caso confirmado de dengue Con Antecedentes de Viaje al Exterior (CAVE)",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figRegionImportados),
            ]
        )
    elif tab == "tab-3":
        figRegionEnInv = px.bar(
            dengueRegionesInv, x="FechaReporte", y="Total en Inv", color="Region"
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos en investigación",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos en investigación por Region"),
                        html.P("", className="lead"),
                    ]
                ),
                dcc.Graph(figure=figRegionEnInv),
            ]
        )
    elif tab == "tab-4":
        figRegionNotificados = px.line(
            dengueRegionesNotif,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Region",
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos notificados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos notificados por Region",
                                id="collapse-button-regiones",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-regiones",
                            children=[
                                html.P(
                                    "Casos notificados: Son casos con sospecha de dengue notificados al Sistema Nacional de Vigilancia de la Salud (SNVS 2.0)",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figRegionNotificados),
            ]
        )
    elif tab == "tab-5":
        figRegionFallecidos = px.line(
            dengueRegionesFall, x="FechaReporte", y="AcumFallecidos", color="Region"
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Fallecidos",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de personas fallecidas por provincia",
                                id="collapse-button-regiones",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-regiones",
                            children=[
                                html.P(
                                    "Fallecimientos: personas fallecidas con confirmación de dengue.",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figRegionFallecidos),
            ]
        )


@app.callback(Output("tabsTotal", "children"), [Input("tabsPais", "active_tab")])
def tab_pais(tab):
    if tab == "tab-1":
        figPaisAutoctonos = px.line(
            denguePaisAut, x="FechaReporte", y="Autoctonos", color="Pais"
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos autóctonos confirmados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos autoctónos en Argentina en 2020",
                                id="collapse-button-pais",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-pais",
                            children=[dcc.Markdown(infoCasosAutoctonos)],
                        ),
                    ]
                ),
                dcc.Graph(figure=figPaisAutoctonos),
            ]
        )
    elif tab == "tab-2":
        figPaisImportados = px.line(
            denguePaisImp, x="FechaReporte", y="Importados", color="Pais"
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos importados confirmados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos importados en Argentina en 2020",
                                id="collapse-button-pais",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-pais",
                            children=[
                                html.P(
                                    "Caso importado: caso confirmado de dengue Con Antecedentes de Viaje al Exterior (CAVE)",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figPaisImportados),
            ]
        )
    elif tab == "tab-3":
        figPaisEnInv = px.bar(
            denguePaisInv, x="FechaReporte", y="Total en Inv", color="Pais"
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos en investigación",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4("Total de casos en investigación en Argentina en 2020"),
                        html.P("", className="lead"),
                    ]
                ),
                dcc.Graph(figure=figPaisEnInv),
            ]
        )
    elif tab == "tab-4":
        figPaisNotif = px.line(
            denguePaisNotif,
            x="FechaReporte",
            y="Total notificados para dengue",
            color="Pais",
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Casos notificados",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de casos notificados en Argentina en 2020",
                                id="collapse-button-pais",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-pais",
                            children=[
                                html.P(
                                    "Casos notificados: Son casos con sospecha de dengue notificados al Sistema Nacional de Vigilancia de la Salud (SNVS 2.0)",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figPaisNotif),
            ]
        )
    elif tab == "tab-5":
        figPaisFall = px.line(
            denguePaisFall, x="FechaReporte", y="AcumFallecidos", color="Pais"
        ).update_layout(
            xaxis_title="Fecha de Reporte",
            yaxis_title="Fallecidos",
            legend={"traceorder": "normal"},
        )
        return html.Div(
            [
                dbc.Col(
                    [
                        html.H4(
                            dbc.Button(
                                "Total de personas fallecidas por provincia",
                                id="collapse-button-pais",
                                color="link",
                            )
                        ),
                        dbc.Collapse(
                            id="collapse-pais",
                            children=[
                                html.P(
                                    "Fallecimientos: personas fallecidas con confirmación de dengue.",
                                    className="lead",
                                ),
                            ],
                        ),
                    ]
                ),
                dcc.Graph(figure=figPaisFall),
            ]
        )


if __name__ == "__main__":
    app.run_server(debug=True)
