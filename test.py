import utils
# repo_url = input("Provide Github Repository Url : ")

# repo_name = utils.extract_repo_name(repo_url)
# print(repo_name)

repos = utils.get_saved_repo()
utils.display_repositories(repos)