import json
 
# Creating a dictionary
Dictionary ={1:{}, 
             2:{},
             3:{}, 
             4:{},
             5:{}}

Dictionary[1] = {'name': 'Gulu',
                  'age': '5',
                  'type':'Cat',
                  'from': 'Jersey City',
                  #three items in order list are 'time','services','rate'
                  'orders':{1:['time','services','rate'],
                            2:['time','services','rate']}}
Dictionary[2] = {'name': 'Hulu',
                  'age': '5',
                  'type':'Cat',
                  'from': 'Jersey City',
                  'orders':{1:['time','services','rate'],
                            2:['time','services','rate']}}
Dictionary[3] = {'name': 'Maki',
                  'age': '2',
                  'type':'Dog',
                  'from': 'New York City',
                  'orders':{1:['time','services','rate'],
                            2:['time','services','rate']}}
Dictionary[4] = {'name': 'Petter',
                  'age': '10',
                  'type':'Bird',
                  'from': 'Hoboken',
                  'orders':{1:['time','services','rate'],
                            2:['time','services','rate']}}
Dictionary[5] = {'name': 'Amy',
                  'age': '4',
                  'type':'Cat',
                  'from': 'Hoboken',
                  'orders':{1:['time','services','rate'],
                            2:['time','services','rate']}}


with open('data.txt', 'w') as outfile:
    json.dump(Dictionary, outfile)
