import gradio as gr
import torch
import subprocess
import tempfile
import os
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

# ============================================
# 🎙️ Speech-to-Text Bahasa Indonesia
# Menggunakan OpenAI Whisper Large v3
# ============================================

# Setup device & dtype
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Model ID
model_id = "openai/whisper-large-v3"

# Load model & processor
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id,
    torch_dtype=torch_dtype,
    low_cpu_mem_usage=True,
    use_safetensors=True,
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

# Create pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)


VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv", ".wmv"}


def extract_audio(file_path):
    """Extract audio from video file using ffmpeg."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in VIDEO_EXTENSIONS:
        return file_path

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.close()
    subprocess.run(
        ["ffmpeg", "-y", "-i", file_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", tmp.name],
        capture_output=True,
    )
    return tmp.name


def transcribe(audio_file, task, return_timestamps):
    """Transcribe audio/video file to text."""
    if audio_file is None:
        return "⚠️ Silakan upload file audio/video terlebih dahulu."

    audio_path = extract_audio(audio_file)

    generate_kwargs = {
        "language": "indonesian",
        "task": task.lower(),
    }

    result = pipe(
        audio_path,
        return_timestamps=True,
        generate_kwargs=generate_kwargs,
    )

    # Cleanup temp file
    if audio_path != audio_file:
        os.unlink(audio_path)

    if return_timestamps:
        output = ""
        for chunk in result["chunks"]:
            start = chunk["timestamp"][0]
            end = chunk["timestamp"][1]
            text = chunk["text"]
            if start is not None and end is not None:
                output += f"[{start:.1f}s → {end:.1f}s] {text}\n"
            else:
                output += f"{text}\n"
        return output.strip()
    else:
        return result["text"]


# ============================================
# Gradio Interface
# ============================================

with gr.Blocks(
    title="🎙️ Speech-to-Text Bahasa Indonesia",
    theme=gr.themes.Soft(primary_hue="blue"),
) as demo:

    gr.Markdown(
        """
    # 🎙️ Speech-to-Text Bahasa Indonesia
    ### Menggunakan OpenAI Whisper Large v3
    
    Upload file audio dalam Bahasa Indonesia dan dapatkan transkripsi teksnya.
    Mendukung format: **MP3, WAV, FLAC, OGG, M4A, WMA, MP4, MKV, AVI, MOV**
    """
    )

    with gr.Row():
        with gr.Column(scale=1):
            audio_input = gr.File(
                label="📁 Upload File Audio/Video",
                file_types=[".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma", ".mp4", ".mkv", ".avi", ".mov", ".webm"],
            )

            with gr.Row():
                task = gr.Radio(
                    choices=["Transcribe", "Translate"],
                    value="Transcribe",
                    label="📝 Mode",
                    info="Transcribe = teks Indonesia | Translate = terjemahkan ke English",
                )

            timestamps = gr.Checkbox(
                label="⏱️ Tampilkan Timestamps",
                value=False,
                info="Tampilkan waktu untuk setiap segmen teks",
            )

            submit_btn = gr.Button(
                "🚀 Mulai Transkripsi",
                variant="primary",
                size="lg",
            )

        with gr.Column(scale=1):
            output_text = gr.Textbox(
                label="📄 Hasil Transkripsi",
                lines=15,
                placeholder="Hasil transkripsi akan muncul di sini...",
            )

    # Examples
    gr.Markdown("---")
    gr.Markdown("### 💡 Tips")
    gr.Markdown(
        """
    - **Audio yang jelas** menghasilkan transkripsi lebih akurat
    - Gunakan **Timestamps** untuk audio panjang agar mudah dinavigasi
    - Mode **Translate** akan menerjemahkan audio Indonesia ke teks English
    - Disarankan audio **< 30 menit** untuk hasil optimal
    """
    )

    # Event handler
    submit_btn.click(
        fn=transcribe,
        inputs=[audio_input, task, timestamps],
        outputs=output_text,
    )

demo.launch()
