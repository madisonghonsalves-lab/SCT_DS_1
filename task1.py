import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_267553.csv",
    skiprows=4
)

data = df[['Country Name', '2024']]

data = data.dropna()

top10 = data.sort_values('2024', ascending=False).head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top10['Country Name'],
    top10['2024']
)

plt.title('Top 10 Countries by Female Population (2024)')
plt.xlabel('Country')
plt.ylabel('Female Population')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('output.png')

plt.show()