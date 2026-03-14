import pandas as pd
import random
from datetime import datetime, timedelta

rows = 50000

products = ["Laptop","Phone","Tablet","Headphones","Monitor","Keyboard","Mouse","Printer"]
categories = ["Electronics","Accessories"]
regions = ["North","South","East","West"]

data = []

start = datetime(2023,1,1)

for i in range(rows):

    order_id = 1000 + i
    product = random.choice(products)
    category = random.choice(categories)
    region = random.choice(regions)

    sales = random.randint(1000,80000)
    quantity = random.randint(1,5)

    order_date = start + timedelta(days=random.randint(0,365))

    data.append([order_id,product,category,region,sales,quantity,order_date])

df = pd.DataFrame(data,columns=[
"Order_ID","Product","Category","Region","Sales","Quantity","Order_Date"
])

df.to_excel("sales_dataset_50000.xlsx",index=False)

print("Dataset created successfully!")