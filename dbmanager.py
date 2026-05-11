import mysql.connector
from datetime import datetime
from connection import connection
from student import Student
from teacher import teacher
from Class import Class
from classlesson import classLesson 

class DBManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def getStudentById(self,id):
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            print(obj)
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print(f"HATA",err)
        pass

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getTeacherById(self,id):
        sql = "SELECT * FROM student WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            print(obj)
            return Student.createStudent(obj)
        except mysql.connector.Error as err:
            print(f"HATA",err)
        pass


    def getStudentsByClassId(self, classid):
        sql = "SELECT * FROM student WHERE classId = %s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            return Student.createStudent(obj)  # ← return + Student objesi ekle
        except mysql.connector.Error as err:
            print(f"HATA", err)

    def getLessonsByClassId(self, classid):
        sql = "SELECT class.name,lesson.name, CONCAT(teacher.name,'',teacher.surname) as teacherName FROM classlesson JOIN class ON classlesson.classId = class.id JOIN lesson ON classlesson.lessonId = lesson.id JOIN teacher ON classlesson.teacherId = teacher.id WHERE classlesson.classId = %s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"HATA", err)

    def addStudent(self,student:Student):
         sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,classId) VALUES (%s,%s,%s,%s,%s,%s)"
         value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid)
         self.cursor.execute(sql,value)

         try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
         except mysql.connector.Error as err:
            print('hata:', err)
         
    def addorEditStudent(self,student:Student):
        pass

    def editStudent(self,student:Student):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classId=%s where id=%s"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def addTeacher(self,teacher:teacher):
         sql = "INSERT INTO teacher(Branch,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)"
         value = (teacher.branch,teacher.name, teacher.surname,teacher.birthdate,teacher.gender)
         self.cursor.execute(sql,value)

         try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
         except mysql.connector.Error as err:
            print('hata:', err)

    def editTeacher(self,teacher:teacher):
        sql = "UPDATE teacher SET Branch = %s ,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        value = (teacher.branch,teacher.name, teacher.surname,teacher.birthdate,teacher.gender,teacher.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def deleteStudent(self,studentid):
        sql = "DELETE FROM student WHERE id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err)


    def __del__(self):
        self.connection.close()
        print("db silindi")
