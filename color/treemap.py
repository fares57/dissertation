import pandas as pd             # Read data from excel
import matplotlib               # data viz
import matplotlib.pyplot as plt # data viz
import squarify                 # generate treemap
import plotly.express as px

df = pd.read_csv('colors-names-freqs.csv')

# print("Column headings:")
# print(df.columns)


# sizes=df['freqs']
# label=df['colors']
# colors=df['colors']
# squarify.plot(sizes, label=label, color=colors, alpha=0.5)
# plt.axis('off')
# plt.show()

print(len(df.hexnames))
print(len(df.colors))

hexnameslist = []
for hexname in df.hexnames:
    hexnameslist.append(hexname)

print(type(hexnameslist))



fig = px.treemap(df, path=['colors'],values='freqs', width=800, height=400)
fig.update_layout(
    treemapcolorway = list(hexnameslist),
    margin = dict(t=50, l=25, r=25, b=25))
fig.show()