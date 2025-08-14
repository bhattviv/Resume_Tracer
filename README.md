🚀 Resume Tracer

A Streamlit-based web application that allows users to upload resumes and track their details, status, and progress.
The app provides an intuitive interface for managing and visualizing resume-related data.

🚀 Features

📤 Resume Upload — Upload PDF or DOCX resumes.

📊 Data Extraction — Extract candidate information from resumes.

🔍 Search & Filter — Easily search for resumes based on name, skills, or experience.

📈 Dashboard View — Visualize resume statistics.

🗂 Download & Manage — Store and retrieve resumes as needed.

🎨 Modern UI — Sleek design built with Streamlit for a smooth experience.

📦 Installation

Clone the repository

git clone https://github.com/yourusername/resume-tracer.git
cd resume-tracer


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows


Install dependencies

pip install -r requirements.txt

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Then open the local URL in your browser:

http://localhost:8501

📁 Project Structure
resume-tracer/
│
├── app.py                # Main Streamlit app
├── utils/                # Helper functions (data parsing, file handling)
├── assets/               # Images, icons, styles
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── data/                 # Uploaded resumes & extracted info

🛠 Tech Stack

Frontend & Backend — Streamlit

Data Handling — Pandas, Python

Resume Parsing — PyPDF2, docx2txt, spaCy (optional)

Visualization — Matplotlib, Plotly

📌 Future Improvements

✅ AI-powered skill extraction

✅ Resume scoring system

✅ Export data as CSV/Excel

✅ Integration with ATS systems

📜 License

This project is licensed under the MIT License — feel free to modify and use it for personal or commercial purposes.
