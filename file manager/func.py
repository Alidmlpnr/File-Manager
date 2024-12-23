import glob
import os
import shutil
from tkinter import Button, Listbox, Toplevel, filedialog, messagebox
import pyautogui 

def open_file(file):
    os.startfile(file)
    messagebox.showinfo('Dosya Aç', f"{file} başarıyla açıldı")

def delete_file(file):
    if messagebox.askyesno("Onay", f"{file} dosyasını silmek istediğinize emin misiniz?"):
        try:
            os.remove(file)
            messagebox.showinfo('Dosya Sil', f"{file} başarıyla silindi")
        except Exception as e:
            messagebox.showerror('Hata', str(e))

def rename_file(file, new_name):
    try:
        dir_name = os.path.dirname(file)
        new_path = os.path.join(dir_name, new_name)
        os.rename(file, new_path)
        messagebox.showinfo('Dosyayı Yeniden Adlandır', f"{file} {new_path} olarak yeniden adlandırıldı")
    except Exception as e:
        messagebox.showerror('Hata', str(e))

def create_folder(dir_path, new_folder_name):
    try:
        os.makedirs(os.path.join(dir_path, new_folder_name))
        messagebox.showinfo('Klasör Oluştur', "Klasör başarıyla oluşturuldu!")
    except Exception as e:
        messagebox.showerror('Hata', str(e))

def delete_folder(folder):
    if messagebox.askyesno("Onay", f"{folder} klasörünü silmek istediğinize emin misiniz?"):
        try:
            os.rmdir(folder)
            messagebox.showinfo('Klasörü Sil', "Klasör başarıyla silindi!")
        except Exception as e:
            messagebox.showerror('Hata', str(e))

def rename_folder(folder, new_name):
    try:
        parent_dir = os.path.dirname(folder)
        new_path = os.path.join(parent_dir, new_name)
        os.rename(folder, new_path)
        messagebox.showinfo('Klasörü Yeniden Adlandır', f"{folder} {new_path} olarak yeniden adlandırıldı")
    except Exception as e:
        messagebox.showerror('Hata', str(e))

def get_file_info(file):
    size = os.path.getsize(file)
    creation_time = os.path.getctime(file)
    return f"Boyut: {size} bayt\nOluşturulma Tarihi: {creation_time}"

def copy_file(file, dest_dir):
    try:
        shutil.copy(file, dest_dir)
        messagebox.showinfo('Dosyayı Kopyala', "Dosya başarıyla kopyalandı!")
    except Exception as e:
        messagebox.showerror('Hata', str(e))

def move_file(file, dest_dir):
    try:
        shutil.move(file, dest_dir)
        messagebox.showinfo('Dosyayı Taşı', "Dosya başarıyla taşındı!")
    except Exception as e:
        messagebox.showerror('Hata', str(e))

music_files = []  

def add_music():
    file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3;*.wav;*.ogg;*.flac")])
    if file:
        music_files.append(file)
        messagebox.showinfo("Bilgi", f"{os.path.basename(file)} başarıyla eklendi.")

def show_music_files():
    if music_files:
        return music_files 
    else:
        messagebox.showinfo("Bilgi", "Herhangi bir müzik dosyası eklenmemiştir.")
        return None


screenshot_files = []  

def add_screenshot():
    
    screenshot = pyautogui.screenshot()
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        screenshot.save(save_path)
        screenshot_files.append(save_path)
        messagebox.showinfo("Bilgi", f"Ekran görüntüsü {os.path.basename(save_path)} olarak kaydedildi.")

def show_screenshot_files():
    if screenshot_files:
        return screenshot_files  
    else:
        messagebox.showinfo("Bilgi", "Herhangi bir ekran görüntüsü eklenmemiştir.")
        return None

downloads_files = []  

def manage_downloads(self):
    action = messagebox.askquestion("İndirilenler Yönetimi", "Yeni bir dosya indirmek ister misiniz?")
    if action == 'yes':
        # Kullanıcıdan dosya seçmesini isteme
        file_path = filedialog.askopenfilename()
        if file_path:
            # İndirilenler klasörünün yolunu alma
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            # Dosyanın adını ve yeni yolunu belirleme
            file_name = os.path.basename(file_path)
            destination = os.path.join(downloads_path, file_name)
            # Dosyayı kopyalama
            shutil.copy(file_path, destination)
            messagebox.showinfo("Başarılı", f"{file_name} başarıyla indirildi.")
    else:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        current_downloads = os.listdir(downloads_path)

        if current_downloads:
            downloads_window = Toplevel(self.root)
            downloads_window.title("İndirilen Dosyalar")
            listbox = Listbox(downloads_window, width=50)
            listbox.pack(pady=20)

            for file in current_downloads:
                listbox.insert('end', file)

            Button(downloads_window, text='Kapat', command=downloads_window.destroy).pack(pady=10)
        else:
            messagebox.showinfo("Bilgi", "İndirilen dosya bulunmamaktadır.")

video_files = []
def add_video():
    file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
    if file:
        video_files.append(file)
        messagebox.showinfo("Bilgi", f"{os.path.basename(file)} başarıyla eklendi.")

def show_video_files():
    if video_files:
        return video_files
    else:
        messagebox.showinfo("Bilgi", "Herhangi bir video dosyası eklenmemiştir.")
        return None

image_files = []

def add_image():
    file = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file:
        image_files.append(file)
        messagebox.showinfo("Bilgi", f"{os.path.basename(file)} başarıyla eklendi.")

def show_image_files():
    if image_files:
        return image_files
    else:
        messagebox.showinfo("Bilgi", "Herhangi bir fotoğraf dosyası eklenmemiştir.")
        return None