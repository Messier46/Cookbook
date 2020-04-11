import mysql.connector
class lookup():
    """description of class"""
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="cookBook",
      passwd="none",
      database="cookbook-py"
    )
    
    