import sys
sys.path.append("..")
sys.path.append("../College_Urdu")
titleColor='black'
fontCol='#89B850'
bgCol='rgba(28, 166, 230,0.1)'
Colors=['#1a5a78','#247ba3','#2e98c9','#1ca6e6','#0fb3ff',]
fontColDark='#0e719e'
from dash import html

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from College_Arabic import Teachers_Section as teachers, Students_Section as students, Admissions as admissions, Scholarships as scholarships



from app import app


def ArabicPageLayout():
    return html.Div(
        style={'padding': '15px', 'width': '100%',
               'background-color': '#F8F8F8'},
        children=[
            dbc.Tabs(
                [
                    dbc.Tab(label="Admissions", tab_id="Admissions"),
                    dbc.Tab(label="Scholarships", tab_id="Scholarships"),
                    dbc.Tab(label="Students", tab_id="Students"),
                    dbc.Tab(label="Teachers", tab_id="Teachers"),
                ],
                id="sales-tabs",
                active_tab="Admissions",
            ),
            html.Div(id="sales-tab-content", className="p-0"),
            #

        ]  # MAIN HTML END,
        , className='container-fluid'
    )

# Main TABS CALLBACK


@app.callback(
    Output("sales-tab-content", "children"),
    [Input("sales-tabs", "active_tab")],
)
def render_tab_content(active_tab):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab:
        if active_tab == "Admissions":
            return admissions.AdmissionsTab()
        elif active_tab == "Scholarships":
            return scholarships.ScholarshipTab()
        elif active_tab == "Students":
            return students.StudentsLayout()
        elif active_tab == "Teachers":
            return teachers.TeachersLayout()
    return "No tab selected"
