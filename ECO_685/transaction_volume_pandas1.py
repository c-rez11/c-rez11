
import json
import pandas as pd
with open('C:\\Users\\cresnick\\OneDrive - Epic\\Desktop\\python projects\\Udemy courses\\new_era\\c-rez11\\ECO_685\\transaction_volume1.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)