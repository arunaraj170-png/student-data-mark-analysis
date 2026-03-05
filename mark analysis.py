import pandas as pd

data = {
    "Name": ["Arun", "Riya", "Kumar"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())
print(df)
