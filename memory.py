import os
import json


def get_memory(repo_folder):
    memory_file = f"{repo_folder}/memory.json"

    if not os.path.exists(memory_file):
        return {
            "last_question": None,
            "last_question_type": None,
            "last_files": [],
            #"last_answer": None
        }

    with open(memory_file, "r", encoding="utf-8") as file:
        return json.load(file)


def update_memory(repo_folder, question, question_type, files): #,answer)
    memory_file = f"{repo_folder}/memory.json"

    memory_data = {
        "last_question": question,
        "last_question_type": question_type,
        "last_files": files,
        #"last_answer": answer
    }

    with open(memory_file, "w", encoding="utf-8") as file:
        json.dump(memory_data, file, indent=4)


# memory = {
#     "last_question" : None,
#     "last_question_type" : None,
#     "last_files" : [],
#     "last_answer" : None
# }

# def update_memory(question , question_type , files , answer):
#     memory["last_answer"] = answer
#     memory["last_files"] = files
#     memory["last_question"] = question
#     memory["last_question_type"] = question_type

# def get_memory():
#     return memory