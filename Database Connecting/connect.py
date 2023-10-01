import mysql.connector
#query="CREATE TABLE login (log_id INT PRIMARY KEY AUTO_INCREMENT , name VARCHAR(20),email VARCHAR(20),password VARCHAR(20))";
#query="CREATE TABLE users (user_id INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(20),email VARCHAR(20))"
query="DROP TABLE log"
class TableCreation:
	def table(self,query):
		try:
			connection=mysql.connector.connect(host='localhost',database='testdb',user='root',password=None)
			cursor=connection.cursor()
			cursor.execute(query)
			print("Query Success !")
		except:
			print("Connection Failed !")
		finally:
			if connection.is_connected():
				connection.close()


