def get_test_score(answer_sheet, student_answers):
    num_of_question=len(answer_sheet)
    correct_count=0
    student_name= student_answers[0]
    student_answers.pop(0)
    for i in range(num_of_question):
        if answer_sheet[i] == student_answers[i]:
            correct_count+=1
    percentage=correct_count/num_of_question*100
    return student_name, percentage