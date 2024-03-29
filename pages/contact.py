import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# **Matthew C Nguyen**', className='mt-3'),
    dcc.Markdown('### *Data Analyst*', className='mb-5'),
    dcc.Markdown('### **Personal info**', style={'color':'gray'}),
    dcc.Markdown('Address', style=green_text),
    dcc.Markdown('Seattle, Washington | San Jose, California'),
    dcc.Markdown('Phone Number', style=green_text),
    dcc.Markdown('669-252 dash 4532'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('mattcng9 at uw.edu'),
    dcc.Markdown('LinkedIn', style=green_text),
    dcc.Markdown('[https://www.linkedin.com/in/mattcng/](https://www.linkedin.com/in/mattcng/)', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')