journal = {
    'Petrov': [
        {'date': '31.03.2019', 'is_attended': True}
    ]
}



def change_status(student,date):
    if (student in journal):
    	for i in range(0,len(journal[student])):
    		if journal[student][i]['date'] is date:
    			journal[student][i]['is_attended'] = False
    		else:
    			journal[student].append({'date': date, 'is_attended': True})
    else:
    	journal[student]= [{'date': date, 'is_attended': True}]
    print(journal)




change_status('Petrov', '31.03.2019')
change_status('Ivanov', '31.03.2019')
change_status('Ivanov', '01.04.2019')
