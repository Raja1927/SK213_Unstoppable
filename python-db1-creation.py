import pymysql.connections
connection = pymysql.connect(host='localhost', user='root', password='raja')
mycursor=connection.cursor()
mycursor.execute("Create database face_reco_fill ")

