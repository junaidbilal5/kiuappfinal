import pandas as pd
import datetime as dt
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import calendar
import plotly
import plotly.express as px
from app import app
df=pd.read_csv('./data/Scholarship1.csv',parse_dates=['Start_Year'])
df["Year"]=df["Start_Year"].dt.strftime("%Y")
year = df.Year.drop_duplicates().sort_values()

sponsor=df.SponsorNo.drop_duplicates().sort_values()

from dash_extensions import Lottie

######-------------------------URL of Lottie Animations---------------------------------------------------###
money='https://assets1.lottiefiles.com/packages/lf20_SyUX5x.json'
approved= 'https://assets2.lottiefiles.com/private_files/lf30_vfmaknbp.json'
sponsor='https://assets4.lottiefiles.com/packages/lf20_0cvczw8l.json'



options = dict(loop=2, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

##-----------------------------------------------------------##--------------------------------------------###

def ScholarshipTab():
    return [

        html.Div([


        html.Div(
                            children = [
                                # Title and subtitle
                                html.Div(
                                    children = [
                                        html.H1(
                                            children = "Scholarship Section/قسم الابتعاث",
                                            style = {
                                                "margin-bottom": "0",
                                                "color": "black"
                                            }
                                        ),

                                    ]
                                )
                            ],
                            className = "six column",
                            id = 'title'
                        ),

        html.Div([

                html.Div([
                    html.Label(['Select Year'],style={'font-weight': 'bold', 'color':'black'}),
                    dcc.Dropdown(
                        id="dropdown(scholarship)",
                        options=[{"label": x, "value": x} for x in year],
                        value=year[0],
                        clearable=False,
                        style={"width": "55%", },
                        className='dcc_compon'
                    ),
                ], className='create_container three columns'),

        ],className = "row flex-display",
                    style = {
                        "margin-bottom": "25px"
                    }),
        html.Div(
                    children = [
                        # (Column 1): Total Applied
                        html.Div(
                            children = [
                                # Title
                                html.H6(
                                    children = "Total Students Availing Scholarship/عدد طلاب المنح",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),
                                (Lottie(options=options, width='20%', height='20%', url=approved)),
                                # Total value
                                html.P(id="card_11",
                                    children = "000",
                                    style = {
                                        "textAlign": "center",
                                        "color": "orange",
                                        "fontSize": 40
                                    }
                                ),

                            ],
                            className = "create_container three columns"
                        ),
                        # (Column 2): Approved
                        html.Div(
                            children = [
                                # Title
                                html.H6(
                                    children = "Total Amount Spent/إجمالي المبلغ المنفق",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),
                                (Lottie(options=options, width='25%', height='25%', url=money)),
                                # Total value
                                html.P(id="card_22",
                                    children = "000",
                                    style = {
                                        "textAlign": "center",
                                        "color": "#dd1e35",
                                        "fontSize": 40
                                    }
                                ),

                            ],
                            className = "card_container three columns"
                        ),

        html.Div(
                            children = [
                                # Title
                                html.H6(
                                    children = "Total Sponsors/الرعاة",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),
                                (Lottie(options=options, width='20%', height='20%', url=sponsor)),
                                # Total value
                                html.P(id="card_33",
                                    children = "000",
                                    style = {
                                        "textAlign": "center",
                                        "color": "#dd1e35",
                                        "fontSize": 40
                                    }
                                ),

                            ],
                            className = "card_container three columns"
                        ),

                    ],
                    className = "row flex-display"
                ),


        html.Div([
            html.Div([
                dcc.Graph(id='bar-graph(scholarship)',config = {
                                        "displayModeBar": "hover"
                                    })
            ],className = "create_container six columns",style = {
                                "maxWidth": "800px"
                            }),

        html.Div([
                dcc.Graph(id='bar-graph1(scholarship)',config = {
                                        "displayModeBar": "hover"
                                    })
            ],className = "create_container six columns",style = {
                                "maxWidth": "1000px"
                            }),


        html.Div(
                            children = [
                                # Donut chart
                                dcc.Graph(
                                    id = "pie_chart(scholarship)",
                                    config = {
                                        "displayModeBar": "hover"
                                    }
                                )
                            ],
                            className = "create_container four columns",
                            style = {
                                "maxWidth": "450px"
                            }
                        ),
        html.Div(
                            children = [
                                # Donut chart
                                dcc.Graph(
                                    id = "pie_chart1(scholarship)",
                                    config = {
                                        "displayModeBar": "hover"
                                    }
                                )
                            ],
                            className = "create_container four columns",
                    ## Width of the pie grapgh
                            style = {
                                "maxWidth": "400px"
                            }
                        ),

            html.Div([
                dcc.Graph(id='the_graph2(scholarship)', config={
                    "displayModeBar": "hover"
                })
            ], className="create_container four columns"),

            html.Div([
                dcc.Graph(id='the_graph3(scholarship)', config={
                    "displayModeBar": "hover"
                })
            ], className="create_container five columns"),


        ],className = "row flex-display"),




        ],id = "mainContainer",
            style = {
                "display": "flex",
                "flex-direction": "column"
            }),


]

@app.callback(
    Output('card_11', 'children'),
	Output('card_22', 'children'),
    Output('card_33', 'children'),

	# Input("dropdown", "value"),     Year id
	Input("dropdown(scholarship)", "value"))


def update_card(year):
    dfg= df.copy()
	# mask = (dfg['Start_Year'] == year)  & (dfg['SponsorNo'] == sponsor)
    mask1=(dfg['Start_Year'] == year)

    total_students=dfg[mask1]['StudentID'].count()
    total_amount = df[mask1]['Sch_Amount'].sum()
    total_sponsors=df[mask1]['SponsorNo'].nunique()
    return total_students, total_amount, total_sponsors

###----------------------------------------------------####-----------------------------------------------------####

@app.callback(
    Output(component_id='bar-graph(scholarship)', component_property='figure'),
     Input("dropdown(scholarship)", "value"))

def update_graph(year):
    mask = (df['Start_Year'] == year)
    dfg = df[mask].groupby('Department').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['StudentID'],
                y=dfg['Department'],

                orientation='h',
                name="Sponosor",
                marker={
                    "color": "#88B2FF"
                },
                hoverinfo="text",

            ),

        ],
        "layout": go.Layout(
            title={
                "text": "Total Student scholarship by College/إجمالي المنحة الدراسية للطلاب حسب الكلية  ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 15
            },
            xaxis={
                "title": "<b>Number of students/عدد الطلاب</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                'categoryorder': 'total descending',
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>College /كلية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "white",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )
    }
    # Return the figure
    return fig




