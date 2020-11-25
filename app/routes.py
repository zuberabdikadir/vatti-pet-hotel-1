from flask import request, redirect 
from app import app 

@app.route('/')
def index():
  return redirect('/index.html')


@app.route('/pets', methods=['GET', 'POST'])
def pets(): 
  if request.method == 'GET':
      #do stuff
      return #placeHolder 
  elif request.method == 'POST':
      return addPet(request.form)

def addPet(pet): 
  print('Checking in a new pet to the hotel!')
  curse = None
  response = None

  try:
    connection = get_db_conn() 
    cursor = connection.cursor()

    sql = "INSERT INTO pets (name, breed, color) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (pet['name'], pet['breed'], pet['color']))

    connection.commit() 
    response = {"msg": "Added your pet successfully to the hotel"}, 201 
  except psycopg2.Error as e: 
    print("Error when checking in your pet")
    response = {"msg": "Error checking in your pet, sorry!"}, 500 
  else: 
    if cursor: 
      cursor.close() 
  
  return response


