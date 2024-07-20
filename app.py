from flask import Flask, request, render_template, send_file, flash, redirect
import yt_dlp as youtube_dl
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Substitua 'your_secret_key' por uma chave secreta segura

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    choice = request.form['choice']
    
    try:
        ydl_opts = {}
        if choice == 'video':
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloads/video.%(ext)s',
            }
        elif choice == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'downloads/audio.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        filename = 'video.mp4' if choice == 'video' else 'audio.mp3'
        path = os.path.join('downloads', filename)
        return send_file(path, as_attachment=True)
    
    except Exception as e:
        flash(f'Erro ao baixar o vídeo: {str(e)}', 'danger')
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)