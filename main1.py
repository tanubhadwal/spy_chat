from spy import spy
spy_list=[]

spy_list.append(spy)

spy['name']='tanu'
spy['salutation']='Mr'
spy['age']='22'
spy['rating']='4.5'
spy['is_online']=True
spy_list.append(spy)

print(len(spy_list))

# select name only..///
print(spy_list[0]['name'])


#lets create a function.......////////////
