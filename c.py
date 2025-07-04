import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#sample dataframe
df = pd.DataFrame({'Department':['Extc','Extc','Cse','Cse','Electrical','Electrical','Mechanical','Mechanical'],
                   'Student':['Premraj','aditi','lokesh','isha','harsha','gagan','pranay','gaurav'],
                   'Cgpa': [9.5,8.5,9.7,6.8,8.7,7.8,8.9,7.5]})
                   
                

#plot a boxplot
sns.boxplot(x='Department',y='Cgpa',data=df)
plt.show()