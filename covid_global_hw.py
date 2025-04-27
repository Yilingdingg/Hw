import matplotlib.pyplot as plt
import pandas as pd

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("WHO-COVID-19-global-data.csv")
print(data.head())
print(data.info())

data.columns = ('Date','Country_code', 'Country', 'WHO_region', 'New_cases', 'Cumulative_cases','New_deaths','Cumulative_deaths')

data['Date'] = data['Date'].astype('datetime64[ns]')
print(data.info())

nl_data = data[data['Country_code']=='US']
print(nl_data.info())

time_series = nl_data.groupby('Date').sum()
print(time_series.head())
print(time_series.index)

x = time_series.index

figure_1 = go.Figure( data=[
    go.Bar( name = "Cumulative Cases during COVID-19", y = nl_data['Cumulative_cases'], x = x,  orientation = 'v'),
    go.Bar( name = "Cumulative Deaths during COVID-19", y = nl_data['Cumulative_deaths'], x = x, orientation = 'v')
])
figure_1.update_layout(title = 'Covid in the US', height = 800, barmode = "stack")
figure_1.write_html('figure_222.html', auto_open = True)