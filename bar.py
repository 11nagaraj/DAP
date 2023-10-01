import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\raghu\Desktop\p\annex4.csv")
df = pd.DataFrame(data)
Item_Code = df['Item Code'].head(10)
Item_Name = df["Item Name"].head(10)
explode = (0.1,0,0,0,0,0,0,0,0,0)
plt.pie(Item_Code,labels=Item_Name,explode=explode,shadow=True,autopct="%1.1f%%")
plt.show()

