from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app

from College_Arabic import Teachers_Section, Scholarships, Students_Section, Admissions

from College_Arabic import ArabicPage as AP



boxStyle = {
    'height': '200px',
    'display': 'flex',
    'width': '300px',
    'margin': '10px',
    'align-items': 'center',
    'text-align': 'center',
    'justify-content': 'center',
    'background-color': '#f2f2f2',  # rgb(255,25,25)
    'color': '#008080',
    'font-size': '50px',
    'font-weight': 'bold',
    'border-radius': '10px',

}


def getMainLayout():
    return [
        #
        # Section 1
        #
        html.Section(
            [
                #
                # ROW
                #
                html.Div(
                    [


                        #
                        # CARD 1
                        #
                        html.Div(
                            [

                                dcc.Link(html.Div(

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-book-open"),
                                                    html.H4("Arabic College",
                                                            className="card__heading")

                                                ],
                                                className="card__title card__title--1"
                                            ),

                                        ],
                                        className="card__side card__side--front-1"
                                    ),
                                    className="card"
                                ), href="/College_Arabic/ArabicPage")

                            ],
                            className="col-1-of-3"
                        ),
                        #
                        # CARD 2
                        #
                        html.Div(
                            [

                                dcc.Link(html.Div(

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-graduation-cap"),
                                                    html.H4("Urdu College",
                                                            className="card__heading")

                                                ],
                                                className="card__title card__title--1"
                                            ),

                                        ],
                                        className="card__side card__side--front-2"
                                    ),
                                    className="card"
                                ), href="/College_Arabic/ArabicPage")

                            ],
                            className="col-1-of-3"
                        ),
                        #
                        # CARD 2
                        #
                        html.Div(
                            [

                                dcc.Link(html.Div(

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-book-open"),
                                                    html.H4("French College",
                                                            className="card__heading")

                                                ],
                                                className="card__title card__title--1"
                                            ),

                                        ],
                                        className="card__side card__side--front-3"
                                    ),
                                    className="card"
                                ), href="/College_Arabic/ArabicPage")

                            ],
                            className="col-1-of-3"
                        ),

                    ],  # ROW
                    className="row-card"
                ),
            ],
            className="section-plans"
        ),
        #
        # Section 2
        #
        html.Section(
            [
                #
                # ROW
                #
                html.Div(
                    [
                        #
                        # CARD 3
                        #
                        html.Div(
                            [

                                dcc.Link(html.Div(

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-graduation-cap"),
                                                    html.H4("English College",
                                                            className="card__heading")

                                                ],
                                                className="card__title card__title--1"
                                            ),

                                        ],
                                        className="card__side card__side--front-4"
                                    ),
                                    className="card"
                                ), href="/College_Arabic/ArabicPage")
                            ],
                            className="col-1-of-3"
                        ),

                        html.Div(
                            [

                                dcc.Link(html.Div(

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.I(
                                                        className="fas fa-book-open"),
                                                    html.H4("ALL Colleges",
                                                            className="card__heading")

                                                ],
                                                className="card__title card__title--1"
                                            ),

                                        ],
                                        className="card__side card__side--front-0"
                                    ),
                                    className="card"
                                ), href="/College_Arabic/ArabicPage")

                            ],
                            className="col-1-of-3"
                        ),

                    ],  # ROW
                    className="row-card"
                ),
            ],
            className="section-plans"
        ),
    ]



app.layout = html.Div([

    html.Div(

        children=[
            # Title and subtitle
            html.Img(
                src=app.get_asset_url("kiu_logo.png"),

                style={
                    "margin-bottom": "0",
                    'height': '200px',
                    'width': '300px',
                    'margin-bottom': '25px'
                }
            )
        ],
        className="six column",
        id='logo'
    ),
    dbc.Navbar(
        [
            dbc.Row(
                [
                    dbc.Col(html.I(className="fas fa-chart-bar fa-4x", style={'color': 'white'})),
                    dbc.Col(dbc.NavbarBrand("Bi Dashboard", className="ml-1",
                                            style={'font-size': '22px', 'font-weight': 'bold'})),
                ],
                align="center",
                no_gutters=True,
            ),

        ],
        color="#45d364",
        dark=True,
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    # ORIGINAL LAYOUT
    print(pathname)
    if pathname == '/College_Arabic/ArabicPage':
        return html.Div(AP.ArabicPageLayout())

    if pathname == '/':
        # if not data.empty:
        #     return dummyLayout()
        # else:
        return getMainLayout()

    elif pathname == '/Scholarships':
        print('GETTING INSIDE CUSTOMERS PAGE')
        return html.Div(Scholarships)
    elif pathname == '/Students_Section':
        return html.Div(Students_Section)
    elif pathname == '/Teachers_Section':
        return html.Div(Teachers_Section)




if __name__ == '__main__':
    app.run_server(host='localhost', port='6017', debug=True)
# host='0.0.0.0',