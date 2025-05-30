from moviepy.editor import AudioFileClip, ImageClip

def generate_video(image_path, audio_path, output_path="final_video.mp4"):
    audio_clip = AudioFileClip(audio_path)
    img_clip = ImageClip(image_path).set_duration(audio_clip.duration).set_audio(audio_clip)
    img_clip.write_videofile(output_path, fps=24)
    return output_path
