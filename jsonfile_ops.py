import json

with open('example_2.json','r') as fo:
    ex_data=json.load(fo)
    print(ex_data['quiz']['maths']['q1']['answer'])

data={
    'employee':[
        {
            'name':'Dinesh',
            'designation':'Manager',
            'location':'Pune',
            'contractor':False,
            'mobile':None
        }
    ]
}

with open('employee.json','w') as wfo:
    json.dump(data,wfo)