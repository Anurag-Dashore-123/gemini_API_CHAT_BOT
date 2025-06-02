import google.generativeai as genai 
genai.generativeai.configure(api_key="YOUR_API_KEY)
model=gemini.GenerativeModel("gemini-1.5-flash")
prompt=str(Input("enter prompt:"))

response=model.generate_content(prompt)
print(response.text)

