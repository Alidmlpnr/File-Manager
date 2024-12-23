import glob
import os
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk
from func import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import shutil

class FileManagerApp:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x550+100+30")
        self.root.title("Dosya Yöneticisi Uygulaması")
        self.root.config(background="gray94")

        #self.set_background()  # Arka planı ayarlamak için
        self.create_widgets()  # Arayüz 

    def create_widgets(self):
        
        self.computer_frame = Frame(self.root, bg='gray20', height=500)
        self.computer_frame.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')

        #Label(self.computer_frame, text="Bu Bilgisayar", font=("bold", 14), fg="lightblue", bg='gray20').pack(pady=10)

        # Treeview ekleme
        self.tree = ttk.Treeview(self.computer_frame)
        self.tree.pack(expand=True, fill='both')

        # "Bu Bilgisayar" ve C sürücüsünü ekleme
        self.computer_node = self.tree.insert('', 'end', text='Bu Bilgisayar', open=True)
        self.c_drive_node = self.tree.insert(self.computer_node, 'end', text='C:', open=False)

        # C sürücüsünü doldurma: 
        self.populate_c_drive()

        # Butonların olduğu frame
        self.button_frame = Frame(self.root, bg='gray94')  
        self.button_frame.grid(row=1, column=1, padx=20, pady=10)

        # İkonların olduğu frame
        self.icon_frame = Frame(self.root, bg='gray94')
        self.icon_frame.grid(row=1, column=2, padx=20, pady=10) 

        # İkonlar için butonları oluştur
        self.create_icon_buttons()

        # İşlev butonları
        self.create_function_buttons()

    def create_icon_buttons(self):
        # Müzik ikonu
        self.music_icon = PhotoImage(file="icons/icon_musics.png").subsample(6)
        self.music_button = Button(self.icon_frame, image=self.music_icon, command=self.manage_music, borderwidth=0)
        self.music_button.grid(row=0, column=0, padx=20, pady=10)

        # Fotoğraf ikonu
        self.image_icon = PhotoImage(file="icons/icon_images.png").subsample(6)
        self.image_button = Button(self.icon_frame, image=self.image_icon, command=self.manage_images, borderwidth=0)
        self.image_button.grid(row=1, column=0, padx=20, pady=10)

        # Video ikonu
        self.video_icon = PhotoImage(file="icons/icon_videos.png").subsample(6)
        self.video_button = Button(self.icon_frame, image=self.video_icon, command=self.manage_videos, borderwidth=0)
        self.video_button.grid(row=2, column=0, padx=20, pady=10)

        # Ekran görüntüsü ikonu
        self.screenshot_icon = PhotoImage(file="icons/icon_screenshots.png").subsample(6)
        self.screenshot_button = Button(self.icon_frame, image=self.screenshot_icon, command=self.manage_screenshots, borderwidth=0)
        self.screenshot_button.grid(row=3, column=0, padx=20, pady=10)

        # İndirilenler ikonu
        self.downloads_icon = PhotoImage(file="icons/icon_downloads.png").subsample(6)
        self.downloads_button = Button(self.icon_frame, image=self.downloads_icon, command=self.manage_downloads, borderwidth=0)
        self.downloads_button.grid(row=4, column=0, padx=20, pady=10)

    def create_function_buttons(self):
        button_configs = [
            ("Dosya Aç", self.open_file),
            ("Dosyayı Sil", self.delete_file),
            ("Dosyayı Yeniden Adlandır", self.rename_file),
            ("Dosyayı Kopyala", self.copy_file),
            ("Dosyayı Taşı", self.move_file),
            ("Klasör Oluştur", self.create_folder),
            ("Klasörü Sil", self.delete_folder),
            ("Klasörü Yeniden Adlandır", self.rename_folder),
            ("Klasör İçeriğini Görüntüle", self.view_folder),
            ("Dosya Bilgisi", self.file_info),
            ("Dosyaları Ara", self.search_files),
            ("Çıkış", self.root.destroy)
        ]
        # Btnları iki sütuna yerleştirme:
        for idx, (text, command) in enumerate(button_configs):
            Button(self.button_frame, text=text, command=command, width=20, font=('bold', 14), bg='lightblue', fg='white').grid(row=idx % 6, column=idx // 6, padx=10, pady=10)



    def set_background(self):
        background_image = Image.open("background/bg_seydisehir.jpg")  
        background_image = background_image.resize((1000, 550), Image.LANCZOS)  
        self.background_image = ImageTk.PhotoImage(background_image)  # Tkinter formatına çevirmek için

        background_label = Label(self.root, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)  # Tam ekran kaplaması için


    downloads_files = []  

    def manage_downloads(self):
        action = messagebox.askquestion("İndirilenler Yönetimi", "Yeni bir dosya indirmek ister misiniz?")
        if action == 'yes':
            # Kullanıcıdan dosya seçmesini iste
            file_path = filedialog.askopenfilename()
            if file_path:
                # İndirilenler klasörünün yolunu al
                downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                # Dosyanın adını ve yeni yolunu belirle
                file_name = os.path.basename(file_path)
                destination = os.path.join(downloads_path, file_name)
                # Dosyayı kopyala
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

    def manage_images(self):
        action = messagebox.askquestion("Fotoğraf Yönetimi", "Yeni bir fotoğraf dosyası eklemek ister misiniz?")
        if action == 'yes':
            add_image()
        else:
            image_files = show_image_files()
            if image_files:
                image_list_window = Toplevel(self.root)
                image_list_window.title("Eklenen Fotoğraflar")
                listbox = Listbox(image_list_window, width=50)
                listbox.pack(pady=20)

                for image in image_files:
                    listbox.insert('end', os.path.basename(image))

                Button(image_list_window, text='Kapat', command=image_list_window.destroy).pack(pady=10)

    
    def manage_videos(self):
        action = messagebox.askquestion("Video Yönetimi", "Yeni bir video dosyası eklemek ister misiniz?")
        if action == 'yes':
            add_video()
        else:
            video_files = show_video_files()
            if video_files:
                video_list_window = Toplevel(self.root)
                video_list_window.title("Eklenen Videolar")
                listbox = Listbox(video_list_window, width=50)
                listbox.pack(pady=20)

                for video in video_files:
                    listbox.insert('end', os.path.basename(video))

                Button(video_list_window, text='Kapat', command=video_list_window.destroy).pack(pady=10)


    def populate_c_drive(self):
        c_path = 'C:\\'
        try:
            for item in os.listdir(c_path):
                self.tree.insert(self.c_drive_node, 'end', text=item)
        except Exception as e:
            messagebox.showerror("Hata", f"C sürücüsünü açarken bir hata oluştu: {e}")
        
    def manage_music(self):
        action = messagebox.askquestion("Müzik Yönetimi", "Yeni bir müzik dosyası eklemek ister misiniz?")
        if action == 'yes':
            add_music()  # Müzik dosyası ekle
        else:
            music_files = show_music_files()  # Eklenen müzikleri göster
            if music_files:  # Eğer müzik varsa
                music_list_window = Toplevel(self.root)
                music_list_window.title("Eklenen Müzikler")
                listbox = Listbox(music_list_window, width=50)
                listbox.pack(pady=20)

                for music in music_files:
                    listbox.insert('end', os.path.basename(music))

                Button(music_list_window, text='Kapat', command=music_list_window.destroy).pack(pady=10)

    def manage_screenshots(self):
        action = messagebox.askquestion("Ekran Görüntüsü Yönetimi", "Yeni bir ekran görüntüsü almak ister misiniz?")
        if action == 'yes':
            add_screenshot()
        else:
            screenshot_files = show_screenshot_files()
            if screenshot_files:
                screenshot_list_window = Toplevel(self.root)
                screenshot_list_window.title("Eklenen Ekran Görüntüleri")
                listbox = Listbox(screenshot_list_window, width=50)
                listbox.pack(pady=20)

                for screenshot in screenshot_files:
                    listbox.insert('end', os.path.basename(screenshot))

                Button(screenshot_list_window, text='Kapat', command=screenshot_list_window.destroy).pack(pady=10)




    def list_drives(self):
        drives = [f"{d}:" for d in range(65, 91) if os.path.exists(f"{chr(d)}:")]
        for drive in drives:
            self.drive_listbox.insert(END, drive)

    def open_file(self):
        file = filedialog.askopenfilename()
        if file:
            open_file(file)

    def delete_file(self):
        file = filedialog.askopenfilename()
        if file:
            delete_file(file)

    def rename_file(self):
        file = filedialog.askopenfilename()
        if file:
            new_name = simpledialog.askstring("Dosyayı Yeniden Adlandır", "Yeni dosya adını girin:")
            if new_name:
                rename_file(file, new_name)

    def delete_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            delete_folder(folder)

    def create_folder(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            new_folder_name = simpledialog.askstring("Klasör Oluştur", "Klasör adını girin:")
            if new_folder_name:
                create_folder(dir_path, new_folder_name)

    def rename_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            new_name = simpledialog.askstring("Klasörü Yeniden Adlandır", "Yeni klasör adını girin:")
            if new_name:
                rename_folder(folder, new_name)

    def view_folder(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            files = os.listdir(dir_path)
            file_list_window = Toplevel(self.root)
            file_list_window.title("Klasör İçeriği")
            listbox = Listbox(file_list_window, width=50)
            listbox.pack(pady=20)

            for name in files:
                listbox.insert('end', name)

            Button(file_list_window, text='Kapat', command=file_list_window.destroy).pack(pady=10)

    def file_info(self):
        file = filedialog.askopenfilename()
        if file:
            info = get_file_info(file)
            messagebox.showinfo("Dosya Bilgisi", info)

    def search_files(self):
        search_term = simpledialog.askstring("Dosyaları Ara", "Arama terimini girin:")
        if search_term:
            matching_files = [f for f in os.listdir() if search_term in f]
            messagebox.showinfo("Arama Sonuçları", "\n".join(matching_files) if matching_files else "Dosya bulunamadı.")

    def copy_file(self):
        file = filedialog.askopenfilename()
        dest_dir = filedialog.askdirectory()
        if file and dest_dir:
            copy_file(file, dest_dir)

    def move_file(self):
        file = filedialog.askopenfilename()
        dest_dir = filedialog.askdirectory()
        if file and dest_dir:
            move_file(file, dest_dir)
