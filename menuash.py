import os
#f_add="/etc/ansible/hosts"
users =['master','jobtracker','client','slave']
slaves_n=[]
#f =open("f_add","w")
slave=int(input("Enter number of slaves"))
rows,cols=(len(users)+(slave-1),3)
ip=[[0]*cols]*rows
for i in range (len(users) + (slave - 1)):
	
	if(i<3):
		
		j=0
		ip[i][j]=(input("Enter the I.P address of {}".format(users[i])))
		ip[i][j + 1]=(input("Enter the Name of {}".format(users[i])))
		ip[i][j + 2]=(input("Enter Password of the {}".format(users[i])))
	else:
		j=0
		ip[i][j]=(input("Enter the I.P address of {}".format(users[3])))
		ip[i][j + 1]=(input("Enter the Name of {}".format(users[3])))
		ip[i][j + 2]=(input("Enter Password of the {}".format(users[3])))


"""for i in range (len(users)):
	if i<3:
		f.write("[{}] \n {} ansible_user={} ansible_password={}".format(users[i],ip,usr_name,usr_pass))		 
	elif i==3:
		for j in range (slave_n):
			f.write("[{}] \n {} ansible_user={} ansible_password={}".format(slave_n[j],ip,usr_name,usr_pass))
"""


#f.close()
for i in range(rows):
	for j in range(cols):
		print(ip[i][j],end="  ")
	print("\n")
