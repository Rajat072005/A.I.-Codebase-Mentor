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
        path = file["path"].lower()

        if "main" in path:
            summary = "Main application entry point file."

        elif "app" in path:
            summary = "Core application component."

        elif "package.json" in path:
            summary = "Project dependencies and scripts configuration."

        elif "vercel" in path:
            summary = "Deployment configuration file."

        elif "routes" in path:
            summary = "Defines API routes."

        elif "controllers" in path:
            summary = "Contains business logic for handling requests."

        elif "models" in path:
            summary = "Database models and schemas."

        elif "readme" in path:
            summary = "Project overview and setup instructions."

        else:
            summary = f"Important project file: {file['path']}"
        if score>0 : 
            repo_context_files.append(
                {
                    "path" : file['path'],
                    "summary" : summary,
                    "content" : file['content'],
                    "score" : score
                }
            )
    repo_context_files.sort(
        key= lambda x: x['score'],
        reverse=True
    )

    return repo_context_files[:15]
    
            