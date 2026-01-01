# 🎬 VidBot – AI Video Generator

VidBot is a Python-based AI video generator that converts text input into short videos using
AI-generated audio, images, and FFmpeg processing.

This project focuses on **clean backend architecture**, **secure API handling**, and
**production-ready Git practices**.

---

## ✨ Features

- 🧠 Text → AI Voice (TTS)
- 🎞️ Auto-generated short videos (reels)
- 🎵 Background audio support
- ⚙️ FFmpeg-based video rendering
- 🔐 Secure API key handling using environment variables
- 🧹 Clean Git setup (no generated files committed)

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **FFmpeg**
- **ElevenLabs API** (Text-to-Speech)
- **HTML / CSS**

---

## 📁 Project Structure
AI-video-generator/
│
├── main.py
├── run.py
├── generate_process.py
├── text_to_audio.py
├── templates/
│ ├── index.html
│ ├── create.html
│ ├── gallery.html
│ └── base.html
├── static/
│ └── css/
│ ├── style.css
│ ├── create.css
│ └── gallery.css
├── .gitignore
└── README.md


---

## 🔐 Environment Setup

This project uses **environment variables** for API keys.

### PowerShell (Windows)

```powershell
$env:ELEVENLABS_API_KEY="your_api_key_here"


Or use a .env file (recommended for local development):

ELEVENLABS_API_KEY=your_api_key_here


⚠️ Never commit API keys to GitHub.

▶️ How to Run Locally

Clone the repository:

git clone https://github.com/mahakk24/AI-video-generator.git
cd AI-video-generator


Install dependencies:

pip install -r requirements.txt


Run the app:

python run.py

🚀 Output

Generated audio → static/songs/

Generated videos → static/reels/

User uploads → user_uploads/

These folders are ignored by Git on purpose.

📌 Notes

Generated media files are not pushed to GitHub

This keeps the repo lightweight and secure

Suitable for deployment and scaling

👤 Author

Mahak Prajapati
GitHub: https://github.com/mahakk24

⭐ Future Improvements

Docker support

Cloud deployment

Background job queue

UI enhancements

⭐ If you like this project, consider giving it a star!

