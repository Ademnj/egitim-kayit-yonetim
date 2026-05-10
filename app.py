from dbmanager import DBManager
import datetime
from student import Student

class App:
    def __init__(self):
        self.db = DBManager()

    def initApp(self):
        msg ="****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış (E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.displayAddStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            elif islem == "7" or islem == "E" or islem == "Ç":
                break
            else:
                print("Hatalı Seçim Yaptınız")
                

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci ID Giriniz:"))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci ID Giriniz:"))

        student = self.db.getStudentById(studentid)

        student[0].name = input("name: ") or student[0].name
        student[0].surname = input("surname: ") or student[0].surname
        student[0].gender = input("Cinsiyet(E/K): ") or student[0].gender
        student[0].classid = input("Sınıf: ") or student[0].classid

        year = int(input("Yıl: ")) or student[0].birthdate.year
        month = int(input("Ay: ")) or student[0].birthdate.month
        day = int(input("Gün: ")) or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])




    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Hangi Sınıf:"))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        for index,std in enumerate(students):
            print(f"{std.id}-{std.name} {std.surname}")

        return classid
    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.id}:{c.name}")

    def displayAddStudent(self):
        self.displayClasses()
        classid = int(input("Hangi Sınıf:"))
        number = input("Numara Giriniz")
        name = input("Ad giriniz:")
        surname = input("Soyad giriniz:")
        year = int(input("Yıl giriniz:"))
        month = int(input("Ay giriniz:"))
        day = int(input("Gün giriniz:"))
        birthdate = datetime.date(year, month, day)
        gender = input("Cinsiyet Giriniz(E/K): ")

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
app = App()
app.initApp()