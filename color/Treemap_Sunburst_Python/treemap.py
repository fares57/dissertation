import plotly.express as px
import pandas as pd
import plotly

# Read Data from Excel
df = pd.read_excel('data.xlsx')

continent = df['Continent']
country = df['Country']
region = df['Region']
sales = df['Sales']
margin = df['Profit Margin %']
remark = df['Remark']

# Create Chart and store as figure [fig]
fig = px.treemap(df,
                path=[continent, region, country],
                values=sales,
                color=margin,
                color_continuous_scale=['red', 'yellow','green'],
                title='Sales/Profit Overview',
                hover_name=remark
                )

# Update/Change Layout
fig.update_layout(
                title_font_size=42,
                title_font_family='Arial'
                )

# Save Chart and Export to HTML
plotly.offline.plot(fig, filename='Chart.html')
