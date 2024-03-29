import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('‎ '),
    dcc.Markdown('# __Matthew Nguyen__', style={'textAlign':'center'}),
    dcc.Markdown('Seattle, Washington | San Jose, California', style={'textAlign': 'center'}),
    dcc.Markdown('‎ '),

    dcc.Markdown('### __Professional Summary__', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('I am a highly motivated college student studying Information Systems in the Foster School of Business at the \n'
                 'University of Washington. Currently, I work in UW Research Compliance as a Data Analyst. \n \n'
                 "I love learning- some of my passions right now include becoming fluent in Chinese, web design, and DJing. I'm \n"
                 'looking for internship opportunities in a data/business intelligence position. \n \n'
                 'Feel free to reach out to me at mattcng9 at uw.edu for any potential openings.',
                 style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### __Skills__', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Python, Pandas, Seaborn, Skicit-learn 
            * HTML, Java, Dash, plotly
            * Word, Excel, Teams, Outlook
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Highly Personable 
            * Eager to Learn
            * Strong communication skills
            ''')
        ], width=3)
    ], justify='center'),

    dcc.Markdown('### __Work History__', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2022 to present', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('__Data Analyst__ \n'
                         '*University of Washington Research Compliance - Seattle, WA*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Conduct weekly analysis of ticket data Excel worksheets to determine team performances, generating updates\n'
                        'pushed to a public site and enhancing transparency in communicating the department’s total backlog status.'),
                html.Li('Archived hundreds of active and inactive budget files in compliance with University and State regulations and\n'
                        'categorized 800+ digitized files.'),
                html.Li('Trained under senior Systems and Data Analysts tracking inter-team performances and suggesting\n'
                        'improvements to processes during a University-wide transition to Workday')
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06 to 07/2022 and \n' 
                         '06 to 07/2023',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown("__Teacher's Assistant__ \n"
                         '*Saint Francis High School - Mountain View, CA*',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Personalized and tutored learning programs for students to help achieve mastery in target subjects.'),
                html.Li(
                    'Attended front-desk duties, directing parents and students in-person and on the phone to relevant departments and\n'
                    'answering general questions about the program.'),
                html.Li(
                    'Retrieved and compiled data from external programs into Excel to process/publish 300+ final student transcripts.')
            ])
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### __Experiences__', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2022 to present',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown("__Campus Involvement, Public Relations__ \n"
                         'Pi Kappa Alpha Fraternity - Seattle, WA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'phi phi'),
                html.Li(
                    'dyllan krouse'),
                html.Li(
                    'Paid dues (not)'),
                html.Li(
                    'LOL')
            ])
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### __Education__', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Expected Graduation 2025',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('B.A. Business Administration, Information Systems\n'
                         '*Minor in Informatics*\n'
                         'University of Washington, Seattle - Seattle, WA\n'
                         'Foster School of Business',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),

    
])
