import pandas as pd
import plotly.express as px
import dash

df_ = pd.read_csv('reviews.csv')

app = dash.Dash(__name__)

app.layout = dash.html.Div([
    dash.html.H4('Beer Ratings for Different Styles of Beer Filtered by ABV'),
    dash.dcc.Graph(id="scatter-plot"),
    dash.html.P("Filter by ABV:"),
    dash.dcc.RangeSlider(
        id='range-slider',
        min=0, max=18, step=1,
        marks={0: '0', 2: '2', 4: '4', 6: '6', 8: '8', 10: '10', 12: '12', 14: '14', 16: '16', 18: '18'},
        value=[2, 16]
    ),
])


@app.callback(
    dash.Output("scatter-plot", "figure"),
    dash.Input("range-slider", "value"))
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
