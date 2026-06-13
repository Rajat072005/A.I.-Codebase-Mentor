def build_repo_context(files):
    repo_context = []
    for file in files :
        path = file.get("path", "").lower()
        
        if(
            "readme" in path
            or "package.json" in path
            or "app.jsx" in path
            or "main.jsx" in path
            or "vite.config" in path
            or 'eslint.config.js' in path
            or "vercel.json" in path
        ):
            repo_context.append(file)

    return repo_context
            