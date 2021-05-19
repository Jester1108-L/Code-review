from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

admin = {"username":"admin","password":"admin"}
inv = [("SC001","sports pants","20","36.50"),
		("SC002","sports shirt","30","37.50"),
		("SC003","sports socks","40","38.50")
]
db_connection = mysql.connector.connect(
		host= "localhost",
		user= "root",
		passwd= "Computer@123",
		auth_plugin='mysql_native_password'
		)
db_cursor = db_connection.cursor()
	
	
def createDatabase():
	db_connection = mysql.connector.connect(
		host= "localhost",
		user= "root",
		passwd= "Computer@123",
		auth_plugin='mysql_native_password'
		)
	db_cursor = db_connection.cursor()
	try:
		db_cursor.execute("CREATE DATABASE inventoryDB")
	except:
		db_connection = mysql.connector.connect(
			host= "localhost",
			user= "root",
			passwd= "Computer@123",
			auth_plugin='mysql_native_password',
			database="inventoryDB"
			)
		db_cursor = db_connection.cursor()
	try:
		db_cursor.execute("CREATE TABLE stock1 (stockCode VARCHAR(20), stockName VARCHAR(255), quantity VARCHAR(255), price VARCHAR(255))")
		for stock in inv:
			insertDatabase("stock1", stock)
	except:
		pass
	

def loadDatabase(table):
	db_connection = mysql.connector.connect(
		host= "localhost",
		user= "root",
		passwd= "Computer@123",
		auth_plugin='mysql_native_password',
		database="inventoryDB"
		)
	db_cursor = db_connection.cursor()
	out = []
	sql = "SELECT * FROM "+ table
	db_cursor.execute(sql)
	for x in db_cursor:
		out.append(x)
	return out
	
def insertDatabase(table, val):
	db_connection = mysql.connector.connect(
			host= "localhost",
			user= "root",
			passwd= "Computer@123",
			auth_plugin='mysql_native_password',
			database="inventoryDB"
			)
	db_cursor = db_connection.cursor()
	sql = "INSERT INTO " + table + " (stockCode,stockName,quantity,price) VALUES " + val
	db_cursor.execute(sql)
	db_connection.commit()
	
def deleteDatabase(table,val):
	db_connection = mysql.connector.connect(
			host= "localhost",
			user= "root",
			passwd= "Computer@123",
			auth_plugin='mysql_native_password',
			database="inventoryDB"
			)
	db_cursor = db_connection.cursor()
	sql = "DELETE FROM " + table + " WHERE stockCode = 'SC003'"
	db_cursor.execute(sql)
	db_connection.commit()
	
def updateDatabase(table, val1, val2, val3):
	db_connection = mysql.connector.connect(
			host= "localhost",
			user= "root",
			passwd= "Computer@123",
			auth_plugin='mysql_native_password',
			database="inventoryDB"
			)
	db_cursor = db_connection.cursor()
	sql = "UPDATE " + table + " SET " + val1 + " = " + val2 + " WHERE stockCode = " + val3
	db_cursor.execute(sql)
	db_connection.commit()

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method == "POST":
		username = request.form["log_username"]
		password = request.form["log_password"]
		createDatabase()
		out = loadDatabase("stock1")
		if admin["username"] == username and admin["password"] == password:
			return render_template("main.html", db = out, user = "admin")
		else:
			return render_template("main.html", db = out, user = username)
	else:
		return render_template("home.html")

@app.route("/insert")
def insertpage():
	return render_template("change.html", change="insert")
	
@app.route("/delete")
def deletepage():
	return render_template("change.html", change="delete")
	
@app.route("/update")
def updatepage():
	return render_template("change.html", change="update")

@app.route("/change1", methods=["POST","GET"])
def insertChange():
	out = loadDatabase("stock1")
	if request.method == "POST":
		table = "stock1"
		#table = request.form["inTable"]
		#code = request.form["inCode"]
		#product = request.form["inName"]
		#quantity = request.form["inQuantity"]
		#price = request.form["inPrice"]
		#temp = "("+code+","+product+","+quantity+","+price+")"
		insertDatabase(table, "(CS004,shoes,25,2000)")
	return render_template("main.html", db = out, user="admin")

@app.route("/change2", methods=["POST","GET"])
def deleteChange():
	out = loadDatabase("stock1")
	if request.method == "POST":
		table = request.form["table"]
		code = request.form["inCode"]
		deleteDatabase(table, code)
	return render_template("main.html", db = out, user="admin")
	
@app.route("/change3", methods=["POST","GET"])
def updateChange():
	out = loadDatabase("stock1")
	if request.method == "POST":
		table = request.form["table"]
		code = request.form["inCode"]
		field = request.form["field"]
		value = request.form["value"]
		insertDatabase(table, field, value, code)
	return render_template("main.html", db = out, user="admin")

if __name__ == "__main__":
	app.run(debug=True, port=5000)
