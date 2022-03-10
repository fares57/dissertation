import pandas as pd             # Read data from excel
import matplotlib               # data viz
import matplotlib.pyplot as plt # data viz
import squarify                 # generate treemap
import plotly.express as px

df = pd.read_excel('colors-names-freqs.xlsx', 'astellas')

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

for index, color in enumerate(df.colors):
    print(color,":",df.freqs[index],":", df.hexnames[index])


fig = px.treemap(df, path=['colors'], values='freqs', labels = 'colors', width=800, height=400)
fig.update_traces(textinfo='label+value')
# fig.update_traces(count = 'branches')
fig.update_layout(
    treemapcolorway = list(hexnameslist),
    margin = dict(t=10, l=10, r=10, b=10))
fig.show()