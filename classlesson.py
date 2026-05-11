class classLesson:
 
    def __init__(self, classId,lessonId,teacherId):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.classId = classId
        self.teacherId = teacherId
        self.lessonId = lessonId

    @staticmethod
    def createClassLesson(obj):
        list = []
        for i in obj:
            list.append(classLesson(i[0], i[1], i[2]))
        return list