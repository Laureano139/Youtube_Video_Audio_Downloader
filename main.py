import tkinter
import customtkinter
from pytube import YouTube
from tkinter import PhotoImage

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Definir path para onde salvar ficheiros (Downloads)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("My Youtube Downloader")
        
        self.HomePage()

    def downloadAudio(self):
        try:
        
            link = self.insert_link_input.get()
            youtube = YouTube(link, on_progress_callback=self.downloading)
            audio = youtube.streams.get_audio_only()
            self.show_ProgressBar_after_click()
            audio.download()
            self.download_completed.configure(text="Download completed successfully!")
            
        except Exception as e:
            print("Error downloading: ", e)
            self.download_completed.configure(text="Oops! Something went wrong! Please try another link!", text_color="red")

    def downloadVideo(self):
        try:
            link = self.insert_link_input.get()
            youtube = YouTube(link, on_progress_callback=self.downloading)
            video = youtube.streams.get_highest_resolution()
            self.show_ProgressBar_after_click()
            video.download()
            self.download_completed.configure(text="Download completed successfully!")
            
        except Exception as e:
            print("Error downloading: ", e)
            self.download_completed.configure(text="Oops! Something went wrong! Please try another link!", text_color="red")
            
    def HomePage(self):
        
        self.destroy_widgets()
        
        self.insert_link = customtkinter.CTkLabel(self, text="Youtube Downloader")
        self.insert_link.configure(font=("Courier-Bold",50))
        #self.insert_link.configure(fg="green") -> Não funfa
        self.insert_link.pack(padx=20, pady=20)
        
        self.go_to_Video = customtkinter.CTkButton(self, text="Video", command=self.DownloadVideoPage, fg_color="green")
        self.go_to_Video.pack(padx=10, pady=10)
        
        self.go_to_Video = customtkinter.CTkButton(self, text="Audio", command=self.DownloadAudioPage, fg_color="green")
        self.go_to_Video.pack(padx=10, pady=10)
        
    def DownloadAudioPage(self):
        
        self.destroy_widgets()
        
        self.insert_link = customtkinter.CTkLabel(self, text="Youtube Downloader")
        self.insert_link.configure(font=("Courier-Bold",50))
        self.insert_link.pack(padx=20, pady=20)
        
        # StringVar() -> Tipo de dados com features adicionais para manipular valores de widgets (Entry, Label, etc)
        self.url = tkinter.StringVar()
        self.insert_link_input = customtkinter.CTkEntry(self, width=500, height=50, border_color="green", textvariable=self.url)
        self.insert_link_input.pack(padx=10, pady=10)
        
        self.downloadAudio = customtkinter.CTkButton(self, text="Download Audio", command=self.downloadAudio, fg_color="green")
        self.downloadAudio.pack(padx=10, pady=10)
        
        self.download_completed = customtkinter.CTkLabel(self, text="")
        self.download_completed.pack()
        
        # Progress Bar
        self.progressPercentage = customtkinter.CTkLabel(self, text="0%")
        #self.progressPercentage.pack()
        
        self.bar = customtkinter.CTkProgressBar(self, width=500)
        self.bar.set(0)
        #self.bar.pack(padx=10, pady=10)
        
        self.goBackButton = customtkinter.CTkButton(self, text="Back", command=self.HomePage, fg_color="green")
        self.goBackButton.pack(pady=100)
        
    def DownloadVideoPage(self):
        
        self.destroy_widgets()
        
        self.insert_link = customtkinter.CTkLabel(self, text="Youtube Downloader")
        self.insert_link.configure(font=("Courier-Bold",50))
        self.insert_link.pack(padx=20, pady=20)
        
        self.url = tkinter.StringVar()
        self.insert_link_input = customtkinter.CTkEntry(self, width=500, height=50, border_color="green", textvariable=self.url)
        self.insert_link_input.pack(padx=10, pady=10)
        
        self.downloadVideo = customtkinter.CTkButton(self, text="Download Video", command=self.downloadVideo, fg_color="green")
        self.downloadVideo.pack(padx=10, pady=10)
        
        self.download_completed = customtkinter.CTkLabel(self, text="")
        self.download_completed.pack()
        
        # Progress Bar
        self.progressPercentage = customtkinter.CTkLabel(self, text="0%")
        self.progressPercentage.pack()
        
        self.bar = customtkinter.CTkProgressBar(self, width=500)
        self.bar.set(0)
        self.bar.pack(padx=10, pady=10)
        
        self.goBackButton = customtkinter.CTkButton(self, text="Back", command=self.HomePage, fg_color="green")
        self.goBackButton.pack(pady=100)
        
    def destroy_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
            
    def downloading(self, stream, chunk, bytesRemaining):
        size = stream.filesize
        bytesDownloaded = size - bytesRemaining
        percentage = (bytesDownloaded / size) * 100
        percentageString = str(int(percentage)) + "%"
        self.progressPercentage.configure(text=percentageString)
        self.progressPercentage.update()
        
        self.bar.set(int(percentage) / 100)
        
    def show_ProgressBar_after_click(self):
        self.progressPercentage.pack()
        self.bar.pack(padx=10, pady=10)

if __name__ == "__main__":
    yd = App()
     # Temos de meter a app a correr, se não fecha logo -> mainloop()
    yd.mainloop()