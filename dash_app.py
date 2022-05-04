import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df_ = pd.read_csv('reviews.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Beer Ratings for Different Styles of Beer Filtered by ABV'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filter by ABV:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=18, step=1,
        marks={0: '0', 2: '2', 4: '4', 6: '6', 8: '8', 10: '10', 12: '12', 14: '14', 16: '16', 18: '18'},
        value=[2, 16]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"),
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    df = df_
    low, high = slider_range
    mask = (df['ABV'] > low) & (df['ABV'] < high)

    fig = px.scatter(
        df[mask], x="ABV", y="Review_Rating",
        color="Style", size='Review_Rating',
        hover_data=['Name'])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)