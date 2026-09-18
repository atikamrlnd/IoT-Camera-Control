# IoT Camera Control Studio

A camera application built with **Python, OpenCV, and Tkinter** for displaying a live camera preview, adjusting image parameters via software, and capturing both single and burst photos.

## Features

* Real-time live camera preview
* Resolution options:

  * `640x480`
  * `1280x720 (HD)`
  * `1920x1080 (FHD)`
* Software-based **Exposure / Brightness** control
* Software-based **ISO / Gain Multiplier** control
* Single capture using `Spacebar`
* Burst capture by holding `Spacebar`
* Photos automatically saved to the `captured_images` folder
* `ESC` to exit the application
* Reset camera parameters back to normal

## Project Structure

```text
project/
│
├── .venv/
│   └── Python virtual environment
│
├── captured_images/
│   └── Folder for saved photos
│
├── camera.py
│   └── Main camera application
│
└── README.md
    └── Project documentation
```

## Tech Stack

* **Python 3**
* **OpenCV** — camera access and image processing
* **Tkinter** — graphical user interface
* **Pillow (PIL)** — displaying OpenCV frames in Tkinter
* **NumPy** — image array processing

## Installation

Make sure **Python 3** is installed on your computer.

### 1. Clone the repository

```bash
git clone https://github.com/atikamrlnd/IoT-Camera-Control.git
cd IoT-Camera-Control
```

### 2. Create a virtual environment

If `.venv` doesn't exist yet:

**Windows:**

```bash
python -m venv .venv
```

**Linux / macOS:**

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**Windows — Command Prompt:**

```bash
.venv\Scripts\activate
```

**Windows — PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Once activated, your terminal will usually show:

```text
(.venv)
```

### 4. Install dependencies

```bash
pip install opencv-python pillow numpy
```

> `tkinter` is usually bundled with Python on Windows. On some Linux distros, Tkinter needs to be installed separately via the system package manager.

## Running the Application

Make sure the virtual environment is active, then run:

```bash
python camera.py
```

If your system uses `python3`:

```bash
python3 camera.py
```

The **IoT Camera Control Studio** window will open and use your computer's default camera.

## Camera Controls

| Control          | Function                                  |
| ---------------- | ------------------------------------------ |
| `Spacebar` press | Take a single photo                        |
| `Spacebar` hold  | Burst capture                              |
| `ESC`            | Exit the application                       |
| Resolution       | Change camera resolution                   |
| Exposure         | Adjust brightness/exposure via software    |
| ISO / Gain       | Adjust image brightness gain               |
| Reset Parameter  | Restore parameters to their default values |

## Captured Photos

Captured photos are automatically saved to:

```text
captured_images/
```

File naming format:

```text
IMG_YYYYMMDD_HHMMSS_mmm.jpg
```

Example:

```text
IMG_20260918_081530_125.jpg
```

## Troubleshooting

### Camera not found

If you see the message:

```text
Camera not found or failed to access!
```

make sure:

1. The camera is connected to the computer.
2. The camera isn't being used by another application like Zoom, Google Meet, or another camera app.
3. Camera permission has been granted to Python/the application.
4. Try closing other applications currently using the camera.
5. Confirm the camera is detected by the operating system.

### Can't activate `.venv` in PowerShell

If PowerShell refuses to run the script, open PowerShell as the appropriate user and run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate it again:

```powershell
.venv\Scripts\Activate.ps1
```

## Notes

The **Exposure** and **ISO / Gain** parameters in this application are processed on the image after the frame is captured from the camera. This means these adjustments are **software-based image processing**, not direct changes to the camera's hardware shutter speed or ISO.

The selected resolution also depends on the camera's capabilities and the driver in use. The camera may return a different resolution if the requested one isn't supported by the hardware.

---

## Development

This project was built as a simple application for **camera control, image processing, and a Python-based GUI**.

```text
Python
   │
   ├── OpenCV ─────── Camera & Image Processing
   │
   ├── NumPy ──────── Image Matrix Processing
   │
   ├── Pillow ─────── Image Conversion
   │
   └── Tkinter ────── Graphical User Interface
```

**Main file:**

```text
camera.py
```

**Output directory:**

```text
captured_images/
```
