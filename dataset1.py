import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marks = np.random.randint(0,101,size=(100,3))

df = pd.DataFrame(marks,columns =["MATHS","ENGLISH","SCIENCE"])

df["AVERAGE"]= df.mean(axis=1)
print(df.head(100))


#lineplot
plt.figure(figsize=(6,4))
plt.plot(df["AVERAGE"][:20],marker="o",linestyle="-")
plt.title("AVERAGE MARKS OF FIRST 20 STUDENTS")
plt.xlabel("students index")
plt.ylabel("Average marks")
plt.savefig('stock1.png')
plt.show()

#histogram
plt.figure(figsize=(6,4))
plt.hist(df["MATHS"],bins=10,edgecolor="black")
plt.title("HISTOGRAM OF MATHS MARKS")
plt.xlabel("MATHS marks")
plt.ylabel("no. of students")
plt.savefig('stock2.png')
plt.show()


#barchart
subject_avg=df[["MATHS","SCIENCE","ENGLISH"]].mean()
plt.figure(figsize=(6,4))
plt.bar(subject_avg.index,subject_avg.values,color=["skyblue","lightgreen","salmon"])
plt.title("AVERAGE MARKS PER SUBJECT")
plt.ylabel("marks")
plt.savefig('stock3.png')
plt.show()