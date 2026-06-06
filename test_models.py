# import google.generativeai as genai

# # 1. You must provide your API key before calling any other genai functions
# genai.configure(api_key="AQ")

# # 2. Now this will work without crashing!
# print("Fetching available models...")
# for model in genai.list_models():
#     print(model.name)