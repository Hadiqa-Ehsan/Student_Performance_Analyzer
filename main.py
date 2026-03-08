import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":["Ali","Sara","Ahmed","Zara"],
    "Marks": [75,90,85,60]        
}
df=pd.DataFrame(data)
print("Student Dataset:")
print(df)

average_marks=df["Marks"].mean()
highest_marks=df["Marks"].max()

print("Average Marks:",average_marks)
print("Highest marks:",highest_marks)

top_student=df.loc[df["Marks"].idxmax()]
print("Top Student:")
print(top_student)

plt.bar(df["Name"], df["Marks"])
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()