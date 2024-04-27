import google.generativeai as genai
st.title"Gemini in here"
analyze_button = st.button("Analyze Text")
genai.configure(st.secrets["GOOGLE_API_KEY"])
