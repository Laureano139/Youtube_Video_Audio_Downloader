import tkinter
import customtkinter
from pytube import YouTube

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
            youtube = YouTube(link)
            audio = youtube.streams.get_audio_only()
            audio.download()
            self.download_completed.configure(text="Download completed successfully!")
            #print("Download completed successfully!")
        except:
            #print("Youtube link may be invalid!")
            self.download_completed.configure(text="Oops! Something went wrong!")

    def downloadVideo(self):
        try:
            link = self.insert_link_input.get()
            youtube = YouTube(link)
            video = youtube.streams.get_highest_resolution()
            video.download()
            self.download_completed.configure(text="Download completed successfully!")
            #print("Download completed successfully!")
        except:
            #print("Youtube link may be invalid!")
            self.download_completed.configure(text="Oops! Something went wrong!")
            
    def HomePage(self):
        
        self.insert_link = customtkinter.CTkLabel(self, text="Youtube Downloader")
        self.insert_link.configure(font=("Courier-Bold",50))
        #self.insert_link.configure(fg="green") -> Não funfa
        self.insert_link.pack(padx=20, pady=20)
        
        self.go_to_Video = customtkinter.CTkButton(self, text="Video", command=self.DownloadVideoPage, fg_color="green")
        self.go_to_Video.pack(padx=10, pady=10)
        
        self.go_to_Video = customtkinter.CTkButton(self, text="Audio", command=self.DownloadAudioPage, fg_color="green")
        self.go_to_Video.pack(padx=10, pady=10)
        
    def DownloadAudioPage(self):
        
        # Adicionar butões para voltar para trás
        
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
        
    def DownloadVideoPage(self):
        
        # Adicionar butões para voltar para trás
        
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
        
        
    def destroy_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    yd = App()
     # Temos de meter a app a correr, se não fecha logo -> mainloop()
    yd.mainloop()