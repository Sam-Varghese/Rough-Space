# Tuition Management
import string
import datetime
import mysql.connector
Program
# By:-
# Sam Varghese,Tejas
Mandloi, Anirudh Modi
# MYSQL CONNECTIVITY:-
con = mysql.connector.connect(host='localhost', user='root', passw
ord='root')
if con.is_connected():
print('Your Connection Is Successful :) ')
else:
print('Sorry Sir But An Unexpected Error Has Occurred,
Please Retry.')
cur = con.cursor()
# CREATING SQL DATABASE AND TABLE:-
cur.execute('create database if not exists tution_software')
cur.execute('use tution_software')
cur.execute('create table if not exists tuition(ROLL_NUMBER
int NOT NULL PRIMARY KEY, NAME varchar(15) NOT NULL, CLASS int
NOT NULL, SCHOOL varchar(15), PHONE_NUMBER
bigint, DATE_OF_ADMISSION varchar(10))')
# CREATING MENUS:-
exit_loop = False
22
while not exit_loop:
print('\n')
print("*"*80)
print('\t\t\t\t\t * MENU *')
print("*"*80)
print("\nPlease select the task which you want me to
perform: -\n\n
1)Registration\n\
2)Student's information of a specific class\n\
3)Get records of a specific student\n\
4)Delete records of a specific student\n\
5)Updating records of a specific student\n\
6)Exit") try: choice=int(input('\nYour choice please: - '))
if choice not in range(1, 7):
choice=int(input('\nIncorrect choice, please
enter a valid choice: - '))
except Exception:
choice=int(input('\nIncorrect choice, please enter a
valid choice: - '))
if choice == 1:  # Registration Section
# Getting the name of student:
stu_name=string.capwords(input('\nPlease enter the
name of the student who want to join tuition: '))
# Getting the class of student:
try:
stu_class=int(input('Please enter the class of
'+stu_name+': '))
23
if stu_class > 12 or stu_class <= 0:  # Raising custom
error if class > 12 or <=0
raise ValueError('Invalid class number')
except Exception as e:
print('ERROR:-', e)
print('\nSorry to say, but an invalid class has
been entered so kindly rectify this data')
stu_class=int(input('Please enter the class of
'+stu_name+': '))
print('\n')
# Getting the roll number of the student:
try:
stu_roll_no=int(input('Please enter the roll
number of '+stu_name+': '))
except Exception as e:
print('ERROR:-', e)
print('\nSorry to say but an invalid roll number
has been entered so kindly rectify this data.')
stu_roll_no=int(input('Please enter the roll
number of '+stu_name+': '))
print('\n')
# Getting the school name of the student
stu_school=string.capwords(input('Please enter the
school name of '+stu_name+': '))
try:
stu_ph_no=int(input('Please enter the contact
number of '+stu_name+': '))
except Exception as e:
print('ERROR:-', e)
print('\nSorry but an invalid contact number has
been entered so kindly rectify this data.')
24
stu_ph_no=int(input('Please enter the contact
number of '+stu_name+': '))
print('\n')
# Generating current date
stu_admission_date=datetime.datetime.now().strftime('%d-%m-%Y'
)
# Making SQL Query
query="insert into tution
values({}, '{}', {}, '{}', {}, '{}')".format(stu_roll_no, stu_name, s
tu_class, stu_school, stu_ph_no, stu_admission_date)
# Inserting data to MySQL Database
try:
cur.execute(query)
con.commit()
except mysql.connector.IntegrityError:  # Handling
repeated roll number exception
cur.execute('select * from tution where
ROLL_NUMBER= % s'% stu_roll_no)  # Showing about the student with
that roll no
data=cur.fetchall()
print('\nSorry but this roll number has been used
for '+data[0][1]+' also.')
print('\nHence please re-enter a valid roll
number.')
stu_roll_no=int(input('Please re-enter the roll
number of '+stu_name+': '))
25
query="insert into tution
values({}, '{}', {}, '{}', {}, '{}')".format(stu_roll_no, stu_name, s
tu_class, stu_school, stu_ph_no, stu_admission_date)
cur.execute(query)
con.commit()
print('\nName successfully registered')
elif choice == 2:  # Getting record of a specific class
try:  # Getting class from the user
classs=int(input('\nPlease enter the class whose
records you want to display: '))
except Exception as e:
print('ERROR:-', e)
print('\nSorry but an invalid class has been
entered so kindly rectify this data')
classs=int(input('\nPlease enter the class whose
records you want to display: '))
print('\n')
# Creating SQL Query
query='select * from tution where
CLASS={}'.format(classs)
# Getting data from SQL Database
cur.execute(query)
data=cur.fetchall()
# Showing data
print('\nPrinting data of class ', classs, ':-')
print('\n')
count=1
for i in data:
26
print(count, ')Roll Number:-', i[0], ', \nName: -', i[1], ' , \nClass: -', i[2],
      ' ,\nSchool Name:-', i[3], ', \nContact Number: -', i[4], ', \nDate of Admission: -', i[5])
print('\n')
count += 1
elif choice == 3:  # Getting records of a specific student
try:
rn=input("\nPlease enter the roll number of the
student.: ")
query="SELECT * from tution WHERE ROLL_NUMBER="+rn
cur.execute(query)
data=cur.fetchall()
print(data)
c=cur.rowcount
if c == 0:
rn=int(input("\nSorry, but there is no student
in this tution by this roll number so please re-enter the
correct roll
number: -"))
cur.execute(query)
data=cur.fetchall()
print("\nShowing records of the student:-\n")
print('Name:- ', data[0][1], '\nClass: -
',data[0][2],'\nRoll Number: - ',data[0][0],'\nSchool Name: -
',data[0][3],\
 2 7
'\nContact information: -
',data[0][4],'\nDate of Admission: - ', data[0][5])
except Exception as e:
print('\nERROR:-', e)
print("\nPLEASE TRY AGAIN SOMETHING WENT
WRONG...")
elif choice == 4:  # Deleting records of a student
try:
dr=input("\nPlease enter the roll number of the
student whose records you want to delete: - ")
query="DELETE from tution WHERE ROLL_NUMBER="+dr
cur.execute(query)
con.commit()
c=cur.rowcount
if c > 0:
print("\nData successfully deleted.")
else:
dr=input('Roll number. '+dr + ' not found, please enter a valid roll number: - ')
query="DELETE from tution WHERE
ROLL_NUMBER="+dr
cur.execute(query)
con.commit()
print("\nData successfully deleted.")
except Exception as e:
print('\nERROR: ', e)
print("PLEASE TRY AGAIN SOMETHING WENT WRONG...")
28
elif choice == 5:  # Modifying Data
try:
roll_no=input('\nEnter roll number whose data
you want to update: - ')
query= 'SELECT * FROM tution WHERE
ROLL_NUMBER='+roll_no
cur.execute(query)
record=cur.fetchall()
c=cur.rowcount
if c == 0:
print('Student with ', roll_no, 'does not
exist! Please enter valid roll number.')
else:
sname=record[0][1]
sclass=record[0][2]
sschool=record[0][3]
scontact=record[0][4]
print('Roll Number:- ', record[0][0], '\nName: -
',sname,'\nClass: - ',sclass,'\nRoll Number: -
',record[0][0],'\nSchool Name: - ',sschool,\
'\nContact information: - ',scontact,'\nDate
of Admission: - ', record[0][5])
print('\nEnter respective values to modify.
Press enter for no change\n')
change=input('\nEnter new name of the student:
')
if len(change) > 0:
sname=change
change=input('Enter new class of the student:
')
if len(change) > 0:
29
change=int(change)
if change > 12:
raise ValueError("Invalid class
number")
sclass=change
change=input('Enter name of new school of the
student: ')
if len(change) > 0:
sschool=change
change=input('Enter new contact of the
student: ')
if len(change) > 0:
change=int(change)
scontact=change
query="UPDATE tution set NAME="+"'"+sname+"'" + ", CLASS=" + \
    str(sclass)+" , SCHOOL="+"'"+sschool+"'" + ", PHONE_NUMBER=" + \
        str(scontact)+" WHERE ROLL_NUMBER="+roll_no
cur.execute(query)
print('\nData successfully updated\n')
except Exception as e:
print('\nERROR: ', e)
print("PLEASE TRY AGAIN SOMETHING WENT WRONG...")
elif choice == 6:  # Exit
print("\nThank you. HAVE A NICE DAY!!")
con.close()
exit_loop=True
