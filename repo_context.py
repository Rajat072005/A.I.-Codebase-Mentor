# IMPORTANT_FILES = {
#     "readme",
#     "package.json",
#     "requirements.txt",
#     "pyproject.toml",
#     "app.jsx",
#     "main.jsx",
#     "main.py",
#     "server.js",
#     "index.js",
#     "vite.config",
#     "next.config",
#     "vercel.json",
#     "docker-compose",
#     "dockerfile"
# }
# IMPORTANT_FOLDERS = {
#     "pages",
#     "routes",
#     "router",
#     "controllers",
#     "models",
#     "services",
#     "api",
#     "store",
#     "redux"
# }

IMPORTANT_SIGNALS = {
    "readme": 5,
    "package.json": 4,
    "requirements.txt": 4,
    "main": 4,
    "app": 4,
    "index": 4,
    "entry": 4,
    "vercel" : 4,
    "routes": 3,
    "router": 3,
    "pages": 3,
    "controllers": 3,
    "models": 3,
    "services": 3,
    "api": 3,
    "store": 3,
    "redux": 3,
    "config": 2,
    "utils": 1,
    "components": 1
}
def build_repo_context(files):
    repo_context_files = []
    
    for file in files :
        score = 0
        path = file.get("path", "").lower()
        
        for signal , weight in IMPORTANT_SIGNALS.items():
            if signal in path :
                score += weight
        
        if score>0 : 
            repo_context_files.append(
                {
                    "path" : file['path'],
                    "content" : file['content'],
                    "score" : score
                }
            )
    repo_context_files.sort(
        key= lambda x: x['score'],
        reverse=True
    )

    return repo_context_files[:15]
    
            