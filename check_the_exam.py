# check the exam kata
# https://www.codewars.com/kata/5a3dd29055519e23ec000074

def is_answer_correct(correct_answer, student_answer):
    return correct_answer == student_answer
 
def check_exam(correct_answers,student_answers):
    score = 0
    for correct_answer, student_answer in zip(correct_answers, student_answers):
        if student_answer:
            if is_answer_correct(correct_answer, student_answer):
                score += 4
            else:     
                score -= 1
    return score if score >= 0 else 0
        
    
