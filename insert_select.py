import mysql.connector
import random
import time

try:
    connection = mysql.connector.connect(host='database-2-cluster.cluster-c3dgprehb0sn.ca-central-1.rds.amazonaws.com',
                                         database='accounts',
                                         user='admin',
                                         password='Admin1!!')

    mySql_insert_query = """INSERT INTO users (nickname, win, loss, draw, point) 
                           VALUES (%s, %s, %s, %s, %s) """

    records_to_insert = [('test' + str(random.random()), 1, 2, 3, 4)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    
    sql_select_Query = "select * from users order by userid Desc limit 3"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
    
    time.sleep(0.1)


except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")