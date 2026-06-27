memory = {
    "last_question" : None,
    "last_question_type" : None,
    "last_files" : [],
    "last_answer" : None
}

def update_memory(question , question_type , files , answer):
    memory["last_answer"] = answer
    memory["last_files"] = files
    memory["last_question"] = question
    memory["last_question_type"] = question_type

def get_memory():
    return memory