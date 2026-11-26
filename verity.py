#!/usr/bin/env python3
import os
import random
import subprocess
import time
import threading
from pathlib import Path

# CONFIGURAÇÕES
BRAINROT_IMAGES = [
    "https://i.imgur.com/8Km9tLL.jpg",  # Exemplo de meme (substitua por URLs de brainrot reais)
    "https://i.imgur.com/2y9QwqL.jpg",
    "https://i.imgur.com/5bGzZ.jpg",
    "https://i.imgur.com/3jKfL.jpg"
]
DESKTOP = Path.home() / "Desktop" / "BRAINROT_ZONE"
WALLPAPER_URL = "https://i.imgur.com/BrainrotWallpaper.jpg"  # Coloque uma URL de wallpaper brainrot

def setup():
    DESKTOP.mkdir(exist_ok=True)
    os.chdir(DESKTOP)
    
    # Baixa imagens de brainrot
    for i, url in enumerate(BRAINROT_IMAGES):
        try:
            subprocess.run(["wget", "-q", url, "-O", f"brainrot_{i}.jpg"], check=True)
        except:
            # Se não tiver internet, cria arquivos de texto com nomes engraçados
            with open(f"brainrot_{i}.txt", "w") as f:
                f.write("SKIBIDI TOILET É VIDA! 🚽")

def change_wallpaper():
    # Troca o wallpaper (funciona no Mint com Cinnamon/MATE/XFCE)
    wallpaper_path = DESKTOP / "wallpaper_brainrot.jpg"
    try:
        subprocess.run(["wget", "-q", WALLPAPER_URL, "-O", str(wallpaper_path)], check=True)
        # Comandos para diferentes DEs do Mint
        subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", f"file://{wallpaper_path}"])
        subprocess.run(["gsettings", "set", "org.mate.background", "picture-filename", str(wallpaper_path)])
        subprocess.run(["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-path", "-s", str(wallpaper_path)])
    except Exception as e:
        print(f"Erro no wallpaper: {e}")

def spawn_sliding_windows():
    # Cria janelas deslizantes com tkinter (sem dependências externas)
    import tkinter as tk
    from tkinter import Label
    
    def create_window():
        root = tk.Tk()
        root.title("BRAINROT ALERT")
        root.geometry("300x100")
        root.attributes('-topmost', True)
        
        # Remove decoração da janela pra ficar mais estranho
        root.overrideredirect(True)
        
        label = Label(root, text="🧠 BRAINROT DETECTED! 🧠\nSKIBIDI SKIBIDI!", 
                     font=("Arial", 12, "bold"), bg="yellow", fg="red")
        label.pack(expand=True)
        
        # Faz a janela deslizar pela tela
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        x = random.randint(0, screen_w - 300)
        y = random.randint(0, screen_h - 100)
        
        def slide():
            nonlocal x, y
            x += random.randint(-5, 5)
            y += random.randint(-3, 3)
            root.geometry(f"+{x}+{y}")
            root.after(50, slide)
        
        slide()
        root.mainloop()
    
    # Spawna várias threads com janelas
    for _ in range(5):
        threading.Thread(target=create_window, daemon=True).start()
        time.sleep(0.5)

def invert_colors_simulation():
    # Simula inversão de cores piscando a tela (sem precisar de permissões de root)
    # Cria um overlay fullscreen que pisca
    try:
        import tkinter as tk
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.config(bg="black")
        
        colors = ["black", "white", "red", "blue", "green", "purple"]
        def flash():
            root.config(bg=random.choice(colors))
            root.after(100, flash)
        
        flash()
        root.mainloop()
    except:
        pass

def spawn_error_icons():
    # Cria arquivos de erro falsos na área de trabalho
    errors = [
        "ERRO_CRITICO_BRAINROT.txt",
        "SISTEMA_CORROMPIDO_POR_SKIBIDI.log",
        "VIRUS_ITALIAN_BRAINROT.exe",
        "NAO_ABRA_ISSO.bat"
    ]
    for error in errors:
        with open(DESKTOP / error, "w") as f:
            f.write("Seu PC foi infectado pelo vírus Brainrot! 🧠💀\n"
                   "Para remover, cante a música do Skibidi Toilet 3 vezes.")

def mouse_clone_effect():
    # Cria cursores fantasmas que seguem o mouse com delay (efeito visual)
    try:
        import tkinter as tk
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.config(bg="")
        root.attributes('-transparentcolor', "white")
        
        canvas = tk.Canvas(root, bg="white", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        ghosts = []
        for i in range(5):
            ghost = canvas.create_text(0, 0, text="🖱️", font=("Arial", 20))
            ghosts.append((ghost, i * 0.1))
        
        def follow_mouse():
            x, y = root.winfo_pointerx(), root.winfo_pointery()
            for ghost, delay in ghosts:
                # Cada fantasma segue com um "atraso" diferente
                canvas.move(ghost, (x - canvas.coords(ghost)[0]) * 0.1, 
                           (y - canvas.coords(ghost)[1]) * 0.1)
            root.after(20, follow_mouse)
        
        follow_mouse()
        root.mainloop()
    except:
        pass

def main():
    print("Iniciando Brainrot Prank... 🧠")
    
    # 1. Prepara arquivos
    setup()
    
    # 2. Troca wallpaper
    change_wallpaper()
    
    # 3. Spawna ícones de erro
    spawn_error_icons()
    
    # 4. Inicia efeitos visuais em threads separadas
    threading.Thread(target=spawn_sliding_windows, daemon=True).start()
    time.sleep(2)
    
    threading.Thread(target=invert_colors_simulation, daemon=True).start()
    time.sleep(2)
    
    threading.Thread(target=mouse_clone_effect, daemon=True).start()
    
    # Mantém o script rodando
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrank encerrado!")

if __name__ == "__main__":
    main()
