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
BUSINESS_FEATURES = [
    "login",
    "signup",
    "authentication",
    "authorization",
    "payment",
    "orders",
    "cart",
    "dashboard",
    "profile",
    "notifications",
    "search"
]

TECHNICAL_FEATURES = [
    "routing",
    "middleware",
    "API",
    "database",
    "cache",
    "state management",
    "configuration",
    "request handling",
    "session management",
    "validation"
]

FEATURES = BUSINESS_FEATURES + TECHNICAL_FEATURES

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

    # ==========================
    # LOCATE    
    # =========================

    "locate" : [
        {
            "category": "where",

            "pattern": "Where is {feature} implemented?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "locate",

            "pattern": "Locate {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "find",

            "pattern": "Find {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "which_file",

            "pattern": "Which file contains {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "which_module",

            "pattern": "Which module handles {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "folder",

            "pattern": "Which folder contains {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "component",

            "pattern": "Which component is responsible for {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "defined",

            "pattern": "Where is {feature} defined?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "declared",

            "pattern": "Where is {feature} declared?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "used",

            "pattern": "Where is {feature} used?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "lives",

            "pattern": "Where does {feature} live?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "point_me",

            "pattern": "Point me to the implementation of {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "navigation",

            "pattern": "Take me to {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "function",

            "pattern": "Which function handles {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "class",

            "pattern": "Which class is responsible for {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },


    ],


    # ==========================
    # COMPARISON    
    # =========================

    "comparison" : [
        {
            "category": "compare",

            "pattern": "Compare {feature1} and {feature2}.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "difference",

            "pattern": "What is the difference between {feature1} and {feature2}?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "similarities",

            "pattern": "How are {feature1} and {feature2} similar?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "contrast",

            "pattern": "Contrast {feature1} with {feature2}.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "versus",

            "pattern": "{feature1} vs {feature2}.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "side_by_side",

            "pattern": "Explain {feature1} and {feature2} side by side.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "better",

            "pattern": "Which is better, {feature1} or {feature2}?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "tradeoffs",

            "pattern": "What are the tradeoffs between {feature1} and {feature2}?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "pros_cons",

            "pattern": "Compare the pros and cons of {feature1} and {feature2}.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "use_case",

            "pattern": "When should I use {feature1} instead of {feature2}?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "performance",

            "pattern": "How do {feature1} and {feature2} differ in terms of performance?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "responsibility",

            "pattern": "How are the responsibilities of {feature1} and {feature2} different?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "roles",

            "pattern": "Compare the roles of {feature1} and {feature2}.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "internal_design",

            "pattern": "How do the implementations of {feature1} and {feature2} differ?",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

        {
            "category": "architecture",

            "pattern": "Compare the architecture of {feature1} and {feature2}.",

            "variables": {
                "feature1": FEATURES,
                "feature2": FEATURES
            }
        },

    ],


        # ==========================
    

    #=========================
    # DEBUG    
    # =========================

    "debug" : [
        {
            "category":"not_working",

            "pattern":"Why is {feature} not working?",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"failing",

            "pattern":"Why is {feature} failing?",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"broken",

            "pattern":"{feature} seems broken.",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"crashing",

            "pattern":"{feature} keeps crashing.",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"unexpected",

            "pattern":"Why is {feature} behaving unexpectedly?",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"issue",

            "pattern":"There is an issue with {feature}.",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"debug",

            "pattern":"Help me debug {feature}.",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"diagnose",

            "pattern":"Diagnose the problem with {feature}.",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"fix",

            "pattern":"How can I fix {feature}?",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"root_cause",

            "pattern":"Find the root cause of the problem in {feature}.",

            "variables":{

                "feature":FEATURES

            }

        },

        {
            "category":"always",

            "pattern":"{feature} always fails.",

            "variables":{
                "feature":FEATURES
            }
        },
####Family 12 — Never
        {
            "category":"never",

            "pattern":"{feature} never works.",

            "variables":{
                "feature":FEATURES
            }
        },
####Family 13 — Doesn't
        {
            "category":"does_not",

            "pattern":"{feature} doesn't work anymore.",

            "variables":{
                "feature":FEATURES
            }
        },
####Family 14 — Stops
        {
            "category":"stops",

            "pattern":"{feature} suddenly stopped working.",

            "variables":{
        "feature":FEATURES
            }
        },
####Family 15 — Unexpected Output
        {
            "category":"wrong_output",

            "pattern":"{feature} returns incorrect results.",

            "variables":{
                "feature":FEATURES
            }
        },
        ####Family 16 — Wrong Behaviour
        {
            "category":"wrong_behaviour",

            "pattern":"{feature} behaves differently than expected.",

            "variables":{
                "feature":FEATURES
            }
        },
####Family 17 — Nothing Happens
        {
            "category":"nothing_happens",

            "pattern":"Nothing happens when I use {feature}.",

            "variables":{
        "feature":FEATURES
            }
        },
        ####Family 18 — Stuck
        {
            "category":"stuck",

            "pattern":"{feature} gets stuck.",

            "variables":{
                "feature":FEATURES
            }
        },
####Family 19 — Infinite
        {
            "category":"infinite",

            "pattern":"{feature} runs forever.",

            "variables":{
        "feature":FEATURES
            }
        },
####Family 20 — Timeout
        {
            "category":"timeout",

            "pattern":"{feature} keeps timing out.",

            "variables":{
        "feature":FEATURES
            }
        },

        {
            "category": "exception",

            "pattern": "Why is {feature} throwing an exception?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 22 — Error
        {
            "category": "error",

            "pattern": "Why does {feature} throw an error?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 23 — Null
        {
            "category": "null",

            "pattern": "Why is {feature} returning null?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 24 — Undefined
        {
            "category": "undefined",

            "pattern": "Why is {feature} returning undefined?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 25 — Missing
        {
            "category": "missing_data",

            "pattern": "Why is {feature} missing data?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 26 — Incorrect Data
        {
            "category": "incorrect_data",

            "pattern": "Why is {feature} producing incorrect data?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 27 — Validation
        {
            "category": "validation",

            "pattern": "Why is validation failing in {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 28 — API Failure
        {
            "category": "api_failure",

            "pattern": "Why is the API failing in {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 29 — Request
        {
            "category": "request",

            "pattern": "Why does the request fail in {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },
        
###Family 30 — Response
        {
            "category": "response",

            "pattern": "Why is the response incorrect in {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },

        {
            "category": "trace_execution",

            "pattern": "Trace the execution of {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 32 — Investigate
        {
            "category": "investigation",

            "pattern": "Investigate the issue in {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 33 — Root Cause
        {
            "category": "root_cause_analysis",

            "pattern": "Help me identify the root cause in {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 34 — Logging
        {
            "category": "logging",

            "pattern": "Where should I add logs to debug {feature}?",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 35 — State Investigation
        {
            "category": "state",

            "pattern": "Help me investigate the state changes in {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 36 — Bottleneck
        {
            "category": "bottleneck",

            "pattern": "Find the bottleneck in {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 37 — Performance Issue
        {
            "category": "performance",

            "pattern": "Why is {feature} performing poorly?",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 38 — Race Condition
        {
            "category": "race_condition",

            "pattern": "Could {feature} have a race condition?",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 39 — Memory Leak
        {
            "category": "memory",

            "pattern": "Does {feature} have a memory leak?",

            "variables": {
                "feature": FEATURES
            }
        },
##Family 40 — Reproduce
        {
            "category": "reproduce",

            "pattern": "Help me reproduce the bug in {feature}.",

            "variables": {
                "feature": FEATURES
            }
        },


    ],


    #=========================
    # CASUAL    
    # =========================

    "casual": [
        {
            "category":"greeting",

            "pattern":"Hello"
        },
#Family 2 — Hi
        {
            "category":"greeting",

            "pattern":"Hi"
        },
#Family 3 — Good Morning
        {
            "category":"greeting",

            "pattern":"Good morning"
        },
#Family 4 — Goodbye
        {
            "category":"goodbye",

            "pattern":"Goodbye"
        },
#Family 5 — Thanks
        {
            "category":"thanks",

            "pattern":"Thank you"
        },
#Family 6 — Appreciation
        {
            "category":"appreciation",

            "pattern":"That was helpful."
        },
#Family 7 — Identity
        {
            "category":"identity",

            "pattern":"Who are you?"
        },
#Family 8 — Capability
        {
            "category":"capability",

            "pattern":"What can you do?"
        },
#Family 9 — Help
        {
            "category":"help",

            "pattern":"Can you help me?"
        },
#Family 10 — Joke
        {
            "category":"joke",

            "pattern":"Tell me a joke."
        },
#Family 11 — Confirmation
        {
            "category":"confirmation",

            "pattern":"Okay"
        },
#Family 12 — Acknowledgement
        {
            "category":"acknowledgement",

            "pattern":"Got it."
        },
#Family 13 — Nice
        {
            "category":"reaction",

            "pattern":"Nice!"
        },
#Family 14 — How are you
        {
            "category":"small_talk",

            "pattern":"How are you?"
        },
#Family 15 — Bye
        {
            "category":"bye",

            "pattern":"See you later."
        },
    ],
}