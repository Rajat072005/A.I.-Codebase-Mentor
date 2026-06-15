import utils
repo_url = input("Provide Github Repository Url : ")

repo_name = utils.extract_repo_name(repo_url)
print(repo_name)