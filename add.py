#  importing libraries
import mysql.connector as msq
#  Connecting to the database
con=msq.connector.connect(
  host="localhost",
  user="user",
  password="",
  database="data"
)
cursor=con.cursor()

#  Creating Table
cursor.execute('CREATE TABLE data (   \
                   RAM int(3),         \
                   storage int(4),     \
                   camera int(3),      \
                   battery int(5),     \
                   CPUCores int(2),    \
                   refreshRate int(3), \
                   range int(1)        \
                )')

#  Repeat until True is not True anymore   
while True:
    try:
        #Asking for inputs
        print('\n\n')
        print('Enter details of the phone-')
        RAM=int(input('RAM: '))
        storage=int(input('Storage: '))
        camera=int(input('camera: '))
        battery=int(input('battery: '))
        CPUCores=int(input('CPUCores: '))
        refreshRate=int(input('refreshRate: '))
        priceRange=int(input('priceRange (-1/1): '))
    except ValueError:
        continue
    except KeyboardInterrupt:
        #Commit to the database before closing the program
        con.commit()
        break
    
    #Insert Values into the table
    cursor.execute('INSERT INTO data VALUES (?,?,?,?,?,?,?)',
                   [RAM,storage,camera,battery,CPUCores,refreshRate,priceRange])