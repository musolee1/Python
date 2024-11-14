# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

# q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
# q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
# q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

# sorular = [q1,q2,q3]

# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatır.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)

import random

class Question:
    def __init__(self, text, choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("Girdiğiniz ifade şıklar içinde yer almıyor.")
        return self.answer == answer
        
class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex +1}: {question.text}")

        for q in question.choices:
            print("-" + q)
        
        answer = input("cevabınız: " )
        if (question.checkAnswer(answer)):
            self.score += 1

        self.questionIndex +=1
        self.loadQuestion()
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def displayScore(self):
        puan = 100 /len(self.questions)
        toplamPuan = round(self.score * puan)
        print(f"{len(self.questions)} sorudan {self.score} adet soruyu doğru cevapladınız. Seni çok seviyorum canım aşkımmmm!!")
        print("Score: ",toplamPuan)
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"{questionNumber}/{totalQuestion}".center(20,'*'))

q1 = Question("En iyi Programlama dili nedir?",["python","c#","java","dart"],"python")
q2 = Question("İlk buluşmamızı hatırlıyor musun? O an ne hissettin?",["c#","dart","python","java"],"python")
q3 = Question("Senin için romantik bir gece nasıl görünürdü?",["dart","python","java","c#"],"python")


sorular = [q1,q2,q3]


quiz = Quiz(sorular)

print(quiz.loadQuestion())