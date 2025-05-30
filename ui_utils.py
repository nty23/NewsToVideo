from IPython.display import HTML

def show_video(video_path):
    display(HTML(f"""
    <video width="720" height="405" controls>
        <source src="{video_path}" type="video/mp4">
    </video>
    """))
