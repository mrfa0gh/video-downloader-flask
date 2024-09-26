from flask import Flask, render_template, request
import yt_dlp
import uuid
import os

app = Flask(__name__)

def download_video(video_url):
    # Generate a random filename with .mp4 extension
    random_filename = str(uuid.uuid4()) + '.mp4'
    # تحديد المسار الافتراضي "Downloads"
    save_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(save_path, random_filename)
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            return f"Video downloaded successfully as {random_filename} in Downloads folder"
        except Exception as e:
            return f"An error occurred: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["url"]
        message = download_video(video_url)
        return render_template('index.html', message=message)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
