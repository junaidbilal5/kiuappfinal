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
df=pd.read_csv('./data/Student Section.csv')

year = df.Year.drop_duplicates().sort_values()
semester= df.Semester.drop_duplicates().sort_values()
from app import app

from dash_extensions import Lottie

######-------------------------URL of Lottie Animations---------------------------------------------------###
enrolled='https://assets5.lottiefiles.com/packages/lf20_dT1E1P.json'
scholars= 'https://assets9.lottiefiles.com/packages/lf20_htEgHu.json'
teacher='https://assets5.lottiefiles.com/private_files/lf30_g4ft9Z.json'
active='https://assets9.lottiefiles.com/packages/lf20_Q895iE.json'


options = dict(loop=2, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

##-----------------------------------------------------------##--------------------------------------------###



def StudentsLayout():
	return [

		html.Div([

		html.Div([

		html.Div(
							children = [
								# Title and subtitle
								html.Div(
									children = [
										html.H1(
											children = "Students Section/قسم الطلاب",
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
						id="dropdown(student)",
						options=[{"label": x, "value": x} for x in year],
						value=year[0],
						clearable=False,
						style={"width": "55%", },
						className='dcc_compon'
					),
				], className='create_container three columns'),

		html.Div([
					html.Label(['Select Semester'],style={'font-weight': 'bold', 'color':'black'}),
					dcc.Dropdown(
						id="dropdown1(student)",
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


		# html.Div(
		# 			children = [
		# 				html.Div(
		# 					children = [
		# 						# Title
		# 						html.H6(
		# 							children = "Total Students Enrolled/مجموع الطلاب",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}
		# 						),
		# 						(Lottie(options=options, width='20%', height='20%', url=enrolled)),
		# 						# Total value
		# 						html.P(id="card_1(student)",
		# 							children = "1117",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "#dd1e35",
		# 								"fontSize": 40
		# 							}
		# 						),
		#
		# 					],
		# 					className = "create_container three columns"
		# 				),
		# 				# (Column 2): Approved
		# 				html.Div(
		# 					children = [
		# 						# Title
		# 						html.H6(
		# 							children = "Total Students on Scholarship/مجموع الطلاب في المنحة",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}
		# 						),
		# 						(Lottie(options=options, width='20%', height='20%', url=scholars)),
		# 						# Total value
		# 						html.P(id="card_2(student)",
		# 							children = "50",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "#dd1e35",
		# 								"fontSize": 40
		# 							}
		# 						),
		#
		# 					],
		# 					className = "card_container three columns"
		# 				),
		#
		# html.Div(
		# 					children = [
		# 						# Title
		# 						html.H6(
		# 							children = "Teacher to Students Ratio/نسبة المدرسين إلى الطلاب",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}
		# 						),
		# 						(Lottie(options=options, width='20%', height='20%', url=teacher)),
		# 						# Total value
		# 						html.P(id="card_3(student)",
		# 							children = "1:3",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "#dd1e35",
		# 								"fontSize": 40
		# 							}
		# 						),
		#
		# 					],
		# 					className = "card_container three columns"
		# 				),
		#
		# html.Div(
		# 					children = [
		# 						# Title
		# 						html.H6(
		# 							children = "Number of Active Courses/عدد الدورات النشطة",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "black"
		# 							}
		# 						),
		# 						(Lottie(options=options, width='20%', height='20%', url=active)),
		# 						# Total value
		# 						html.P(id="card_4(student)",
		# 							children = "260",
		# 							style = {
		# 								"textAlign": "center",
		# 								"color": "#dd1e35",
		# 								"fontSize": 40
		# 							}
		# 						),
		#
		# 					],
		# 					className = "card_container three columns"
		# 				),
		#
		# 			],
		# 			className = "row flex-display"
		# 		),

			html.Div([
				html.Div([
					dcc.Graph(id='the_graph2(student)', config={
						"displayModeBar": "hover"
					})
				], className="create_container eleven columns"),

			], className="row flex-display"),

			###-------------------------------------------------Gauge Meter-----------------------------------------------##

			html.Div([

				html.Div(
					children=[
						# Donut chart
						dcc.Graph(
							id="pie_chart4(student)",
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
							id="pie_chart5(student)",
							config={
								"displayModeBar": "hover"
							}
						)
					],
					className="create_container six columns",
					## Width of the pie grapgh

				),

			], className="row flex-display"),
			html.Div([
				html.Div(
					children=[
						# Donut chart
						dcc.Graph(
							id="pie_chart6(student)",
							config={
								"displayModeBar": "hover"
							}
						)
					],
					className="create_container twelve columns",
					## Width of the pie grapgh

				),

				html.Div(
					children=[
						# Donut chart
						dcc.Graph(
							id="pie_chart7(student)",
							config={
								"displayModeBar": "hover"
							}
						)
					],
					className="create_container twelve columns",
					## Width of the pie grapgh

				),

			], className="row flex-display"),

		html.Div([

		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "pie_chart(student)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container three columns",

						),

		html.Div(
							children = [
								# Donut chart
								dcc.Graph(
									id = "pie_chart1(student)",
									config = {
										"displayModeBar": "hover"
									}
								)
							],
							className = "create_container three columns",
					## Width of the pie grapgh

						),

			html.Div(
				children=[
					# Donut chart
					dcc.Graph(
						id="pie_chart2(student)",
						config={
							"displayModeBar": "hover"
						}
					)
				],
				className="create_container three columns",
				## Width of the pie grapgh

			),

			html.Div(
				children=[
					# Donut chart
					dcc.Graph(
						id="pie_chart3(student)",
						config={
							"displayModeBar": "hover"
						}
					)
				],
				className="create_container three columns",
				## Width of the pie grapgh

			),

		],className = "row flex-display"),


		],id = "mainContainer",
			style = {
				"display": "flex",
				"flex-direction": "column"
			}),

		])

		]

####-----------------------Callbacks for Gauge-Meters------------------------------####

@app.callback(
    Output(component_id='gauge(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)
    present = df[mask].Hours_conducted.sum()
    total = df[mask].Total_hours.sum()
    attendance = (present / total) * 100

    gauge1 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=attendance,
	domain={'x': [0, 1], 'y': [0, 1]},
	gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#f76b25"}}))
    gauge1.update_layout(
		height=300,
		margin=dict(l=10, r=10, t=40, b=10),
		showlegend=False,
		template="plotly_dark",
		plot_bgcolor='white',
		paper_bgcolor='white',
		font_color="black",
		font_size=10
	)

    return gauge1

#####---------------------------------------------------------------######----------------------------------------------###

@app.callback(
    Output(component_id='gauge1(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)
    modules_complete = df[mask].Modules_comp.sum()
    total_modules = df[mask].Total_modules.sum()
    performance = (modules_complete / total_modules) * 100

    gauge2 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=performance,
	domain={'x': [0, 1], 'y': [0, 1]},
	gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#f76b25"}}))
    gauge2.update_layout(
		height=300,
		margin=dict(l=10, r=10, t=40, b=10),
		showlegend=False,
		template="plotly_dark",
		plot_bgcolor='white',
		paper_bgcolor='white',
		font_color="black",
		font_size=10
	)

    return gauge2


@app.callback(
    Output(component_id='the_graph2(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
	if year==2021:

		categories = ['Arabic College/الكلية العربية', 'English College/كلية اللغة الإنجليزية', 'French College/الكلية الفرنسية', 'Urdu College/كلية الأردية']

		fig = go.Figure()
		fig.add_trace(go.Bar(
			x=categories,
			y=[285, 377, 250, 150],
			name='Bachlore(البكالوريوس)',
			marker_color='rgb(87, 212, 122)'
		))
		fig.add_trace(go.Bar(
			x=categories,
			y=[336, 255, 200, 125],
			name='General Secondary/الثانوية العامة',
			marker_color='rgb(87, 156, 212)'
		))

		fig.add_trace(go.Bar(
			x=categories,
			y=[67, 135, 120, 170],
			name='Masters Degree/ماجيستير',
			marker_color='rgb(195, 87, 212)'
		))

		fig.add_trace(go.Bar(
			x=categories,
			y=[12, 20, 15, 13],
			name='PHD/دكتوراه',
			marker_color='rgb(212, 133, 87)'
		))

		# Here we modify the tickangle of the xaxis, resulting in rotated labels.
		fig.update_layout(barmode='group')
		# fig.show()
		fig.update_layout(
			height=550,
			paper_bgcolor='white',
			plot_bgcolor='white',
			title=f'<b>Summary of Colleges</b>',
			title_font_color='Black',
			title_font_size=20,
			showlegend=True,

		)
		return fig
	if year==2020:
		categories = ['Arabic College/الكلية العربية', 'English College/كلية اللغة الإنجليزية', 'French College/الكلية الفرنسية', 'Urdu College/كلية الأردية']

		fig = go.Figure()
		fig.add_trace(go.Bar(
			x=categories,
			y=[270, 300, 240, 145],
			name='Bachlore(البكالوريوس)',
			marker_color='rgb(87, 212, 122)'
		))
		fig.add_trace(go.Bar(
			x=categories,
			y=[330, 240, 150, 115],
			name='General Secondary/الثانوية العامة',
			marker_color='rgb(87, 156, 212)'
		))

		fig.add_trace(go.Bar(
			x=categories,
			y=[60, 125, 110, 150],
			name='Masters Degree/ماجيستير',
			marker_color='rgb(195, 87, 212)'
		))

		fig.add_trace(go.Bar(
			x=categories,
			y=[10, 25, 10, 11],
			name='PHD/دكتوراه',
			marker_color='rgb(212, 133, 87)'
		))

		# Here we modify the tickangle of the xaxis, resulting in rotated labels.
		fig.update_layout(barmode='group')
		# fig.show()
		fig.update_layout(
			height=550,
			paper_bgcolor='white',
			plot_bgcolor='white',
			title=f'<b>Summary of Colleges</b>',
			title_font_color='Black',
			title_font_size=20,
			showlegend=True,

		)
		return fig




@app.callback(
    Output(component_id='pie_chart(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)
    labels = ['Male', 'Female']
    values = [156, 132]


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
										"text": "Gender Proportion in Arabic College /نسبة الجنس في كلية اللغة العربية",
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
    Output(component_id='pie_chart1(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)
    labels = ['Male', 'Female']
    values = [66, 252]


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
										"text": "Gender Proportion in Urdu College/نسبة الجنس في كلية الأردية ",
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
    Output(component_id='pie_chart2(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)
    labels = ['Male', 'Female']
    values = [95,199]


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
										"text": " Gender Proportion in English College/نسبة الجنس في كلية اللغة الإنجليزية",
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
    Output(component_id='pie_chart3(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)
    labels = ['Male', 'Female']
    values = [52,39]


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
										"text": " Gender Proportion in French College/نسبة الجنس في الكلية الفرنسية",
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
    Output(component_id='pie_chart4(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)


    labels = ['Pakistan',
'India',
'Canada',
'South Africa',
'United Kingdom',
'Nepal'
]
    values = [295,
41,
3,
1,
1,
1,
]

    fig = {
		"data": [
			go.Bar(
				x=labels,
				y=values,
				name="Department Wise",
				marker={
					"color": "rgb(219, 191, 249)",

				},
				hoverinfo="text",

			),

		],

		"layout": go.Layout(
			title={
				"text": f" Urdu College Country Wise /دولة كلية الأوردو ",
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
				"title": "<b>Department/قسم</b>",
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
				"title": "<b>Number of students/عدد المتقدمين</b>",
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
    Output(component_id='pie_chart5(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)


    labels = ['France',
'Cameroon',
'Canada',
'Belgium',
'Senegal',
'Guinea',
'Benin',
'Egypt'
'Switzerland',
'Togo',
'United Kingdom',
'Vietnam'

]
    values = [63,
22,
12,
6,
5,
2,
2,
1,
1,
1,
1,
1,

]

    fig = {
		"data": [
			go.Bar(
				x=labels,
				y=values,
				name="Department Wise",
				marker={
					"color": "rgb(219, 191, 249)",

				},
				hoverinfo="text",

			),

		],

		"layout": go.Layout(
			title={
				"text": f" French College Country Wise /نسبة الكلية الفرنسية ",
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
				"title": "<b>Department/قسم</b>",
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
				"title": "<b>Number of students/عدد المتقدمين</b>",
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
    Output(component_id='pie_chart7(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)


    labels = ['Sudan',
'Egypt',
'Senegal',
'Algeria',
'Somalia',
'Jordan',
'Tunisia',
'India',
'Nigeria',
'Yemen',
'United Arab Emirates',
'Syria, Syrian Arab Republic',
'Morocco',
'Mali',
'Pakistan',
'Palestine',
'United Kingdom',
'France',
'Kuwait',
'Libya',
'Turkey',
'United States',
'Iran (Islamic Republic of)',
'Cote dIvoire (Ivory Coast)',
'Australia',
'Netherlands',
'Indonesia',
'Burkina Faso',
'Kenya',
'Iraq',
'Bahrain',
'Comoros',
'Saudi Arabia',
'Ghana',
'Chad',
'Italy',
'Bangladesh',
'Oman'


]
    values = [64,
55,
36,
33,
15,
14,
11,
8,
8,
7,
6,
6,
6,
5,
4,
4,
4,
3,
3,
3,
2,
2,
2,
2,
2,
2,
2,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,


]

    fig = {
		"data": [
			go.Bar(
				x=labels,
				y=values,
				name="Department Wise",
				marker={
					"color": "rgb(219, 191, 249)",

				},
				hoverinfo="text",

			),

		],

		"layout": go.Layout(
			title={
				"text": f" Arabic College Country Wise/نسبة الكلية العربية بالدولة  ",
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
				"title": "<b>Department/قسم</b>",
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
				"title": "<b>Number of students/عدد المتقدمين</b>",
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
    Output(component_id='pie_chart6(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year,semester):



    mask= (df['Year']==year)  & (df['Semester']==semester)


    labels = ['Nigeria',
'India',
'United Kingdom',
'Ghana',
'Egypt',
'Kenya',
'Pakistan',
'Australia',
'Canada',
'United States',
'Sri Lanka',
'United Arab Emirates',
'Brunei Darussalam',
'Somalia',
'Bangladesh',
'Malaysia',
'Indonesia',
'Uzbekistan',
'Benin',
'Algeria'
'Qatar',
'Slovenia'
'Uganda',
'South Africa',
'Kazakhstan',
'Romania',
'Slovakia (Slovak Republic)',
'Botswana'
'France',
'Philippines',
'Sudan'
'Iran (Islamic Republic of)',
'Libya',
'Sweden',
'Tanzania',
'Yemen'


]
    values = [109,
81,
24,
20,
20,
14,
14,
6,
6,
4,
4,
3,
3,
3,
3,
2,
2,
2,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,

]

    fig = {
		"data": [
			go.Bar(
				x=labels,
				y=values,
				name="Department Wise",
				marker={
					"color": "rgb(219, 191, 249)",

				},
				hoverinfo="text",

			),

		],

		"layout": go.Layout(
			title={
				"text": f" English College Country Wise/نسبة اللغة الإنجليزية بالبلد  ",
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
				"title": "<b>Department/قسم</b>",
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
				"title": "<b>Number of students/عدد المتقدمين</b>",
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
    Output(component_id='small_bar(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))

def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('Request').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['StudentID'],
                y=dfg['Request'],
                name="Department Wise",
				orientation='h',
                marker={
                    "color": "#f79d9c",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"Number of Student Requests /الطلبات ",
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
                "title": "<b>Total number/الرقم الإجمالي</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
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
                "title": "<b>Request Status/حالة الطلب</b>",
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
    Output(component_id='small_bar1(student)', component_property='figure'),
     Input("dropdown(student)", "value"),
     Input("dropdown1(student)", "value"))
def update_graph(year, semester):
    mask= (df['Year']==year)  & (df['Semester']==semester)


    dfg=df[mask].groupby('Country').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['Country'],
                y=dfg['StudentID'],
                name="Country Wise",
                marker={
                    "color": "#f79d9c",
                    "opacity":0.6,
                },
                hoverinfo="text",

            ),


        ],

        "layout": go.Layout(
            title={
                "text": f"Number of Students from Country /الطلاب في جميع أنحاء البلدان ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "black",
                "size": 19
            },
            xaxis={
                "title": "<b>Country/دولة</b>",
                "color": "black",
                "showline": True,
                "showgrid": False,
                "showticklabels": True,
                "linecolor": "black",
                "linewidth": 1,
                "ticks": "outside",
				'categoryorder': 'total descending',
                "tickfont": {
                    "family": "Aerial",
                    "color": "black",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Students/تلاميذ</b>",
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
    app.run_server(debug=True, port=1439, )