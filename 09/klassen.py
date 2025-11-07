class Exam: 
    def __init__(self, examiner, subject, course_number): 
        self.examiner = examiner
        self.sunject = subject 
        self.course_number = course_number 
        self.participants = []
        self.results = []
    
    def get_number_of_participants(self):
        return len(self.participants)

    def add_participant(self, participant):
        self.participants.append(participant)

    """a) Methode set_Result erzeugen"""  
    def set_result(self, participant, result):
        self.results.append((participant, result))


class WrittenExam(Exam):
    TYPE = "Klausur"  # Art der Prüfung als Konstante der Klasse

    def __init__(self, examiner, subject, course_number, date, time, duration):
        super().__init__(examiner, subject, course_number)
        self.date = date
        self.time = time
        self.duration = duration

pruefung = Exam("Sabrina","BWL","WDS25B1")

pruefung.participants =  [
    "Lovelace, Ada",
    "Turing, Alan",
    "Hopper, Grace",
    "von Neumann, John",
    "Knuth, Donald"
]

pruefung.results =  [
    ("Lovelace, Ada", 1.6),
    ("Turing, Alan", 2.0),
    ("Hopper, Grace", 3.3),
    ("von Neumann, John", 3.6),
    ("Knuth, Donald", 5.0),
]


pruefung.set_result("Knuth, Donald Jr.", 2.0)
print(pruefung.results)