import mysql.connector
def conn():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="face_recognition")
  return mydb

def insertDB(Name,Age,Gender):
  mysql = conn()  
  mycursor = mysql.cursor()
  sql = "INSERT INTO user (Name, Age , Gender ) VALUES (%s, %s ,%s)"
  val = (Name,Age,Gender)
  mycursor.execute(sql, val)
  mysql.commit()  
def getIdUser(Name):
  mysql = conn()
  mycursor = mysql.cursor()
  sql = "SELECT Id FROM user WHERE Name = %s"
  val = (Name,)
  mycursor.execute(sql,val)
  myresult = mycursor.fetchall()
  for Id in myresult[0]:
    return Id
def getProfile(Id):
  mysql = conn()
  mycursor = mysql.cursor()
  sql = "SELECT * FROM user WHERE Id = %s"
  val = (Id,)
  mycursor.execute(sql,val)
  myresult = mycursor.fetchall()
  return myresult[0]
