# 🤖 GenAI-Powered Virtual Interviewer

A proof-of-concept AI system that simulates human-like technical interviews using state-of-the-art LLMs and RAG (Retrieval-Augmented Generation). It dynamically generates personalized questions based on a candidate’s resume and evaluates their responses with contextual feedback.

---

## 🧠 Key Features

- Real-time question generation using LLM (LLaMA 3.1 via Groq)
- Resume-aware flow using Retrieval-Augmented Generation (RAG)
- Scoring and feedback for each answer
- Modular design using LangChain, FAISS, and Streamlit

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM Integration:** Groq + LLaMA 3.1
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
- **Vector Store:** FAISS
- **PDF Parsing:** PyPDF
- **Prompt Chaining:** LangChain
- **Environment Management:** python-dotenv

---

## 📦 Installation & Run Locally

```bash
git clone https://github.com/Devanshu070/GenAI-Interviewer.git
cd GenAI-Interviewer
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
## 🔮 Future Roadmap

- **Multimodal Integration**  
  Incorporate audio (speech-to-text) and video (facial expression/emotion analysis) for a more immersive interview experience.

- **Analytics Dashboard**  
  Visualize candidate performance, scoring trends, and feedback summaries for HR/recruiter insights.

- **Multi-Round Interview Simulation**  
  Simulate full-length interviews with HR round + technical round + managerial round.

- **Data Privacy & Consent**  
  Implement secure data handling practices and candidate consent mechanisms.

---

## 👨‍💻 Author

**Devanshu Gupta**

---
## 📸 Screenshots

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/d249dea0-2367-497f-a4cc-1b9d4ec1fda8" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/a685feec-7573-4269-9f49-4c5856b6c7e5" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/e5309f6d-54b0-4ecd-b22f-f3119f86af00" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/ff361b71-1681-4d56-802e-641446a87da9" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/ee59059e-4429-418b-8d83-0ca3d18d87d7" width="400"/></td>
  </tr>
</table>


