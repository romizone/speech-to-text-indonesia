---
title: Speech-to-Text Bahasa Indonesia
emoji: 🎙️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=250&section=header&text=🎙️%20Speech-to-Text&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Bahasa%20Indonesia%20%7C%20Whisper%20Large%20v3&descSize=20&descAlignY=55" width="100%" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Gradio](https://img.shields.io/badge/Gradio-6.0+-F97316?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Transformers-FFD21E?style=for-the-badge)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=667EEA&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=Konversi+Suara+ke+Teks+Otomatis+🇮🇩;Powered+by+OpenAI+Whisper+Large+v3+🚀" alt="Typing SVG" />

<br/>

> 🎯 Solusi end-to-end untuk mengonversi **speech Bahasa Indonesia** menjadi teks secara otomatis.
> Mendukung file **audio** dan **video** dengan akurasi tinggi.

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="800" />

</div>

---

## 📑 Table of Contents

<div align="center">

🏠 [Overview](#-overview) · ✨ [Features](#-features) · 📂 [Formats](#-supported-formats) · 🛠️ [Tech Stack](#%EF%B8%8F-tech-stack) · 📋 [Prerequisites](#-prerequisites)

💻 [Installation](#-installation) · 🚀 [Usage](#-usage) · ☁️ [Deployment](#%EF%B8%8F-deployment) · 📁 [Structure](#-project-structure) · ⚙️ [Config](#%EF%B8%8F-configuration)

⚠️ [Limitations](#%EF%B8%8F-known-limitations) · 🤝 [Contributing](#-contributing) · 📄 [License](#-license)

</div>

---

## 🏠 Overview

<img src="https://user-images.githubusercontent.com/74038190/238353480-219bcc70-f5dc-466b-9a60-29653d8e8433.gif" width="38" align="left" />

Proyek ini menyediakan solusi **end-to-end** untuk mengonversi speech (ucapan) dalam **Bahasa Indonesia** menjadi teks secara otomatis. Aplikasi mendukung input berupa file audio maupun video, dengan ekstraksi audio otomatis untuk file video menggunakan FFmpeg.

<br/>

<div align="center">

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  📁 Upload   │────▶│  🔊 Extract  │────▶│  🧠 Whisper  │────▶│  📝 Output   │
│  Audio/Video │     │  Audio (FFmpeg)│    │  Large v3    │     │  Teks/Timestamp│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

</div>

---

## ✨ Features

<div align="center">

| | Feature | Description |
|:---:|---|---|
| 🇮🇩 | **Transkripsi Indonesia** | Konversi speech Bahasa Indonesia ke teks dengan akurasi tinggi |
| 🌐 | **Translate ke English** | Terjemahan langsung dari audio Indonesia ke teks English |
| ⏱️ | **Timestamps** | Tampilkan waktu per segmen untuk navigasi audio/video panjang |
| 🎬 | **Video Support** | Upload file video (MP4, MKV, AVI, dll.) — audio diekstrak otomatis |
| 📼 | **Long-form Audio** | Mendukung audio/video berdurasi panjang (> 30 detik) |
| ⚡ | **GPU Acceleration** | Otomatis menggunakan CUDA GPU jika tersedia, fallback ke CPU |

</div>

---

## 📂 Supported Formats

<div align="center">

| 🔊 Audio | 🎬 Video |
|:---:|:---:|
| ![MP3](https://img.shields.io/badge/MP3-FF6B6B?style=flat-square&logoColor=white) ![WAV](https://img.shields.io/badge/WAV-4ECDC4?style=flat-square&logoColor=white) ![FLAC](https://img.shields.io/badge/FLAC-45B7D1?style=flat-square&logoColor=white) | ![MP4](https://img.shields.io/badge/MP4-667EEA?style=flat-square&logoColor=white) ![MKV](https://img.shields.io/badge/MKV-764BA2?style=flat-square&logoColor=white) ![AVI](https://img.shields.io/badge/AVI-F093FB?style=flat-square&logoColor=white) |
| ![OGG](https://img.shields.io/badge/OGG-96CEB4?style=flat-square&logoColor=white) ![M4A](https://img.shields.io/badge/M4A-FFEAA7?style=flat-square&logoColor=black) ![WMA](https://img.shields.io/badge/WMA-DDA0DD?style=flat-square&logoColor=white) | ![MOV](https://img.shields.io/badge/MOV-74B9FF?style=flat-square&logoColor=white) ![WebM](https://img.shields.io/badge/WebM-A29BFE?style=flat-square&logoColor=white) ![FLV](https://img.shields.io/badge/FLV-FD79A8?style=flat-square&logoColor=white) |

</div>

---

## 🛠️ Tech Stack

<div align="center">

| Component | Technology | |
|:---:|---|:---:|
| 🧠 **Model** | [OpenAI Whisper Large v3](https://huggingface.co/openai/whisper-large-v3) | ![Whisper](https://img.shields.io/badge/Whisper-412991?style=flat-square&logo=openai&logoColor=white) |
| 🔥 **ML Framework** | PyTorch + Hugging Face Transformers | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) |
| 🎨 **Web UI** | Gradio | ![Gradio](https://img.shields.io/badge/Gradio-F97316?style=flat-square&logo=gradio&logoColor=white) |
| 🎵 **Audio** | FFmpeg | ![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white) |
| 🚀 **Optimization** | Hugging Face Accelerate | ![HF](https://img.shields.io/badge/Accelerate-FFD21E?style=flat-square&logoColor=black) |

</div>

---

## 📋 Prerequisites

<div align="center">

| Requirement | Minimum | Recommended |
|:---:|:---:|:---:|
| 🐍 Python | >= 3.10 | 3.13 |
| 🎬 FFmpeg | Required | Latest |
| 💾 RAM | 8 GB | 16 GB |
| 🎮 GPU | Opsional | NVIDIA CUDA |

</div>

### 📦 Install FFmpeg

```bash
# 🍎 macOS
brew install ffmpeg

# 🐧 Ubuntu/Debian
sudo apt install ffmpeg

# 🪟 Windows (via Chocolatey)
choco install ffmpeg
```

---

## 💻 Installation

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="30" align="left" />

**Step 1** — Clone repository

```bash
git clone https://github.com/romizone/speech-to-text-indonesia.git
cd speech-to-text-indonesia
```

**Step 2** — Buat virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # 🐧 Linux/macOS
# venv\Scripts\activate   # 🪟 Windows
```

**Step 3** — Install dependencies

```bash
pip install -r requirements.txt
```

**Step 4** — Jalankan aplikasi

```bash
python app.py
```

> 🌐 Aplikasi akan berjalan di `http://localhost:7860`

---

## 🚀 Usage

<div align="center">

```
  1️⃣ Upload          2️⃣ Pilih Mode        3️⃣ Klik Mulai       4️⃣ Hasil
┌──────────┐      ┌──────────────┐     ┌──────────────┐    ┌──────────────┐
│ 📁 Audio │      │ 📝 Transcribe│     │              │    │ 📄 Teks      │
│    atau   │ ──▶  │      atau    │ ──▶  │  🚀 Mulai   │──▶ │    atau      │
│ 🎬 Video │      │ 🌐 Translate │     │  Transkripsi │    │ ⏱️ Timestamp │
└──────────┘      └──────────────┘     └──────────────┘    └──────────────┘
```

</div>

### 📝 Contoh Output

**Tanpa timestamps:**
```
Selamat pagi, hari ini kita akan membahas tentang teknologi kecerdasan buatan.
```

**Dengan timestamps:**
```
[0.0s → 2.5s]  Selamat pagi,
[2.5s → 6.8s]  hari ini kita akan membahas tentang teknologi kecerdasan buatan.
```

---

## ☁️ Deployment

### 🤗 Hugging Face Spaces

Proyek ini siap di-deploy ke [Hugging Face Spaces](https://huggingface.co/spaces). Metadata konfigurasi sudah tersedia di header `README.md` (YAML front matter).

```
1️⃣  Buat Space baru di Hugging Face (SDK: Gradio)
2️⃣  Push repository ini ke Space tersebut
3️⃣  Space akan otomatis build dan deploy ✅
```

### 🐳 Docker (Opsional)

```dockerfile
FROM python:3.13-slim
RUN apt-get update && apt-get install -y ffmpeg
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]
```

---

## 📁 Project Structure

```
speech-to-text-indonesia/
│
├── 🎯 app.py              # Main application (Gradio + Whisper pipeline)
├── 📦 requirements.txt    # Python dependencies
├── 📖 README.md           # Documentation
└── 🚫 .gitignore          # Git ignore rules
```

---

## ⚙️ Configuration

| Parameter | Default | Description |
|:---:|:---:|---|
| `model_id` | `openai/whisper-large-v3` | 🧠 Model Whisper yang digunakan |
| `device` | Auto-detect | ⚡ `cuda:0` jika GPU tersedia, `cpu` jika tidak |
| `torch_dtype` | Auto-detect | 🔢 `float16` (GPU) atau `float32` (CPU) |
| `language` | `indonesian` | 🇮🇩 Bahasa target untuk transkripsi |

> 💡 Untuk mengganti model, ubah `model_id` di `app.py`:

```python
model_id = "openai/whisper-large-v3-turbo"  # ⚡ Lebih cepat
model_id = "openai/whisper-medium"           # 💾 Lebih ringan
```

---

## ⚠️ Known Limitations

| | Limitation |
|:---:|---|
| 📥 | Download model pertama kali membutuhkan **~3 GB** bandwidth |
| 🐢 | Inference di CPU relatif lambat untuk audio panjang (> 5 menit) |
| 🔇 | Akurasi bergantung pada kualitas audio (background noise menurunkan akurasi) |
| 📁 | File video besar membutuhkan waktu lebih lama untuk ekstraksi audio |

---

## 🤝 Contributing

<img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37c1-4d43-bbba-0f4a3cdd1e44.gif" width="30" align="left" />

Kontribusi sangat diterima! Ikuti langkah berikut:

```
1️⃣  Fork repository ini
2️⃣  Buat branch fitur    →  git checkout -b feature/nama-fitur
3️⃣  Commit perubahan     →  git commit -m "Add: deskripsi fitur"
4️⃣  Push ke branch       →  git push origin feature/nama-fitur
5️⃣  Buat Pull Request    →  🎉
```

---

## 📄 License

Proyek ini menggunakan lisensi [MIT](LICENSE).

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=120&section=footer" width="100%" />

Made with ❤️ using **Whisper Large v3** + **Gradio**

[![GitHub](https://img.shields.io/badge/GitHub-romizone-181717?style=for-the-badge&logo=github)](https://github.com/romizone)

</div>
