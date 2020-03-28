import chart_studio.plotly as py
import plotly.graph_objects as go
import pandas as pd

df_fires = pd.read_csv('./df_hist_fires.csv')
# df_fires.head(5)
fig = go.Figure(go.Scatter(x=df_fires.Year, y=df_fires.State, text=df_fires.Name, mode='markers', name='2007'))
fig.update_xaxes(title_text='Year')
fig.update_yaxes(title_text='State')

py.iplot(fig, filename='pandas-multiple-scatter')