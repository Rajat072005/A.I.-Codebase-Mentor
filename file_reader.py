import os

Skip_Folders = {'.git' , 'node_modules' , '__pycache__' , "venv" , 'dist' , 'build'}
Allowed_extensions = [".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".css",
    ".html",
    ".json",
    ".md",
    ".txt"]
Ignore_Files = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml" , ".config.js" ,'robot.json'}
def read_repository(repo_path):
    all_files = []
    for root , dirs , files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in Skip_Folders]

        for file in files : 
            
            file_extension = os.path.splitext(file)[1]
            
            if file in Ignore_Files:
                continue
            if file_extension not in Allowed_extensions:
                continue

            file_path = os.path.join(root , file)

            try : 
                with open(file_path , "r" , encoding = "utf-8") as f:
                    content = f.read()

                    file_info = {
                        "path" : file_path,
                        "content" : content
                    }
                    all_files.append(file_info)
            except Exception as error:
                print(f"could not read {file_path}")
                print('error : ' , error)
    
    return all_files