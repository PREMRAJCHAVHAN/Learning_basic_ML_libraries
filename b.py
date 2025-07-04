import pandas as pd

#create a simple dataframe
data={
    'Name':['Alice','Bob','Charlie','premraj','pranay'],
    'Age':[25,30,35,21,32],
    'City':['New York','Paris','Londan','yavatmal','nanded'],
    'College':['Jdiet','Gcoey','Ycc','coep','Ramdeobaba']
}
df = pd.DataFrame(data)

#display the dataframe
print(df)

#access a column
print(df['Name'])

#basic statistics
print(df['Age'].mean())#Average age

#filter rows
print(df[df['Age'] > 28])
