import sqlite3
from Login_Page import *
from Diet_Menu import *
from Main_Menu import *
from FindDietMenu import *
from FindWorkoutMenu import *
from Workout_Menu import *
from ShowDietsPage import *

#Creating the main three tables in the database.
def create_users():
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE credentials (
              username text PRIMARY KEY,
              hashpassword int,
              name text,
              age int,
              gender text,
              height int,
              weight int)""")
    
    c.execute("""CREATE TABLE Diets(
              dietID int PRIMARY KEY,
              diet text)""")
    
    c.execute("""CREATE TABLE Workouts(
              workoutID int PRIMARY KEY,
              workout text)""")

    conn.commit()
    conn.close()

#Creating the UserDiet table.
def create_UserDiet():
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE UserDiet(
              username text,
              dietID int,
              FOREIGN KEY(dietID)
              REFERENCES Diets(dietID),
              FOREIGN KEY(username)
              REFERENCES credentials(username))""")
    
    conn.commit()
    conn.close()

#Creating the UserWorkout table.
def create_UserWorkout():
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE UserWorkout(
              username text,
              workoutID int,
              FOREIGN KEY(workoutID)
              REFERENCES Workouts(workoutID),
              FOREIGN KEY(username)
              REFERENCES credentials(username))""")
    
    conn.commit()
    conn.close()

#Creating the UserProfile table.
def create_UserProfile():
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE UserProfile(
              username text,
              bodyfat FLOAT,
              BMI float,
              FOREIGN KEY(username)
              REFERENCES credentials(username))""")
    
    conn.commit()
    conn.close()

#Registering a new user.
def register_users(username_entry, password_entry,name,age,gender,height,weight):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""INSERT INTO credentials VALUES(:username,:password,:name,:age,:gender,:height,:weight)""",
              {"username":username_entry,
              "password":password_entry,
              "name":name,
              "age":age,
              "gender":gender,
              "height":height,
              "weight":weight})
    
    conn.commit()
    conn.close()

#Used to get username from credentials.  
def Username_get(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT username
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f
    except:
        pass
    
    conn.commit()
    conn.close()

#Used to get hashedpass from credentials.
def getHashedPassword(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT hashpassword
                    FROM credentials
                    WHERE username=(?)""",
                    (username,))
        data = c.fetchall()

        return data[0][0]
    except:
        pass

