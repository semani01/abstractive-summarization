# **Abstractive Summarization Using Transformers**

## 🚀 **Project Overview**
The ever-growing volume of digital content, including research papers, news articles, and web content, presents a major challenge in efficiently extracting meaningful insights. This project implements an advanced **abstractive summarization system** leveraging **PEGASUS-XSum**, a state-of-the-art transformer model fine-tuned on scientific datasets.

The system is capable of summarizing:
- 📄 **Scientific Papers (arXiv dataset)**
- 📰 **News Articles (CNN/DailyMail dataset)**
- 🌐 **Web Content (URLs)**
- 📑 **PDF Documents**

The developed model is integrated into a **user-friendly web application**, enabling users to **input text, upload PDFs, or paste URLs** for instant abstractive summaries.

---

## 🧠 **Model Architecture**
PEGASUS-XSum follows a **Transformer-based encoder-decoder architecture** designed for abstractive summarization. It leverages **Gap-Sentence Generation (GSG) and Masked Language Modeling (MLM)** as pretraining objectives.

### **Architecture Overview:**
![Model Architecture](https://github.com/user-attachments/assets/55b6c5cc-7327-46c5-afc1-c01efb55a771)

- **Gap-Sentence Generation (GSG):** One full sentence is masked and used as the target summary.
- **Masked Language Modeling (MLM):** Some tokens are randomly masked in the input, forcing the model to predict missing words based on context.

These techniques significantly improve the model’s ability to **generate human-like, fluent, and coherent summaries.**

---

## 🌐 **Web Application**
To make abstractive summarization accessible to users, we developed a **fully functional web application** with a sleek and intuitive UI.

### **App Features:**
✅ Summarize **raw text** 📜  
✅ Upload **PDFs** for summarization 📑  
✅ Summarize content from **URLs** 🌍  
✅ Fast inference powered by **Flask API** ⚡

### **App Screenshot**
<img src="https://github.com/user-attachments/assets/b93d6292-5f9b-46eb-893a-afdb6e1bd65b" alt="Abstract Summarization App" width="500" />

---

## ⚙️ **Installation & Setup**
To run the project locally, follow these steps:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/abstractive-summarization-app.git
cd abstractive-summarization-app
```
### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate    # On Windows
```
### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4️⃣ Download & Setup the Model**
```bash
wget https://github.com/your-username/repo-name/releases/download/v1.0.0/model.safetensors -P app/deployment_model/
```
### **5️⃣ Merging Model Files**
If the fine-tuned PEGASUS-XSum model is split into multiple parts due to size restrictions, merge them using:
```bash
cat model_part_aa model_part_ab > model.safetensors
```
### **6️⃣ Run the Web App**
```bash
python app.py
```
Now, open your browser and navigate to http://127.0.0.1:5000/ to access the summarization interface.

---
## 📊 **Dataset & Model Training**

### **Datasets Used:**
- **arXiv Dataset** (Scientific Papers)  
- **CNN/DailyMail** (News Articles)  
- **XSUM** (Concise Summaries)

### **Preprocessing Steps:**
- **Tokenization** using **Hugging Face's Pegasus tokenizer**  
- **Input truncation** to **1024 tokens**  
- **Padding** for uniform sequence length  
- **Dataset splitting**: **Train (40k) | Validation (5k) | Test (5k)**

### **Training Setup:**
- **Fine-tuned PEGASUS-XSum** on Google Colab with GPU acceleration  
- Optimized hyperparameters using **Optuna**  
- Loss function: **Cross-entropy with label smoothing**

---

## 📈 **Evaluation & Performance**

We assessed model performance using **ROUGE** and **BLEU** scores:

| **Metric**      | **PEGASUS-XSum** |
|-----------------|------------------|
| **ROUGE-1**     | 41.97%           |
| **ROUGE-2**     | 23.48%           |
| **ROUGE-L**     | 38.21%           |
| **BLEU Score**  | 42.23%           |

### **Comparison with Other Models**

| **Model**        | **Challenges**                                         |
|------------------|--------------------------------------------------------|
| **BART**         | Extractive tendencies, lacked fluency                  |
| **GPT-3.5-Turbo**| High computation cost, token length limitations        |
| **T5-Large**     | Training instability, gradient explosion issues         |
| **PEGASUS-XSum** | Best abstractive summarization performance             |

---

## 🔮 **Future Enhancements**
- **Multilingual Summarization**: Expand support beyond English texts.  
- **Real-time Summarization**: Reduce inference latency for real-time applications.  
- **Reinforcement Learning**: Improve factual accuracy by integrating human feedback.  
- **Larger Dataset Integration**: Train on diverse datasets to enhance generalization.  

---

## 📌 **Technologies Used**
- **Backend**: Flask, Python  
- **Model**: Pegasus-XSum (Hugging Face Transformers)  
- **Frontend**: HTML, CSS, JavaScript  
- **Dependencies**: PyPDF2, BeautifulSoup, Flask, Hugging Face Transformers  

---

## 💡 **Conclusion**
This project successfully demonstrates the power of **transformer-based abstractive summarization** using **PEGASUS-XSum**. With its **high accuracy, fluency, and adaptability**, it provides a **practical tool** for summarizing complex text content efficiently. The **web application** further enhances usability, making summarization accessible to a wider audience.

📌 **Developed by:** *Sai Srikar Emani*  

🚀 **Let’s make information more accessible, one summary at a time!**





