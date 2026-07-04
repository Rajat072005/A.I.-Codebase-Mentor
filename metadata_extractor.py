def detect_module_type(path):
    normalized_path = path.replace("\\" , "/").lower()
    path_parts = normalized_path.split("/")
    file_name = path_parts[-1]
    file_type = file_name.split(".")[-1]

    module_keywords = {
        "pages": "page",
        "components": "component",
        "hooks": "hook",
        "features": "state",
        "store": "state",
        "context": "state",
        "api": "api",
        "services": "service",
        "utils": "utility",
        "styles": "style",
        "styling": "style",
        "middlewares": "backend"
    }

    for part in path_parts:
        if part in module_keywords:
            return module_keywords[part] , file_type
    
    return "general", file_type