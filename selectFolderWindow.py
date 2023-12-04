import tkinter as tk
from tkinter import filedialog

class selectFolder:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Folder")
        self.root.geometry("200x100")

        self.select_folder_button = tk.Button(root, text="Select destination folder", command=self.open_folder_dialog)
        self.select_folder_button.pack(pady=20)

    def open_folder_dialog(self):

        dialog = SelectFolderDialog(self.root)

        selected_folder = dialog.show_dialog()

        if selected_folder:
            print(f"Pasta selecionada: {selected_folder}")
            outputPath = selected_folder

            self.root.destroy()

class SelectFolderDialog:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()

    def show_dialog(self):
        folder_selected = filedialog.askdirectory()

        self.root.deiconify()

        return folder_selected

if __name__ == "__main__":
    root = tk.Tk()
    app = selectFolder(root)
    root.mainloop()