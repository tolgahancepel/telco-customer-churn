import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

def get_navbar():
    PLOTLY_LOGO = "/assets/cepel-logo.png"

    nav_item_home = dbc.NavItem(dbc.NavLink("Home", href="#"))
    nav_item_about = dbc.NavItem(dbc.NavLink("About", href="#"))
    nav_item_github = dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/tolgahancepel/telco-customer-churn"))

    logo = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        ],
                        align="center",
                        no_gutters=True,
                    ),
                    href="https://plot.ly",
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            #nav_item_home,
                            #nav_item_about,
                            nav_item_github
                        ], className="ml-auto", navbar=True
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ]
        ),
        color="primary",
        dark=True,
        className="mb-5",
    )

    return logo