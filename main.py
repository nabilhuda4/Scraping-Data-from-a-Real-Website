from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/QS_World_University_Rankings'

page = requests.get(url)


soup = BeautifulSoup(page.text, 'html.parser')


caption = soup.find_all('caption')[1:]

cap = [captions.text.strip() for captions in caption]

data1 = soup.find_all('table')[1]
A1 = data1.find_all('th')
main1 = [title.text.strip() for title in A1]

column_data = data1.find_all('tr')

data2 = soup.find_all('table')[2]
A2 = data2.find_all('th')
main2 = [title.text.strip() for title in A2]

column_data1 = data2.find_all('tr')

data3 = soup.find_all('table')[3]
A3 = data3.find_all('th')
main3 = [title.text.strip() for title in A3]

column_data2 = data3.find_all('tr')


data4 = soup.find_all('table')[4]
A4 = data4.find_all('th')
main4 = [title.text.strip() for title in A4]


column_data3 = data4.find_all('tr')


data5 = soup.find_all('table')[5]
A5 = data5.find_all('th')
main5 = [title.text.strip() for title in A5]


column_data4 = data5.find_all('tr')


data6 = soup.find_all('table')[6]
A6 = data6.find_all('th')
main6 = [title.text.strip() for title in A6]


column_data5 = data6.find_all('tr')


data7 = soup.find_all('table')[7]
A7 = data7.find_all('th')
main7 = [title.text.strip() for title in A7]


column_data6 = data7.find_all('tr')


data8 = soup.find_all('table')[8]
A8 = data8.find_all('th')
main8 = [title.text.strip() for title in A8]


column_data7 = data8.find_all('tr')


import pandas as pd


from IPython.display import display


df8 = pd.DataFrame(columns = main8)


for row in column_data7[1:]:
    row_data8 = row.find_all('td')
    individual_row_data8 = [data.text.strip() for data in row_data8]
    length = len(df8)
    df8.loc[length] = individual_row_data8
    #print(individual_row_data8)

    

df7 = pd.DataFrame(columns = main7)



for row in column_data6[1:]:
    row_data7 = row.find_all('td')
    individual_row_data7 = [data.text.strip() for data in row_data7]
    length = len(df7)
    df7.loc[length] = individual_row_data7
    #print(individual_row_data7)
    


    df6 = pd.DataFrame(columns = main6) 
    


    for row in column_data5[1:]:
     row_data6 = row.find_all('td')
     individual_row_data6 = [data.text.strip() for data in row_data6]
     length = len(df6)
     df6.loc[length] = individual_row_data6
    #print(individual_row_data6)
    


    df5 = pd.DataFrame(columns = main5)
    



    for row in column_data4[1:]:
     row_data5 = row.find_all('td')
     individual_row_data5 = [data.text.strip() for data in row_data5]
     length = len(df5)
     df5.loc[length] = individual_row_data5
    #print(individual_row_data5)
   


    df4 = pd.DataFrame(columns = main4)
   


    for row in column_data3[1:]:
     row_data4 = row.find_all('td')
     individual_row_data4 = [data.text.strip() for data in row_data4]
     length = len(df4)
     df4.loc[length] = individual_row_data4
    #print(individual_row_data4)
    



    df3 = pd.DataFrame(columns = main3)
    


    for row in column_data2[1:]:
     row_data3 = row.find_all('td')
     individual_row_data3 = [data.text.strip() for data in row_data3]
     length = len(df3)
     df3.loc[length] = individual_row_data3
    #print(individual_row_data3)
    




    df2 = pd.DataFrame(columns = main2)
    



    for row in column_data1[1:]:
     row_data2 = row.find_all('td')
     individual_row_data2 = [data.text.strip() for data in row_data2]
     length = len(df2)
     df2.loc[length] = individual_row_data2
    #print(individual_row_data2)
    




    df1 = pd.DataFrame(columns = main1,)
   



    for row in column_data[1:]:
     row_data1 = row.find_all('td')
     individual_row_data1 = [data.text.strip() for data in row_data1]
     length = len(df1)
     df1.loc[length] = individual_row_data1
    #print(individual_row_data1)


  





print('Welcome to my small "Scraping Data from a Real Website" Project')
print('This project will give you all the information related to "QS World University Rankings"')
ans = input("If you want all data related to this subject enter Y if not then enter N to exit: ").upper()

#display(df1,df2,df3,df4,df5,df6,df7,df8)


if ans == "Y":

     df1.to_csv('QS World University Rankings Global Top 10.csv', index=False)
     df2.to_csv('QS World University Rankings Arab Region Top 10.csv', index=False)
     df3.to_csv('QS World University Rankings Asia Top 10.csv', index=False)
     df4.to_csv('QS World University Rankings Latin America Top 10.csv', index=False)
     df5.to_csv('QS World University Rankings Europe Top 10.csv', index=False)
     df6.to_csv('Categories of QS World University Rankings by Faculty and Subject.csv', index=False)
     df7.to_csv('QS Best Student Cities Top 10.csv', index=False)
     df8.to_csv('QS World University Rankings Sustainability Top 10.csv', index=False)

     print("Thanks for using my project, the data should be in the directory you ran this file!")
else:
  print("Thank you for checking this out!")


  #the creator is Nabil Al Huda