inport pandas as pd 
filename = input()

#reading through file
dataF = pd.read_csv(filename , sep=',');
# creating dataframe which contains unique values in dataF['queries']
queries =  dataF['query'].unique()

#now encoding each query
dataF['tag'] = 0

def newdata(dataF , queries):
    listq  = queries.tolist()
    for i in range(len(dataF)):
        dataF['tag'][i] = listq.index(dataF['query'][i])
    return dataF
    
#////////////
data = newdata(dataF,queries)
#drop query column from data
del data['query']
# finally convert df to .csv


data.to_csv (r'C:\Users\admin\Desktop\export_dataframe.csv', index = False, header=True)

