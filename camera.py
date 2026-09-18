import cv2
import os
from datetime import datetime
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("1000x700")

        self.cap = None
        self.is_bursting = False
        self.output_dir = "captured_images"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Matriks Resolusi Standard
        self.resolutions = {
            "640x480": (640, 480),
            "1280x720 (HD)": (1280, 720),
            "1920x1080 (FHD)": (1920, 1080)
        }

        # Parameter Kontrol Software (Mencegah Bug Driver Hardware)
        self.exposure_val = 0.0  # Range: -100 s.d 100 (Brightness/Exposure)
        self.iso_gain_val = 1.0   # Range: 0.5 s.d 3.0 (Gain/ISO Multiplier)

        # Inisialisasi Kamera Pertama Kali
        if not self.init_camera(640, 480):
            messagebox.showerror("Error", "Kamera tidak ditemukan atau gagal diakses!")
            self.window.destroy()
            return

        self._build_gui()

        # Keyboard Binding
        self.window.bind('<KeyPress>', self.on_key_press)
        self.window.bind('<KeyRelease>', self.on_key_release)

        # Loop Frame
        self.update_frame()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def init_camera(self, width, height):
        """Inisialisasi ulang aliran kamera dengan aman."""
        if self.cap is not None:
            self.cap.release()

        # Gunakan MSMF atau default backend agar stabil
        self.cap = cv2.VideoCapture(0, cv2.CAP_ANY)
        if not self.cap.isOpened():
            return False

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        return True

    def _build_gui(self):
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Preview Frame
        self.canvas = tk.Canvas(main_frame, bg="black", width=640, height=480)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Control Panel
        control_panel = ttk.LabelFrame(main_frame, text=" Parameter Kamera ")
        control_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=5)

        # 1. Resolusi
        ttk.Label(control_panel, text="Resolusi Stream:").pack(anchor=tk.W, padx=10, pady=(10, 2))
        self.res_combo = ttk.Combobox(control_panel, values=list(self.resolutions.keys()), state="readonly")
        self.res_combo.current(0)
        self.res_combo.pack(fill=tk.X, padx=10, pady=2)
        self.res_combo.bind("<<ComboboxSelected>>", self.change_resolution)

        # 2. Exposure / Shutter Speed (Software Level)
        ttk.Label(control_panel, text="Shutter Speed / Exposure:").pack(anchor=tk.W, padx=10, pady=(15, 2))
        self.exposure_slider = ttk.Scale(control_panel, from_=-100, to=100, value=0, command=self.change_exposure)
        self.exposure_slider.pack(fill=tk.X, padx=10, pady=2)

        # 3. ISO / Gain (Software Level)
        ttk.Label(control_panel, text="ISO / Gain Multiplier:").pack(anchor=tk.W, padx=10, pady=(15, 2))
        self.iso_slider = ttk.Scale(control_panel, from_=0.5, to=3.0, value=1.0, command=self.change_iso)
        self.iso_slider.pack(fill=tk.X, padx=10, pady=2)

        # Tombol Reset
        btn_reset = ttk.Button(control_panel, text="Reset Parameter Manual", command=self.reset_parameters)
        btn_reset.pack(fill=tk.X, padx=10, pady=15)

        # Info Binding
        info_frame = ttk.LabelFrame(control_panel, text=" Key Mapping ")
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        ttk.Label(info_frame, text="• Spacebar (Tekan) : Single Capture\n• Spacebar (Tahan) : Burst Capture\n• ESC : Keluar Aplikasi", justify=tk.LEFT).pack(padx=10, pady=10)

    # --- Parameter Handlers ---
    def change_resolution(self, event):
        selected = self.res_combo.get()
        w, h = self.resolutions[selected]
        self.init_camera(w, h)

    def change_exposure(self, val):
        self.exposure_val = float(val)

    def change_iso(self, val):
        self.iso_gain_val = float(val)

    def reset_parameters(self):
        """Reset parameter kembali ke nilai netral secara instan."""
        self.exposure_val = 0.0
        self.iso_gain_val = 1.0
        self.exposure_slider.set(0)
        self.iso_slider.set(1.0)

    def apply_image_processing(self, frame):
        """Memproses Exposure & ISO pada matriks piksel secara real-time (Aman dari Bug Hardware)."""
        # alpha = Gain/ISO (1.0 = normal), beta = Exposure/Brightness (0 = normal)
        processed = cv2.convertScaleAbs(frame, alpha=self.iso_gain_val, beta=self.exposure_val)
        return processed

    # --- Key Events & Burst Capture ---
    def on_key_press(self, event):
        if event.keysym == 'space':
            if not self.is_bursting:
                self.is_bursting = True
                self.capture_image()
        elif event.keysym == 'Escape':
            self.on_closing()

    def on_key_release(self, event):
        if event.keysym == 'space':
            self.is_bursting = False

    def capture_image(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Terapkan efek parameter ke hasil foto yang disimpan
                final_frame = self.apply_image_processing(frame)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
                filename = os.path.join(self.output_dir, f"IMG_{timestamp}.jpg")
                cv2.imwrite(filename, final_frame)
                print(f"[SAVED] {filename}")

    # --- Live Preview Loop ---
    def update_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                if self.is_bursting:
                    self.capture_image()

                # Processing Gambar
                processed_frame = self.apply_image_processing(frame)
                cv2_image = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

                if self.is_bursting:
                    cv2.putText(cv2_image, "BURST CAPTURING...", (20, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                # Convert ke Tkinter Format
                img = Image.fromarray(cv2_image)
                img = img.resize((640, 480), Image.Resampling.LANCZOS)
                imgtk = ImageTk.PhotoImage(image=img)

                self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
                self.canvas.imgtk = imgtk

        self.window.after(30, self.update_frame)

    def on_closing(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root, "IoT Camera Control Studio")
    root.mainloop()
