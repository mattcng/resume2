import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn import preprocessing
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

dash.register_page(__name__, title='Diabetes Knn Model', order=1)

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                html.H4('Explanatory k-NN plot'),
                dcc.Graph(id = "graph"),
                html.Label("Select number of neighbors:"),
                dcc.Slider(
                    id='slider-neighbors',
                    min=5, max=20, step=1, value=5,
                    marks={i: str(i) for i in range(5,21,5)}),
                html.Div(id='slider-neighbors-value'),  
                html.Label('Sample Size:'),
                dcc.Slider(
                    id='slider-sample-size',
                    min=10,
                    max=75000,
                    step=10,
                    value=25000,
                    marks={i: str(i) for i in range(0, 75001, 10000)}),
                html.Div(id='slider-sample-value'),  
                html.P('Red denotes a negative diabetes test, while Blue denotes a positive'),
                html.P('Made with plotly Dash')

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@callback(
    Output("graph", "figure"),
    [Input("slider-neighbors", "value"),
    Input("slider-sample-size", "value")]
)

def train_and_display_model(k, sample_size):
    diabetes_data = pd.read_csv("/Users/matphat/resume/Dash-by-Plotly/Good_to_Know/resume/diabetes.csv") 
    data_filtered = diabetes_data.drop(['gender', 'hypertension', 'heart_disease', 'smoking_history'], axis = 1)

    x_data = pd.get_dummies(data_filtered.drop(['diabetes'],axis=1))
    y_data = data_filtered['diabetes']

    MinMaxScaler = preprocessing.MinMaxScaler()
    X_data_minmax = MinMaxScaler.fit_transform(x_data)
    data_minmax = pd.DataFrame(X_data_minmax,columns=['age', 'bmi', 'HbA1c_level', 'blood_glucose_level'])
    
    X = data_minmax[['age','bmi']].values
    y = y_data

    xrange, yrange = build_range(X, y)
    xx, yy = np.meshgrid(xrange, yrange)
    test_input = np.c_[xx.ravel(), yy.ravel()]

    clf = KNeighborsClassifier(k, weights='uniform')

    clf.fit(X, y)
    Z = clf.predict_proba(test_input)[:, 1]
    Z = Z.reshape(xx.shape)

    # Downsample the data based on the selected sample size
    downsampled_indices = np.random.choice(range(len(X)), size=sample_size, replace=False)
    X_downsampled = X[downsampled_indices]
    y_downsampled = y[downsampled_indices]

    fig = build_figure(X_downsampled, y_downsampled, Z, xrange, yrange, sample_size)
    fig.update_layout(paper_bgcolor='LightSlateGray')

    return fig


# ############ HELPER FUNCTIONS ############
def build_range(X, y, mesh_size=.02, margin=.25):
    """
    Create an x range and a y range for building meshgrid
    """
    x_min = X[:, 0].min() - margin
    x_max = X[:, 0].max() + margin
    y_min = X[:, 1].min() - margin
    y_max = X[:, 1].max() + margin

    xrange = np.arange(x_min, x_max, mesh_size)
    yrange = np.arange(y_min, y_max, mesh_size)
    return xrange, yrange


def build_figure(X, y, Z, xrange, yrange, sample_size):
    #splitting data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(str), test_size=0.25, random_state=0)

    trace_specs = [
        [X_train, y_train, '0', 'Train', 'square', 'darkred'],
        [X_train, y_train, '1', 'Train', 'square', 'darkblue'],
        [X_test, y_test, '0', 'Test', 'circle', 'red'],
        [X_test, y_test, '1', 'Test', 'circle', 'blue']
    ]

    #figure graph
    fig = go.Figure(data=[
        go.Scatter(
            x=X[y==label, 0], y=X[y==label, 1],
            name=f'{split}, y={label}',
            mode='markers', marker_symbol=marker, marker_color = color,
        )
        for X, y, label, split, marker, color in trace_specs
            
    ])
    fig.update_traces(
        marker_size=12, marker_line_width=1.5
        # ,marker_color="seagreen"
    )

    #countour graph
    fig.add_trace(
        go.Contour(
            x=xrange, y=yrange, z=Z,
            showscale=False, colorscale='RdBu',
            opacity=0.75, name='Score', hoverinfo='skip'
        )
    )

    fig.update_layout(
        title="Diabetes based on BMI and Age",
        xaxis_title="Age",
        yaxis_title="BMI",
        legend_title="Point Classifications",
        height = 800,
        font=dict(
            size=16,
            color="RebeccaPurple"
    )
    
)
    return fig

