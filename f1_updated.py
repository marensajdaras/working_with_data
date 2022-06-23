import pandas as pd 
o = pd.read_csv(r'C:\Users\User\Desktop\Github\code\e_card.csv')
print(o.describe())

# print first 5 records
print(o.head())


print('------------------------')
print('Read Header: ',end='\n')
print(o.columns)

print('----------------')
# we can sort values with sort_values()
o.sort_values(['Period','Group'],ascending=[1,0])
print(o.head())
print('We can see how it changes!')

# if we want to get some records that we will decide by ourselves  we can use iloc
print(o.iloc[1,4])

# we can transfer this csv file to the desire format with to_excel or to_csv
# i do not want to do it but for clarification the code will be just like these:
# o.to_excel('modified.xlsx',index=False)


# we can use also the function groupby()

print(o.groupby(['Period','Group']))


print('\n'*5)
print('Working with large amount of data: ')

new_o = o.DataFrame(columns=o.columns)

for i in o:
    results = i.groupby(['Period'])

    new_o = pd.concat([new_o, results])
    
print(new_o)

