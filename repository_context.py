def get_repository_context(files):
    important_files = []
    important_keywords = [
        "package.json",
        "readme",
        "vite.config",
        "main.jsx",
        "app.jsx",
        "eslint.config.js",
        "vercel.json"
    ]
    for file in files:
        path = file['path'].lower()
        for keyword in important_keywords :
            if keyword in path:
                important_files.append(
                    file
                )
                break
    return important_files