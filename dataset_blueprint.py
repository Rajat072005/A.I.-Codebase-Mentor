FEATURES = [

    "authentication",
    "login",
    "signup",
    "payment",
    "cart",
    "orders",
    "profile",
    "dashboard",
    "notifications",
    "search",
    "routing",
    "middleware",
    "API",
    "database",
    "cache",
    "state management",
    "configuration",
    "session management",
    "authorization",
    "request handling"

]
OBJECT = [
    "project",
    "repository",
    "application",
    "system",
    "codebase",
    "software",
    "platform"
]
QUESTION_TEMPLATES = {

    # ==========================
    # OVERVIEW
    # ==========================

    "overview" : [

        {
            "pattern": "What does this {object} do?",
        
            "variables": {
                "object": [
                    "project",
                    "repository",
                    "application",
                    "system",
                    "codebase",
                    "software",
                    "platform"
                ]
            }  ,
        
            "category": "purpose"
        },
        
        {
            "pattern": "Give me an overview of this {object}.",
        
            "variables": {
                "object": OBJECT
            },
        
            "category": "Overview"
        },
        
        {
            "pattern": "Explain this {object}.",
        
            "variables": {
                "object": OBJECT
            },
        
            "category": "explanation"
        },

        {
            

            "pattern": "Summarize this {object}.",

            "variables": {
                "object": OBJECT
            },

            "category": "summary"
        },
        
        {
            "pattern": "What problem does this {object} solve?",

            "variables": {
                "object": OBJECT
            },
            "category": "problem"
        },
        
        {
            "pattern": "Introduce this {object}?",
        
            "variables": {
                "object": OBJECT
            },
        
            "category": "introduction"
        },

        {
            "pattern": "What is the purpose of this {object}?",

            "variables": {
                "object": OBJECT
            },
            "category": "goal"
        },

        {
            "pattern": "Describe this {object}.",

            "variables": {
                "object": OBJECT
            },
            "category": "description"
        },

        {
            "pattern": "Explain this {object} at a high level.",

            "variables": {
                "object": OBJECT
            },
            "category": "high_level"
        },

        {
            "pattern": "Help me understand this {object}.",

            "variables": {
                "object": OBJECT
            },
            "category": "learning",
        },

        {
            "pattern": "Can you give me a brief introduction to this {object}?",

            "variables": {
                "object": OBJECT
            },
            "category": "repository_intro",
        },

        {
            "pattern": "What is the main idea behind this {object}?",

            "variables": {
                "object": OBJECT
            },
            "category": "main_idea",
        },

        {
            "pattern": "What is this {object} built for?",

            "variables": {
                "object": OBJECT
            },
            "category": "built_for",
        },

        {
            "pattern": "Help me understand this {object} as a whole.",

            "variables": {
                "object": OBJECT
            },
            "category": "overall_understanding"
        },

        {
            "pattern": "Before I explore the code, explain this {object}.",

            "variables": {
                "object": OBJECT
            },
            "category": "before_reading",
        },

        {
            "pattern": "I am new to this {object}. Can you explain it?",

            "variables": {
                "object": OBJECT
            },
            "category": "new_developer"
        },

        {
            "pattern": "Give me a quick summary of this {object}.",

            "variables": {
                "object": OBJECT
            },
            "category": "quick_summary"
        },

        {
            "pattern": "Explain this {object} like I'm joining the project today.",

            "variables": {
                "object": OBJECT
            },
            "category": "beginner"
        },

        {
            "pattern": "What should I know about this {object} before reading the code?",

            "variables": {
                "object": OBJECT
            },
            "category": "repository_understanding"
        },

        {
            "pattern": "Can you provide some context about this {object}?",

            "variables": {
                "object": OBJECT
            },
            "category": "project_context",
        },
        
    ],

    # ==========================
    # ARCHITECTURE
    # ==========================
    
    "architecture" : [
        {
            "pattern":
            "Explain the architecture of this application.",

            "category": "overall_architecture"
        },

        {
            "pattern":
            "How does {feature} interact with other components?",

            "variables": {
                "feature": FEATURES
            },
            "category": "interaction"
        },

        {
            "pattern":
            "Explain the flow of {feature}.",

            "variables": {
                "feature": FEATURES
            },

            "category": "flow", 
        },

        {
            

            "pattern":
            "How does {feature} communicate with the rest of the system?",

            "variables": {
                "feature": FEATURES
            },
            "category": "communication",
        },

        {
            

            "pattern":
            "What components does {feature} depend on?",

            "variables": {
                "feature": FEATURES
            },
            "category": "dependency",
        },

        {
            

            "pattern":
            "Describe the lifecycle of {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "lifecycle",
        },

        {
            

            "pattern":
            "Describe the system design behind {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "system_design",
        },

        {
            

            "pattern":
            "How does data flow through {feature}?",

            "variables": {
                "feature": FEATURES
            },
            "category": "data_flow",
        },

        {
            

            "pattern":
            "How is {feature} connected to the rest of the repository?",

            "variables": {
                "feature": FEATURES
            },
            "category": "relationships",
        },

        {
            

            "pattern":
            "Give me the high-level design of {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "high_level_design"
        },
    ],

    # ==========================
    # IMPLEMENTATION
    # ==========================
    
    "implementation" : [
        {
            

            "pattern":
            "How is {feature} implemented?",

            "variables": {
                "feature": FEATURES
            },
            "category": "implementation"
        },

        {
            

            "pattern":
            "Explain how {feature} works.",

            "variables": {
                "feature": FEATURES
            },
            "category": "explanation"
        },

        {
            

            "pattern":
            "Walk me through the implementation of {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "walkthrough"
        },

        {
            

            "pattern":
            "Explain the internal logic of {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "logic",
        },

        {
            

            "pattern":
            "Explain the execution flow of {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "execution",
        },

        {
            

            "pattern":
            "Help me understand the code behind {feature}.",

            "variables": {
                "feature": FEATURES
            },
            "category": "code",
        },

        {
            

            "pattern":
            "Explain {feature} step by step.",

            "variables": {
                "feature": FEATURES
            },
            "category": "step_by_step",
        },

        {
            

            "pattern":
            "Teach me how {feature} works.",

            "variables": {
                "feature": FEATURES
            },
            "category": "learning",
        },

        {
            

            "pattern":
            "How was {feature} built?",

            "variables": {
                "feature": FEATURES
            },
            "category": "build",
        },

        {
            

            "pattern":
            "Explain the implementation of the {feature} module.",

            "variables": {
                "feature": FEATURES
            },
            "category": "module"
        },

        {
            "category": "behind_scenes",

            "pattern": "What happens behind the scenes when {feature} runs?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "under_the_hood",

            "pattern": "How does {feature} work under the hood?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "deep_dive",

            "pattern": "Can you do a deep dive into {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "mechanism",

            "pattern": "Explain the mechanism behind {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "working_principle",

            "pattern": "Explain the working principle of {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "processing",

            "pattern": "How does {feature} process requests?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "request_lifecycle",

            "pattern": "What happens after {feature} receives a request?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "sequence",

            "pattern": "What is the sequence of operations inside {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "input_output",

            "pattern": "How does {feature} transform input into output?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "lifecycle",

            "pattern": "Describe the lifecycle of {feature} during execution.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "reasoning",

            "pattern": "Why is {feature} implemented this way?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "algorithm",

            "pattern": "Explain the algorithm used in {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "event_handling",

            "pattern": "How does {feature} handle events internally?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "state_changes",

            "pattern": "How does the internal state change during {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "end_to_end",

            "pattern": "Explain the complete execution of {feature} from start to finish.",

            "variables": {
                "feature": FEATURES
            }
        },

    ],

    "locate" : [

    ],




}