import pandas as pd
from app import app
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import calendar
import dash_bootstrap_components as dbc
from dash_extensions import Lottie
df=pd.read_csv('./data/KIU3.csv', parse_dates=['Date'])
df = df.astype({"AppID": str})
df["Year"]=df["Date"].dt.strftime("%Y")
year = df.Year.drop_duplicates()
AcTerm= df.AcademicTerm.drop_duplicates().sort_values()

dict_of_locations = df.set_index("Country")[["Lat", "Long"]].T.to_dict("dict")

##------------------Get Month Names---------------------------##

df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x],)


month = df.Month.unique()

from . import ArabicPage as cP





######-------------------------URL of Lottie Animations---------------------------------------------------###
applied='https://assets8.lottiefiles.com/packages/lf20_s3u31uyq.json'
approved= 'https://assets2.lottiefiles.com/private_files/lf30_vfmaknbp.json'
pending='https://assets9.lottiefiles.com/packages/lf20_z5q31ue7.json'
declined='https://assets2.lottiefiles.com/packages/lf20_bc4ugzhr.json'


options = dict(loop=2, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

##-----------------------------------------------------------##--------------------------------------------###

def AdmissionsTab():

    return [

        html.Div([

            dbc.Row(
                dbc.Col([
                    dbc.Row([html.Div(id='change-lang-div'),
                             dcc.Dropdown(
                                 id='sales-gen-lang-dropdown',
                                 options=[
                                     {'label': 'English', 'value': 'En'},
                                     {'label': 'Arabic', 'value': 'Ar'}
                                 ],
                                 value='En',
                                 searchable=False,
                                 style={'width': '150px', 'height': '20px', }
                             )])
                ], width=12, className="d-flex justify-content-end")
            ),

        html.Div(
                            children = [
                                # Title and subtitle
                                html.Div(
                                    children = [
                                        html.H1(
                                            children = f"Admission Section/قسم القبول",
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
                    html.Label(['Select Year/ اختر السنة'],style={'font-weight': 'bold', 'color':'black'}),
                    dcc.Dropdown(
                        id="dropdown",
                        options=[{"label": x, "value": x} for x in year],
                        value=year[0],
                        clearable=False,
                        style={"width": "55%", "color":"black" },
                        className='dcc_compon'
                    ),
                ], className='create_container three columns'),


        html.Div([
                    html.Label(['Select Semester/حدد الفصل الدراسي'],style={'font-weight': 'bold', 'color':'black'}),
                    dcc.Dropdown(
                        id="dropdown2",
                        options=[{"label": x, "value": x} for x in AcTerm],
                        value=AcTerm[0],
                        clearable=False,
                        style={"width": "60%", },
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
                                html.H6(id='card_name1',
                                    children = "Total Applied/المجموع المطبق",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),

                                (Lottie(options=options, width='20%', height='20%', url=applied)),
                                # Total value
                                html.P(id="card_1",
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
                                    children = "Approved/موافقة",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),
                                (Lottie(options=options, width='20%', height='20%', url=approved)),
                                # Total value
                                html.P(id="card_2",
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
                        # (Column 3): Pending
                        html.Div(
                            children = [
                                # Title
                                html.H6(
                                    children = "Pending/قيد الانتظار",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),
                                (Lottie(options=options, width='20%', height='20%', url=pending)),
                                # Total recovered
                                html.P(id="card_3",
                                    children = "000",
                                    style = {
                                        "textAlign": "center",
                                        "color": "green",
                                        "fontSize": 40
                                    }
                                ),

                            ],
                            className = "card_container three columns"
                        ),
                        # (Column 4): Declined
                        html.Div(
                            children = [
                                # Title
                                html.H6(
                                    children = "Declined/رفض",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),
                                (Lottie(options=options, width='20%', height='20%', url=declined)),
                                # Total v
                                html.P(id="card_4",
                                    children = "000",
                                    style = {
                                        "textAlign": "center",
                                        "color": "#e55467",
                                        "fontSize": 40
                                    }
                                ),

                            ],
                            className = "card_container three columns"
                        )
                    ],
                    className = "row flex-display"
                ),







    html.Div([
        html.Div([
            dcc.Graph(id='the_graph2', config={
						"displayModeBar": "hover"
					})
        ], className="create_container six columns",),

        html.Div(
            children=[
                # Donut chart
                dcc.Graph(
                    id="pie_chart",
                    config={
                        "displayModeBar": "hover"
                    },

                )
            ],
            className="create_container three columns",
            style={
                "maxWidth": "450px"
            }
        ),
        html.Div([
            dcc.Graph(id='small-bar-graph',config={
						"displayModeBar": "hover"
					})
        ], className="create_container three columns",
            style={
                "maxWidth": "500px"
            })

    ],className = "row flex-display"),


html.Div([

    html.Div([
        dcc.Graph(id='the_graph1', config=dict(locale="fr"))
    ], className="create_container four columns"),

    html.Div([
        dcc.Graph(id='bar-graph',config={
						"displayModeBar": "hover"
					})
    ], className="create_container four columns"),


    html.Div(
        children=[
            # Donut chart
            dcc.Graph(
                id="pie_chart1",
                config={
                    "displayModeBar": "hover"
                }
            )
        ],
        className="create_container three columns",
        ## Width of the pie grapgh
        style={
            "maxWidth": "700px"
        }
    ),

],className = "row flex-display"),








        html.Div([
        html.Div([

        html.Label(['Select Country'],style={'font-weight': 'bold', 'color':'white'}),
                dcc.Dropdown(
                    id="w_countries",
                    multi=False,
                    searchable=True,
                    value="Pakistan",
                    placeholder="Select Country",
                    options=[{"label": c, "value": c} for c in (df["Country"].unique())],
                    className="dcc_compon"
                ),




        ###--------------------------------Values in the given card of Select Coountry-----------------------------####
        html.H6(
                                    children = "Exam Centres/مراكز الاختبارات",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),


            html.P(  				id="card_01",


                                    children = "12" ,
                                    className = "fix_label",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),

        ##------------------------------------------------------##-------------------------------------------------##
        html.H6(
                                    children = "Total Faculty/مجموع المدرسين",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),


            html.P(  				id="card_02",


                                    children = "50" ,
                                    className = "fix_label",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),

        ##---------------------------------------------##-----------------------------------------------##
        html.H6(
                                    children = "Total Students/مجموع الطلاب",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),


            html.P(  				id="card_03",


                                    children = "400" ,
                                    className = "fix_label",
                                    style = {
                                        "textAlign": "center",
                                        "color": "black"
                                    }
                                ),


            ],className="create_container three columns",style={
            "maxWidth": "900px"
        }),

            html.Div(
                children=[
                    dcc.Graph(
                        id="map_chart",
                        config={
                            "displayModeBar": "hover"
                        }
                    )
                ],
                className="create_container eight columns"
            )


            ],className = "row flex-display"),



        ],id = "mainContainer"),


]



##-----------BAR GRAPH FOR DEPARTMENT WISE ADMISSIONS--------------------------##

@app.callback(
    Output(component_id='bar-graph', component_property='figure'),
     Input("dropdown", "value"),
     Input("dropdown2", "value"))

def update_graph(year, term):
    mask= (df['Year']==year)  & (df['AcademicTerm']==term)


    dfg=df[mask].groupby('Department').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['Department'],
                y=dfg['AppID'],
                name="Department Wise",
                marker={
                    "color": "#DD4B39",

                },
                hoverinfo="text",

            ),


        ],


        "layout": go.Layout(
            title={
                "text": f"Number of applications by Department/عدد المتقدمين حسب القسم  ",
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
                "title": "<b>Number of applications/عدد المتقدمين</b>",
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
    Output(component_id='small-bar-graph', component_property='figure'),
     Input("dropdown", "value"),
     Input("dropdown2", "value"))

def update_graph(year, term):
    mask= (df['Year']==year)  & (df['AcademicTerm']==term)


    dfg=df[mask].groupby('Continent').count().reset_index()



    fig = {
        "data": [
            go.Bar(
                x=dfg['AppID'],
                y=dfg['Continent'],
                name="Continent Wise",
                orientation='h',
                marker={
                    "color": "rgb(219, 191, 249)",

                },
                hoverinfo="text",

            ),


        ],


        "layout": go.Layout(
            title={
                "text": f"Number of applications by Continent/عدد الطلبات حسب القارة  ",
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
                "title": "<b>Number of applications/عدد المتقدمين</b>",
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
                "title": "<b>Continent/القارة</b>",
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




#### -------------------------    Yearwise Department Enrollments Line Chart   ------------------------------ ###

@app.callback(
    Output(component_id='the_graph2', component_property='figure'),

	 Input("dropdown2", "value"))

def update_graph(year):

    dfg=df.groupby('Year').count().reset_index()

    categories = ['Jan, 2017', 'Jan,2018', 'Jan,2019', 'Jan,2020', 'Jan,2021']
    fig = {
        "data": [
            go.Scatter(
                x=categories,
                y=[1500, 1700, 1600, 2000, 2400],
                name="Department Wise",
                marker={'color':'rgb(186, 225, 247)'},

                fill='tozeroy',
                fillcolor='rgba(232, 255, 249, 0.6)'

            ),

        ],
        "layout": go.Layout(
            title={
                "text": "Year Wise Admissions/القبول السنوي ",
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
                "title": "<b>Number of applications/عدد المتقدمين</b>",
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






###-------------------Bar Chart by Age Group---------------------####

@app.callback(
    Output(component_id='the_graph1', component_property='figure'),
     Input("dropdown", "value"),

     Input("dropdown2", "value"))




def update_graph(year,  term):

    bins = [18, 25, 30, 35, 40]
    labels = ['18-24', '25-30', '30-35', '35-40']
    df['AgeGroup'] = pd.cut(df.Age, bins, labels=labels, include_lowest=True)

    mask = (df['Year'] == year)  & (df['AcademicTerm'] == term)
    dfg=df[mask].groupby('AgeGroup').count().reset_index()

    fig = {
        "data": [
            go.Bar(
                x=dfg['AgeGroup'],
                y=dfg['AppID'],
                name="Age group wise",
                orientation='v',
                marker={
                    "color": "#00A65A",

                },
                hoverinfo="text",

            ),

        ],
        "layout": go.Layout(
            title={
                "text": f"Number of applications by Age Group /عدد المتقدمين حسب الفئة العمرية ",
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
                "title": "<b>Age Group/الفئة العمرية</b>",
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
                "title": "<b>Total Applicants/إجمالي المتقدمين </b>",
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
    # Return the figure
    return fig

##----------------------------Doughnout Chart with Gender Proportion-------------------------------------------------------###

@app.callback(
    Output(component_id='pie_chart', component_property='figure'),
	Input("dropdown", "value"),
	Input("dropdown2", "value"))

def update_graph(year, term):


                            #make sure to make copy of the datafreame and never play with the original one.
	mask = (df['Year'] == year) & (df['AcademicTerm'] == term)
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
										"text": f"Gender Proportion /الجنس",
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
    Output(component_id='pie_chart1', component_property='figure'),
	Input("dropdown", "value"),
	Input("dropdown2", "value"))

def update_graph(year, term):


#make sure to make copy of the datafreame and never play with the original one.
	mask = (df['Year'] == year) & (df['AcademicTerm'] == term)
	labels = ['BS', 'MS', 'PHD']
	values = df[mask]['AcademicLevel'].value_counts()


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
										"text": f"Academic Level Proportion/نسبة المستوى الأكاديمي",
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

###---------------------------------Cards----------------------------------###


@app.callback(
    Output('card_1', 'children' ),
	Output('card_2', 'children' ),
	Output('card_3', 'children' ),
	Output('card_4', 'children' ),


	Input("dropdown", "value"),
	Input("dropdown2", "value"))



### There needs to be a condition if a value is not there in the column, it should ignore it and print the other values ###

def update_card(year, term):
	dfg= df.copy()
	mask = (dfg['Year'] == year)  & (dfg['AcademicTerm'] == term)


	apps=dfg[mask]['AppID'].count()

	approved= (dfg[mask]['Status'].value_counts().A)

	pending=dfg[mask]['Status'].value_counts().P

	declined=dfg[mask]['Status'].value_counts().D
	return apps, approved, pending, declined



@app.callback(
	Output(
		component_id = "map_chart",
		component_property = "figure"
	),
	Input(
		component_id = "w_countries",
		component_property = "value"
	)
)
def update_map(w_countries):
	# Filter the data
	dff = df.groupby(["Lat", "Long", "Country"])[["ExamCentre", "Scholarship"]].max().reset_index()
	dfg = dff[dff["Country"] == w_countries]
	# Get zoom
	if w_countries:
		zoom = 3
		zoom_lat = dict_of_locations[w_countries]["Lat"]
		zoom_long = dict_of_locations[w_countries]["Long"]
	# Build the figure
	fig = {
		"data": [
			go.Scattermapbox(
				lon = dfg["Long"],
				lat = dfg["Lat"],
				mode = "markers",
				marker = go.scattermapbox.Marker(

					colorscale = "HSV",
                    size=14,
					showscale = False,
					sizemode = "area",
					opacity = 0.5
				),
				hoverinfo = "text",
				hovertemplate = "<b>Country:</b> " + df["Country"].astype(str) + "<br>" +
								"<b>Exam Centres:</b> " + "<br>" +
								"<b> Total Faculty: </b>" + "<br>" +
								"<b> Total Students: </b>"+ "<extra></extra>"

			)
		],
		"layout": go.Layout(
			hovermode = "x",
			paper_bgcolor = "#1f2c56",
			plot_bgcolor = "#1f2c56",
			margin = {
				"r": 0,
				"l": 0,
				"t": 0,
				"b": 0
			},
			mapbox = dict(
				accesstoken = "pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw",   ##Very important without it map cannot be accessed
				center = go.layout.mapbox.Center(
					lat = zoom_lat,
					lon = zoom_long
				),
				style = "light",
				zoom = zoom
			),
			autosize = True
		)
	}
	# Return the figure
	return fig










if __name__ == '__main__':
    app.run_server(debug=True, port=1239, )