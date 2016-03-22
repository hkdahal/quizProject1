import random

ques = {}
ans = {}

def loadQuiz():
    print("Loading from file")
    filename = "quizData1.txt"
    file = open(filename)
    mainKey = 0
    next(file)
    for line in file:
        line.strip()
        lineList = line.split()
        anEmpty = ""
        if lineList[0] is not "-":
            mainKey += 1
            ques[mainKey] = anEmpty
            for i in range(1, len(lineList)):
                ques[mainKey] = ques[mainKey] + lineList[i] + " "
        else:
            ans[mainKey] = anEmpty
            if len(lineList) > 2:
                for i in range(1, len(lineList)):
                    ans[mainKey] += lineList[i] + " "
            else:
                ans[mainKey] = lineList[1]

def main():

    print ("Welcome to Quiz")

    loadQuiz()
    totalQuestions = len(ques)
    num_questions = int(input("How many questions? "))
    while (num_questions > totalQuestions or num_questions <= 0):
        num_questions = int(input("Enter how many questions? "))

    num_random = random.sample(range(1, totalQuestions+1), num_questions)

    print(num_random)
    for qu in num_random:
        user_answer = input(ques[qu] + "\nAnswer: ")
        while len(user_answer) is 0:
            user_answer = input("Enter answer: ")
        tryCount = 0
        check(user_answer, qu, tryCount)

def check(user_answer, qu, count):
    correct_answer = ans[qu].strip().lower()
    count += 1
    if len(user_answer) is len(correct_answer) and user_answer in \
            correct_answer:
            print("Correct answer\n")
    else:
        if (count is 3):
            print("Thanks for trying, correct answer is " + correct_answer +
                  "\n")
            return
        user_answer = input("Wrong answer, try again: ")
        check(user_answer, qu, count)

if __name__ == '__main__':
    main()
    print("Done!")
