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
df=pd.read_csv('./data/Teachers.csv')
df2=pd.read_csv('./data/Teacher_nationality.csv')
df2=df2.fillna(0)
from app import app
year = df.Year.drop_duplicates().sort_values()
semester= df.Semester.drop_duplicates().sort_values()

from dash_extensions import Lottie

######-------------------------URL of Lottie Animations---------------------------------------------------###
teacher='https://assets1.lottiefiles.com/private_files/lf30_g4ft9Z.json'
quiz='https://assets7.lottiefiles.com/private_files/lf30_6ocpfdil.json'
assignment='https://assets9.lottiefiles.com/private_files/lf30_VrsZnP.json'

options = dict(loop=2, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))



def TeachersLayout():
	return [


		html.Div([

		html.Div([

		html.Div(
							children = [
								# Title and subtitle
								html.Div(
									children = [
										html.H1(
											children = "Teachers Section/قسم المعلمين",
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
					html.Label(['Select Year/عام'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown(teacher)",
						options=[{"label": x, "value": x} for x in year],
						value=year[0],
						clearable=False,
						style={"width": "55%", },
						className='dcc_compon'
					),
				], className='create_container three columns'),

		html.Div([
					html.Label(['Select Semester/حدد الفصل الدراسي'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown1(teacher)",
						options=[{"label": x, "value": x} for x in semester],
						value=semester[0],
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
						html.Div(
							children = [
								# Title
								html.H6(
									children = "Total Teachers/مجموع المعلمين",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='20%', height='20%', url=teacher)),
								# Total value
								html.P(id="card_1(teacher)",
									children = "300",
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
									children = "Total Assignments Given/مجموع التعيينات الممنوحة",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='20%', height='20%', url=assignment)),

								# Total value
								html.P(id="card_2(teacher)",
									children = "150",
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
									children = "Total Tests Taken/مجموع الاختبارات التي تم إجراؤها",
									style = {
										"textAlign": "center",
										"color": "black"
									}
								),
								(Lottie(options=options, width='34%', height='34%', url=quiz)),
								# Total value
								html.P(id="card_3(teacher)",
									children = "200",
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

		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "small_bar(teacher)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container five columns",
						),

        html.Div(
            children=[
                # Donut chart
                dcc.Graph(
                    id="small_bar11(teacher)",
                    config={
                        "displayModeBar": "hover"
                    }
                )
            ],
            className="create_container six columns",
        ),

		], className="row flex-display"),



			html.Div([

				html.Div(
					children=[
						# Donut chart
						dcc.Graph(
							id="small_bar12(teacher)",
							config={
								"displayModeBar": "hover"
							}
						)
					],
					className="create_container five columns",
                    ),
                html.Div(
                    children=[
                        # Donut chart
                        dcc.Graph(
                            id="small_bar13(teacher)",
                            config={
                                "displayModeBar": "hover"
                            }
                        )
                    ],
                    className="create_container six columns",
                ),
			], className="row flex-display"),




		],id = "mainContainer",
			style = {
				"display": "flex",
				"flex-direction": "column"
			}),

		])
]
####-----------------------Callbacks for Gauge-Meters------------------------------####




#####---------------------------------------------------------------######----------------------------------------------###











@app.callback(
    Output(component_id='small_bar(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    maks= df2[df2['Deparment']=='Arabic']






    fig = {
        "data": [
            go.Bar(
                x=maks['Country'],
                y=maks['Teachers'],
                name="Country-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text":'Teachers Nationality in Arabic College/جنسية المعلمين بالكلية العربية' ,
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
                "title": "<b> Nationality/جنسية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Teachers/معلمون</b>",
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
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig


@app.callback(
    Output(component_id='small_bar11(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    maks= df2[df2['Deparment']=='English']



    fig = {
        "data": [
            go.Bar(
                x=maks['Country'],
                y=maks['Teachers'],
                name="Country-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text":'Teachers Nationality in English College/جنسية المعلمين بالكلية الانجليزية' ,
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
                "title": "<b> Nationality/جنسية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Teachers/معلمون</b>",
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
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig


@app.callback(
    Output(component_id='small_bar12(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    maks= df2[df2['Deparment']=='Urdu']



    fig = {
        "data": [
            go.Bar(
                x=maks['Country'],
                y=maks['Teachers'],
                name="Country-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text":'Teachers Nationality in Urdu College/جنسية المعلمين بالكلية الأردية' ,
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
                "title": "<b> Nationality/جنسية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Teachers/معلمون</b>",
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
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig


@app.callback(
    Output(component_id='small_bar13(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))

def update_graph(year, semester):
    maks= df2[df2['Deparment']=='French']



    fig = {
        "data": [
            go.Bar(
                x=maks['Country'],
                y=maks['Teachers'],
                name="Country-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text":'Teachers Nationality in French College/جنسية المعلمين بالكلية الفرنسية' ,
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
                "title": "<b> Nationality/جنسية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Teachers/معلمون</b>",
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
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig




@app.callback(
    Output(component_id='small_bar1(teacher)', component_property='figure'),
     Input("dropdown(teacher)", "value"),
     Input("dropdown1(teacher)", "value"))


def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('College').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['College'],
                y=dfg['Teacher_Name'],
                name="College-wise teachers",
                marker={
                    "color": "rgb(219, 191, 249)",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"College Wise Number of Teachers /عدد المعلمين الحكيم في الكلية ",
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
                "title": "<b> College/كلية</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
				'categoryorder': 'total descending',
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Teachers/معلمون</b>",
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
                "bgcolor": "black",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )


    }
    return fig



if __name__ == '__main__':
    app.run_server(debug=True, port=1440, )