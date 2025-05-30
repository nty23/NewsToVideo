from article_utils import fetch_article
from audio_utils import text_to_audio
from image_utils import generate_image_with_text, generate_background_image
from video_utils import generate_video
from ui_utils import show_video

def main():
    url = input("Enter news article URL: ").strip()
    print(f"Fetching article from {url}...")
    article_text = fetch_article(url)
    print("[✓] Article fetched")

    script = article_text[:600].rsplit('.', 1)[0] + '.' if len(article_text) > 600 else article_text
    print("[✓] Script created:\n", script)

    print("Generating audio...")
    audio_file = text_to_audio(script)
    print("[✓] Audio created")

    print("Generating background image...")
    bg_image = generate_background_image(script)
    print("[✓] Background image generated")

    print("Overlaying text on image...")
    image_file = generate_image_with_text(script, bg_image)
    print("[✓] Text overlay completed")

    print("Creating video...")
    video_file = generate_video(image_file, audio_file)
    print(f"[✓] Video saved: {video_file}")

    print("Displaying video below:")
    show_video(video_file)

if __name__ == "__main__":
    main()
