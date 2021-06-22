import pymysql

conn = pymysql.connect(host="database-2-cluster.cluster-c3dgprehb0sn.ca-central-1.rds.amazonaws.com", user="admin", password='Admin1!!', db="accounts")

try:
    curs = conn.cursor()
    sql = "select * from users order by userid Desc limit 3"
    curs.execute(sql)
    rows = curs.fetchall()
    
    for row in rows:
        print(row)
        
finally:
    conn.close()