@app.callback(
    Output(component_id='bar-graph1(scholarship)', component_property='figure'),
     Input("dropdown(scholarship)", "value"))

def update_graph(year):
    mask=df['Start_Year']==year
    dfg=df[mask].groupby('Country').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['Country'],
                y=dfg['StudentID'],
                name="Country wise",
                marker={
                    "color": "#88B2FF"
                },
                hoverinfo="text",

            ),

        ],
        "layout": go.Layout(
            title={
                "text": "Number of scholarships by country/عدد المنح الدراسية حسب الدولة",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 15
            },
            xaxis={
                "title": "<b>Country/دولة</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                'categoryorder': 'total descending',
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Number of students/عدد الطلاب</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "#1f2c56",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )
    }
    # Return the figure
    return fig



####-------------------Line Charts-------------------------##

@app.callback(
    Output(component_id='the_graph2(scholarship)', component_property='figure'),

	 Input("dropdown(scholarship)", "value"))

def update_graph(year):

    dfg=df.groupby('Start_Year')['Sch_Amount'].sum().reset_index()

    fig = {
        "data": [
            go.Scatter(
                x=dfg['Start_Year'],
                y=dfg['Sch_Amount'],
                name="Department Wise",
                marker={
                    'color':'rgb(186, 225, 247)'
                },
                hoverinfo="text",
                fill='tozeroy',
                fillcolor='rgba(232, 255, 249, 0.6)'

            ),

        ],
        "layout": go.Layout(
            title={
                "text": "Yearly scholarship amount/مبلغ المنحة السنوية ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 15
            },
            xaxis={
                "title": "<b>Year/عام</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                'categoryorder': 'total descending',
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Amount spent/المقدار المنفق</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )
    }
    # Return the figure
    return fig

@app.callback(
    Output(component_id='the_graph3(scholarship)', component_property='figure'),

	 Input("dropdown(scholarship)", "value"))

def update_graph(year):

    dfg=df.groupby('Start_Year')['SponsorNo'].nunique().reset_index()

    fig = {
        "data": [
            go.Scatter(
                x=dfg['Start_Year'],
                y=dfg['SponsorNo'],
                name="Department Wise",
                marker={
                    'color':'rgb(186, 225, 247)'
                },
                hoverinfo="text",
                fill='tozeroy',
                fillcolor='rgba(232, 255, 249, 0.6)'

            ),

        ],
        "layout": go.Layout(
            title={
                "text": "Yearly sponsor numbers/عدد الرعاة سنويا ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 15
            },
            xaxis={
                "title": "<b>Year/عام</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                'categoryorder': 'total descending',
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Sponsors/الرعاة</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "black",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="white",
            plot_bgcolor="white",
            legend={
                "orientation": "h",
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )
    }
    # Return the figure
    return fig

@app.callback(
    Output(component_id='pie_chart(scholarship)', component_property='figure'),
	Input("dropdown(scholarship)", "value"))

def update_graph(year):



	mask = (df['Start_Year'] == year)
	labels = df[mask]['Gender'].unique()
	values = df[mask]['Gender'].value_counts()


	fig = {
								"data": [
									go.Pie(
										labels=labels,
										values=values,
										marker={

										},
										hoverinfo="label+value+percent",
										textinfo="percent",
										hole=0.7,
										rotation=45,
										insidetextorientation="radial"
									)
								],
								"layout": go.Layout(
									title={
										"text": f"Gender-wise scholarship students/  الجنس (الطلاب)",
										"y": 0.93,
										"x": 0.5,
										"xanchor": "center",
										"yanchor": "top"
									},
									titlefont={
										"color": "black",
										"size": 15
									},
									font={
										"family": "sans-serif",
										"color": "black",
										"size": 12
									},
									hovermode="closest",
									paper_bgcolor="white",
									plot_bgcolor="white",
									legend={
										"orientation": "h",
										"bgcolor": "white",
										"xanchor": "center",
										"x": 0.5,
										"y": -0.7
									}
								)
							}

	return fig


@app.callback(
    Output(component_id='pie_chart1(scholarship)', component_property='figure'),
	Input("dropdown(scholarship)", "value"))

def update_graph(year):


#make sure to make copy of the datafreame and never play with the original one.
	mask = (df['Start_Year'] == year)
	labels = ['Asian', 'European', 'ME','African']
	values = df[mask]['Ethnicity'].value_counts()


	fig = {
								"data": [
									go.Pie(
										labels=labels,
										values=values,

										hoverinfo="value+label+percent",
										textinfo="percent",
                                        hole=0.3,

										rotation=45,
										insidetextorientation="radial"
									)
								],
								"layout": go.Layout(
									title={
										"text": f"Continent-wise scholarship holders/طلاب المنح الدراسية عبر القارة",
										"y": 0.93,
										"x": 0.5,
										"xanchor": "center",
										"yanchor": "top"
									},
									titlefont={
										"color": "black",
										"size": 15
									},
									font={
										"family": "sans-serif",
										"color": "black",
										"size": 12
									},
									hovermode="closest",
									paper_bgcolor="white",
									plot_bgcolor="white",
									legend={
										"orientation": "h",
										"bgcolor": "white",
										"xanchor": "center",
										"x": 0.5,
										"y": -0.7
									}
								)
							}

	return fig



if __name__ == '__main__':
    app.run_server(debug=True, port=1260, )