import pandas as pd             # Read data from excel
import matplotlib               # data viz
import matplotlib.pyplot as plt # data viz
import squarify                 # generate treemap

df = pd.read_excel('colors-names-freqs.xlsx')

print("Column headings:")
print(df.columns)


sizes=df['freqs']
label=""
colors=df['colors']
squarify.plot(sizes, label=label, color=colors, alpha=0.5)
plt.axis('off')
plt.show()