import json
import pandas as pd
with open('C:\\Users\\User\\Desktop\\python\\c-rez11\\c-rez11\\ECO 685\\transaction_volume1.json') as f:
    data = json.load(f)
#df = pd.DataFrame(data['market-price'])
df = pd.DataFrame(data['estimated-transaction-volume-usd'])
print(df)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
#load_df = sns.load_dat(df)
sns.relplot(
    data=df
)
plt.show()