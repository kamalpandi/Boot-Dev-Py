def get_test_score(answer_sheet, student_answers):
    num_of_question=len(answer_sheet)
    correct_count=0
    print(num_of_question)
    for i in range(num_of_question):
        if answer_sheet[i] == student_answers[i]:
            correct_count+=1
    percentage=correct_count/num_of_question*100
    return percentage