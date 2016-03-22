import random   # importing random to generate random numbers later

ques = {}   # a dictionary to hold questions (key: an integer, value: question)
ans = {}    # a dictionary to hold answers (key: an integer, value: answer)

def loadQuiz():
    """
    This function loads the quiz's data (i.e, questions and answers) from a
    file and then puts to dictionaries with key as a serial numbers (
    integers) and the question as value and same key as answer's keys and
    value as the answers.
    :return: updates the dictionaries
    """
    print("Loading from file")
    filename = "quizData1.txt"
    file = open(filename)
    mainKey = 0 # initializing key integer
    next(file)  # skipping first line
    for line in file:   # going through each line and updating dictionaries
        line.strip()
        lineList = line.split()
        anEmpty = ""
        if lineList[0] is not "-":
            mainKey += 1    # updating key (integer)
            ques[mainKey] = anEmpty
            # first item in the list is ignored, example: "1."
            for i in range(1, len(lineList)):
                ques[mainKey] = ques[mainKey] + lineList[i] + " "
        else:
            ans[mainKey] = anEmpty
            # first item in the list is ignored, which is "-"
            if len(lineList) > 2:   # if answer is more than one word
                for i in range(1, len(lineList)):
                    ans[mainKey] += lineList[i] + " "
            else:
                # if answer is just one word
                ans[mainKey] = lineList[1]

def check(user_answer, qu, count):
    """
    Checks if the given answer matches with the correct one.
    Recursive if wrong answer is given.
    After 3 wrong answers, the correct answer is revealed.
    :param user_answer: user's input answer
    :param qu: key or question number
    :param count: count of how many times a user inputs an answer
    :return: doesn't return anything, just prints or recurse appropriately
    """
    correct_answer = ans[qu].strip().lower()
    count += 1
    if len(user_answer) is len(correct_answer) and user_answer in \
            correct_answer:
            print("Correct answer\n")
    else:
        if (count is 3):  # correct answer revealed after 3 wrong answers
            print("Thanks for trying, correct answer is " + correct_answer +
                  "\n")
            return
        user_answer = input("Wrong answer, try again: ")
        while len(user_answer) is 0:
            # making sure user gives an answer not just an empty lin (an ENTER)
            user_answer = input("Enter answer: ")
        check(user_answer, qu, count)

def main():
    """
    Main function that shows user the question according to the randomly
    generated keys (integers) and takes user's inputs and checks the answers.
    :return:
    """
    print ("Welcome to Quiz")

    loadQuiz()  #loading quiz
    totalQuestions = len(ques)
    num_questions = int(input("How many questions? (less than " + str(
        totalQuestions) + "): "))
    #making sure user gives a number greater than 0 and less than total questions
    while (num_questions > totalQuestions or num_questions <= 0):
        num_questions = int(input("Enter how many questions? "))

    # a list holding randomly generated numbers
    num_random = random.sample(range(1, totalQuestions+1), num_questions)

    #print(num_random)
    for qu in num_random:   # doing action as per the generated random numbers
        user_answer = input(ques[qu] + "\nAnswer: ")
        while len(user_answer) is 0:
            # making sure user gives an answer not just an empty lin (an ENTER)
            user_answer = input("Enter answer: ")
        tryCount = 0
        check(user_answer, qu, tryCount)

if __name__ == '__main__':
    main()
    print("Done!")