#Used to get username as a string from credentials.
def Username_get2(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT username
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Used to get name from credentials.
def getName(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT name
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Used to get height from credentials.
def getHeight(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT height
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Used to get weight from credentials.
def getWeight(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT weight
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Used to get age from credentials.
def getAge(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT age
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Used to get gender from credentials.
def getGender(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()
    
    try:
        c.execute("""SELECT gender
                    FROM credentials
                    WHERE username=(?)""",
                    (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Updating info into credentials.
def updateInfo(username, name, age, gender, height, weight):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""UPDATE credentials SET
                 name = :name,
                 height = :height,
                 weight = :weight,
                 age = :age,
                 gender = :gender
                
                WHERE username = :username""",

                {"name":name,
                 "height":height,
                 "weight":weight,
                 "age":age,
                 "gender":gender,
                 "username":username})
    
    conn.commit()
    conn.close()

#Updating UserProfile.
def UpdateUserProfile(username,bodyfat,BMI):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""UPDATE userProfile SET
                 BMI = :BMI,
                 bodyfat = :bodyfat
                 
                 WHERE username = :username""",
                 
                 {"username":username,
                  "BMI":BMI,
                  "bodyfat":bodyfat})

    conn.commit()
    conn.close()

#Adding diet plans into the Diets table.
def addDietPlan(dietID, diet):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""INSERT OR IGNORE INTO Diets VALUES(:dietID, :diet)""",
              {"dietID":dietID,
               "diet":diet})
    
    conn.commit()
    conn.close()

#Getting diet plan from Diets.
def getDietPlan(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT diet
                     FROM Diets
                     WHERE dietID=(?)""",
                 (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Adding dietID to UserDiet
def addDietID(username,dietID):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""INSERT INTO userDiet VALUES(:username, :dietID)""",
              {"username":username,
               "dietID":dietID})

    conn.commit()
    conn.close()

#Deleting diet from UserDiet for a specific given username.
def deleteSavedDiet(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""DELETE FROM UserDiet WHERE username=(?)""",
              (username,))
    
    conn.commit()
    conn.close()

#Getting dietID from UserDiet for a specific given username.
def getDietID(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT dietID
                     FROM UserDiet
                     WHERE username=(?)""",
                 (username,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Adding workout to the Workouts table.
def addWorkoutPlan(workoutID, workout):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""INSERT OR IGNORE INTO Workouts VALUES(:workoutID, :workout)""",
              {"workoutID":workoutID,
               "workout":workout})
    
    conn.commit()
    conn.close()

#Getting workout from Workouts.
def getWorkoutPlan(data):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT workout
                     FROM Workouts
                     WHERE workoutID=(?)""",
                 (data,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass
    
    conn.commit()
    conn.close()

#Addinng WorkoutID to UserWorkout.
def addWorkoutID(username,workoutID):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""INSERT INTO userWorkout VALUES(:username, :workoutID)""",
              {"username":username,
               "workoutID":workoutID})

    conn.commit()
    conn.close()

#Deleting workout for UserWorkout for a specific given username.
def deleteSavedWorkout(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""DELETE FROM UserWorkout WHERE username=(?)""",
              (username,))
    
    conn.commit()
    conn.close()

#Getting workout ID from UserWorkout for a specific given username.
def getWorkoutID(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT workoutID
                     FROM UserWorkout
                     WHERE username=(?)""",
                 (username,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Adding details to UserProfile for a specific given username.
def addtoUserProfile(username,bodyfat,BMI):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""INSERT INTO userProfile VALUES(:username,:bodyfat,:BMI)""",
              {"username":username,
               "BMI":BMI,
               "bodyfat":bodyfat})
    
    conn.commit()
    conn.close()

#Updating weight for a user in the table credentials.
def updateWeight(username, weight):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""UPDATE credentials SET
                 weight = :weight
              
                 WHERE username = :username""",
                 {"username":username,
                  "weight":weight})

    conn.commit()
    conn.close()

#Deleting UserProfile.
def deleteUserProfile(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    c.execute("""DELETE FROM UserProfile WHERE username=(?)""",
              (username,))
    
    conn.commit()
    conn.close()

#Getting saved diet for a specific given username.
#Uses INNER JOIN.
def getSavedDietPlan(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT Diets.diet
                     FROM credentials
                     INNER JOIN UserDiet ON credentials.username = UserDiet.username
                     INNER JOIN Diets ON UserDiet.dietID = Diets.dietID
                     WHERE credentials.username=(?)""",
                 (username,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Getting saved workout for a specific given username. 
#Uses INNER JOIN.
def getSavedWorkoutPlan(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT Workouts.workout
                     FROM credentials
                     INNER JOIN UserWorkout ON credentials.username = UserWorkout.username
                     INNER JOIN Workouts ON UserWorkout.workoutID = Workouts.workoutID
                     WHERE credentials.username=(?)""",
                 (username,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Getting average BMI from all of the users in the UserProfile table. 
#Uses Aggregate SQL.
def getAvgBMI():
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT avg(BMI)
                     FROM userProfile""")
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Getting average bodyfat from all of the users in the UserProfile table. 
#Uses Aggregate SQL.
def getAvgBodyfat():
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT avg(bodyfat)
                     FROM userProfile""")
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Getting BMI for a specific given username.
def getBMI(username):
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT BMI
                     FROM userProfile
                     WHERE username = (?)""",
                     (username,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()

#Getting bodyfat for a specific given username.
def getBodyfat(username):
    
    conn = sqlite3.connect("credentials_book.db")
    c = conn.cursor()

    try:
        c.execute("""SELECT bodyfat
                     FROM userProfile
                     WHERE username = (?)""",
                     (username,))
        f = c.fetchall()
        return f[0][0]
    except:
        pass

    conn.commit()
    conn.close()