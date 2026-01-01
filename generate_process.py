#this file handles the reel generation
# This file looks for new folders inside user uploads and converts them to reel if they are not already converted
import os 
from text_to_audio import text_to_speech_file
import time
import subprocess


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_UPLOADS_DIR = os.path.join(BASE_DIR, "user_uploads")
DONE_FILE = os.path.join(BASE_DIR, "done.txt")

def text_to_audio(folder):
    desc_path = os.path.join(USER_UPLOADS_DIR, folder, "desc.txt")

    if not os.path.exists(desc_path):
        print(f"⚠️  Skipping {folder}: desc.txt not found")
        return

    with open(desc_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read().strip()


    if not text:
        print(f"⚠️  Skipping {folder}: desc.txt is empty")
        return

    text_to_speech_file(text, folder)
def normalize_images(folder):
    folder_path = os.path.join("user_uploads", folder)

    # All image files
    all_images = sorted(
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    )

    if not all_images:
        raise RuntimeError("❌ No images found in folder")

    # If images are already normalized, do nothing
    if all(img.startswith("frame_") for img in all_images):
        print("🖼️ Images already normalized, skipping rename")
        return

    # Otherwise, rename them
    for i, img in enumerate(all_images, start=1):
        src = os.path.join(folder_path, img)
        dst = os.path.join(folder_path, f"frame_{i:03d}.jpg")
        os.rename(src, dst)

    print(f"🖼️ Normalized {len(all_images)} images")



def create_reel(folder):
    normalize_images(folder)
    folder_path = os.path.join("user_uploads", folder)
    audio_path = os.path.join(folder_path, "audio.mp3")
    output_video = f"static/reels/{folder}.mp4"

    command = [
        "ffmpeg",
        "-y",
        "-framerate", "1/3",
        "-thread_queue_size", "512",
        "-i", f"{folder_path}/frame_%03d.jpg",
        "-i", audio_path,
        "-vf",
        (
            "scale=1080:1920:force_original_aspect_ratio=decrease,"
            "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,"
            "format=yuv420p"
        ),
        "-c:v", "libx264",
        "-profile:v", "baseline",
        "-level", "3.1",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",
        output_video,
    ]


    subprocess.run(command, check=True)
    print("✅ Reel created:", output_video)


if __name__ == "__main__":
    while True:
        print("Processing queue...")
        with open("done.txt", "r") as f:
            done_folders = f.readlines()

        done_folders = [f.strip() for f in done_folders]
        folders = os.listdir("user_uploads") 
        for folder in folders:
            if(folder not in done_folders): 
                text_to_audio(folder) # Generate the audio.mp3 from desc.txt
                create_reel(folder) # Convert the images and audio.mp3 inside the folder to a reel
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(10)

    
