def detect_target_modules(question):
    target_modules = set()
    lowercased_question = question.lower()
    routing_rules = {
    "page": ["page", "component"],
    "component": ["component"],
    "style": ["style", "component"],
    "theme": ["style", "component"],
    "css": ["style"],
    "state": ["state", "hook", "component"],
    "redux": ["state"],
    "store": ["state"],
    "hook": ["hook"],
    "api": ["api", "service"],
    "service": ["service", "api"],
    "authentication": ["api", "service"],
    "login": ["page", "component", "api"]
    }

    for keyword, modules in routing_rules.items():
        if keyword in lowercased_question:
            for module in modules :
                target_modules.add(module)

    return target_modules
