import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_UPLOADS_DIR = os.path.join(BASE_DIR, "user_uploads")

# ElevenLabs client (env-based, portable)
client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def text_to_speech_file(text: str, folder: str) -> str:
    audio_path = os.path.join(USER_UPLOADS_DIR, folder, "audio.mp3")

    # ✅ Skip regeneration (saves credits)
    if os.path.exists(audio_path):
        size = os.path.getsize(audio_path)
        if size > 10_000:  # ~10 KB
            print("🔁 Valid audio already exists, skipping TTS")
            return audio_path
        else:
            print("⚠️ Corrupt audio detected, regenerating")
            os.remove(audio_path)

    response = client.text_to_speech.convert(
        text=text,
        voice_id="pNInz6obpgDQGcFmaJgB",
        model_id="eleven_turbo_v2_5",
        output_format="mp3_22050_32",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    with open(audio_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"✅ Audio saved: {audio_path}")
    return audio_path
