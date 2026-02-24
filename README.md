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

# Speech-to-Text Bahasa Indonesia

Aplikasi transkripsi otomatis untuk audio dan video Bahasa Indonesia menggunakan model **OpenAI Whisper Large v3**. Dibangun dengan Gradio untuk antarmuka web yang interaktif.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Supported Formats](#supported-formats)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

## Overview

Proyek ini menyediakan solusi end-to-end untuk mengonversi speech (ucapan) dalam Bahasa Indonesia menjadi teks secara otomatis. Aplikasi mendukung input berupa file audio maupun video, dengan ekstraksi audio otomatis untuk file video menggunakan FFmpeg.

## Features

| Feature | Description |
|---|---|
| **Transkripsi Indonesia** | Konversi speech Bahasa Indonesia ke teks dengan akurasi tinggi |
| **Translate ke English** | Terjemahan langsung dari audio Indonesia ke teks English |
| **Timestamps** | Tampilkan waktu per segmen untuk navigasi audio/video panjang |
| **Video Support** | Upload file video (MP4, MKV, AVI, dll.) — audio diekstrak otomatis |
| **Long-form Audio** | Mendukung audio/video berdurasi panjang (> 30 detik) |
| **GPU Acceleration** | Otomatis menggunakan CUDA GPU jika tersedia, fallback ke CPU |

## Supported Formats

**Audio:** MP3, WAV, FLAC, OGG, M4A, WMA

**Video:** MP4, MKV, AVI, MOV, WebM, FLV, WMV

## Tech Stack

| Component | Technology |
|---|---|
| Model | [OpenAI Whisper Large v3](https://huggingface.co/openai/whisper-large-v3) |
| ML Framework | PyTorch, Hugging Face Transformers |
| Web UI | Gradio |
| Audio Extraction | FFmpeg |
| Inference Optimization | Hugging Face Accelerate |

## Prerequisites

- **Python** >= 3.10
- **FFmpeg** (required for video file support)
- **RAM** >= 8 GB (model membutuhkan ~3 GB)
- **GPU** (opsional, untuk inference lebih cepat)

### Install FFmpeg

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows (via Chocolatey)
choco install ffmpeg
```

## Installation

1. **Clone repository**

```bash
git clone https://github.com/romizone/speech-to-text-indonesia.git
cd speech-to-text-indonesia
```

2. **Buat virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Jalankan aplikasi**

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:7860`

## Usage

1. Buka `http://localhost:7860` di browser
2. Upload file audio atau video
3. Pilih mode:
   - **Transcribe** — menghasilkan teks dalam Bahasa Indonesia
   - **Translate** — menerjemahkan audio ke teks English
4. (Opsional) Centang **Tampilkan Timestamps** untuk melihat waktu per segmen
5. Klik **Mulai Transkripsi**

### Contoh Output

**Tanpa timestamps:**
```
Selamat pagi, hari ini kita akan membahas tentang teknologi kecerdasan buatan.
```

**Dengan timestamps:**
```
[0.0s -> 2.5s] Selamat pagi,
[2.5s -> 6.8s] hari ini kita akan membahas tentang teknologi kecerdasan buatan.
```

## Deployment

### Hugging Face Spaces

Proyek ini siap di-deploy ke [Hugging Face Spaces](https://huggingface.co/spaces). Metadata konfigurasi sudah tersedia di header `README.md` (YAML front matter).

1. Buat Space baru di Hugging Face (SDK: Gradio)
2. Push repository ini ke Space tersebut
3. Space akan otomatis build dan deploy

### Docker (Opsional)

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

## Project Structure

```
speech-to-text-indonesia/
├── app.py              # Main application (Gradio + Whisper pipeline)
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── .gitignore          # Git ignore rules
```

## Configuration

| Parameter | Default | Description |
|---|---|---|
| `model_id` | `openai/whisper-large-v3` | Model Whisper yang digunakan |
| `device` | Auto-detect | `cuda:0` jika GPU tersedia, `cpu` jika tidak |
| `torch_dtype` | Auto-detect | `float16` (GPU) atau `float32` (CPU) |
| `language` | `indonesian` | Bahasa target untuk transkripsi |

Untuk mengganti model (misalnya ke versi lebih ringan), ubah `model_id` di `app.py`:

```python
model_id = "openai/whisper-large-v3-turbo"  # Lebih cepat, sedikit kurang akurat
model_id = "openai/whisper-medium"           # Lebih ringan untuk perangkat terbatas
```

## Known Limitations

- Download model pertama kali membutuhkan ~3 GB bandwidth
- Inference di CPU relatif lambat untuk audio panjang (> 5 menit)
- Akurasi bergantung pada kualitas audio (background noise dapat mengurangi akurasi)
- File video besar membutuhkan waktu lebih lama untuk ekstraksi audio

## Contributing

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/nama-fitur`)
3. Commit perubahan (`git commit -m "Add: deskripsi fitur"`)
4. Push ke branch (`git push origin feature/nama-fitur`)
5. Buat Pull Request

## License

Proyek ini menggunakan lisensi [MIT](LICENSE).

---

Dibuat dengan Whisper Large v3 + Gradio
