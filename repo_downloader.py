from git import Repo

def download_repo(repo_url , folder_name):
    try : 
        Repo.clone_from(repo_url , folder_name)

        print("repo downloaded successfully")

    except Exception as error : 
        print("something went wrong : " + str(error))