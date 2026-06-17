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

IMPORTANT_KEYWORDS = {
    "readme",
    "package.json",
    "requirements.txt",
    "pyproject.toml",
    "app.jsx",
    "main.jsx",
    "main.py",
    "server.js",
    "index.js",
    "vite.config",
    "next.config",
    "vercel.json",
    "docker-compose",
    "dockerfile",
    "pages",
    "routes",
    "router",
    "controllers",
    "models",
    "services",
    "api",
    "store",
    "redux"
}
def build_repo_context(files):
    repo_context = []
    
    for file in files :
        path = file.get("path", "").lower()
        
        
        for keyword in IMPORTANT_KEYWORDS:
            if keyword in path:
                repo_context.append(file)
                break
        

    return repo_context
            