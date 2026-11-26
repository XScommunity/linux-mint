#!/usr/bin/env python3
import os
import random
import subprocess
import time
import threading
from pathlib import Path
import tkinter as tk
from tkinter import Label, Canvas

# SUAS URLs DO GITHUB
GITHUB_RAW = "https://raw.githubusercontent.com/XScommunity/linux-mint/main"
WALLPAPER_URL = f"{GITHUB_RAW}/wall.png"
# Se você adicionar mais imagens na pasta images/ do repo, coloca aqui:
BRAINROT_IMAGES = [
    f"{GITHUB_RAW}/wall.png",  # Usando o wall como imagem também por enquanto
    # Adicione mais quando subir as imagens pro repo, ex:
    # f"{GITHUB_RAW}/images/brainrot1.jpg",
    # f"{GITHUB_RAW}/images/skibidi.jpg",
]

DESKTOP = Path.home() / "Desktop"
BRAINROT_FOLDER = DESKTOP / "SISTEMA_INFECTADO"

def setup_infection():
    """Prepara as imagens baixando do seu GitHub"""
    BRAINROT_FOLDER.mkdir(exist_ok=True)
    
    # Baixa o wallpaper
    print("[*] Baixando wallpaper brainrot...")
    wp_path = BRAINROT_FOLDER / "wallpaper.png"
    try:
        subprocess.run(["wget", "-q", WALLPAPER_URL, "-O", str(wp_path)], check=True)
        print("[+] Wallpaper baixado!")
    except:
        print("[!] Falha no download, usando cor sólida nojenta")
    
    # Baixa imagens de brainrot (se tiver no repo)
    for i, url in enumerate(BRAINROT_IMAGES):
        img_path = BRAINROT_FOLDER / f"brainrot_{i}.jpg"
        try:
            subprocess.run(["wget", "-q", url, "-O", str(img_path)], check=True)
        except:
            pass
    
    return wp_path if wp_path.exists() else None

def change_wallpaper(wp_path):
    """Troca o wallpaper sem precisar de admin"""
    if not wp_path:
        return
    
    uri = f"file://{wp_path.absolute()}"
    # Tenta Cinnamon (padrão do Mint)
    try:
        subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", uri])
        subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-options", "scaled"])
    except:
        pass
    
    # Tenta MATE
    try:
        subprocess.run(["gsettings", "set", "org.mate.background", "picture-filename", str(wp_path.absolute())])
    except:
        pass
    
    # Tenta XFCE
    try:
        subprocess.run(["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-path", "-s", str(wp_path)])
    except:
        pass
    
    print("[+] Wallpaper trocado!")

def create_fake_errors():
    """Cria arquivos de erro assustadores (mas inofensivos)"""
    errors = [
        ("ERRO_FATAl_BRAINROT.txt", "SEU SISTEMA FOI INFECTADO PELO VÍRUS SKIBIDI!\n\nPara remover: dance a dança do fortnite por 10 horas."),
        ("SISTEMA_CORROMPIDO.log", "[00:00] Inicializando brainrot.dll\n[00:01] Corrompendo memória com imagens de Ohio\n[00:02] Falha crítica: Sigma levels too high"),
        ("VIRUS_DETECTADO.bat", "@echo off\necho VOCÊ FOI HACKEADO PELO BRAINROT\necho Seu PC agora pertence ao Skibidi Toilet\npause"),
        ("LEIA_ISSO_URGENTE.txt", "PARABÉNS!\n\nVocê acaba de ganhar 1 ano de brainrot grátis!\nResgate em: www.skibidi-ohio-sigma.com"),
    ]
    
    for name, content in errors:
        (DESKTOP / name).write_text(content)
    
    # Cria mais 30 arquivos aleatórios
    for i in range(30):
        name = f"BRAINROT_{random.randint(1000,9999)}.sys"
        (DESKTOP / name).write_text("skibidi" * 100)

def fullscreen_gallery():
    """Slideshow fullscreen de brainrot com suas imagens"""
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.configure(bg='black')
    
    # Tenta carregar as imagens baixadas
    images = []
    try:
        from PIL import Image, ImageTk
        for img_file in BRAINROT_FOLDER.glob("brainrot_*.jpg"):
            try:
                img = Image.open(img_file)
                img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
                images.append(ImageTk.PhotoImage(img))
            except:
                pass
    except ImportError:
        pass  # Sem Pillow, usa texto mesmo
    
    label = Label(root, bg="black")
    label.pack(expand=True)
    
    messages = [
        "🚽 SKIBIDI TOILET 🚽",
        "SIGMA BOY GRINDSET",
        "VOCÊ ESTÁ NO OHIO!",
        "GRIMACE SHAKE ENERGIA",
        "TUNG TUNG TUNG SAHUR",
        "TRALALERO TRALALA",
        "MANGO MANGO MANGO",
        "BOMBARDIRO CROCODILO"
    ]
    
    def show_next():
        if images and random.random() > 0.3:
            # Mostra imagem do seu GitHub
            img = random.choice(images)
            label.config(image=img, text="")
        else:
            # Mostra texto berrante
            label.config(image="", 
                        text=random.choice(messages),
                        font=("Arial", random.randint(30, 80), "bold"),
                        fg=random.choice(["red", "lime", "yellow", "cyan", "magenta"]),
                        bg="black")
        root.after(800, show_next)
    
    show_next()
    root.mainloop()

def popup_bomb():
    """Janelas que fogem do mouse"""
    popups = []
    
    def create_popup():
        popup = tk.Toplevel()
        popup.title("⚠️ ALERTA DE SEGURANÇA ⚠️")
        popup.geometry("400x200")
        popup.attributes('-topmost', True)
        popup.configure(bg="yellow")
        
        msg = Label(popup, 
                   text="VÍRUS BRAINROT DETECTADO!\n\nAmeaças encontradas:\n• Skibidi Toilet\n• Ohio Virus\n• Sigma Malware",
                   font=("Arial", 12, "bold"),
                   fg="red", bg="yellow")
        msg.pack(expand=True)
        
        def flee(event):
            x = random.randint(0, popup.winfo_screenwidth()-400)
            y = random.randint(0, popup.winfo_screenheight()-200)
            popup.geometry(f"+{x}+{y}")
        
        popup.bind("<Enter>", flee)
        popups.append(popup)
    
    # Cria 15 popups iniciais
    for _ in range(15):
        create_popup()
        time.sleep(0.2)
    
    # Spawna mais a cada 5 segundos
    def spam():
        while True:
            time.sleep(5)
            create_popup()
    
    threading.Thread(target=spam, daemon=True).start()

def mouse_ghost():
    """Cria fantasmas do mouse que seguem com atraso"""
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.attributes('-transparentcolor', 'white')
    root.configure(bg='white')
    
    canvas = Canvas(root, bg='white', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    ghosts = []
    for i in range(8):
        ghost = canvas.create_text(0, 0, text="🖱️", font=("Arial", 24))
        ghosts.append(ghost)
    
    def follow():
        mx, my = root.winfo_pointerx(), root.winfo_pointery()
        for i, ghost in enumerate(ghosts):
            # Cada fantasma tem velocidade diferente
            speed = 0.1 - (i * 0.01)
            coords = canvas.coords(ghost)
            if coords:
                dx = (mx - coords[0]) * speed
                dy = (my - coords[1]) * speed
                canvas.move(ghost, dx, dy)
        root.after(30, follow)
    
    follow()
    root.mainloop()

def main():
    print("""
    ╔══════════════════════════════════════╗
    ║     BRAINROT PRANK v2.0 - GITHUB     ║
    ║     Repositório: XScommunity/linux-mint ║
    ╚══════════════════════════════════════╝
    """)
    
    # 1. Baixa suas imagens do GitHub
    wp_path = setup_infection()
    
    # 2. Troca o wallpaper
    change_wallpaper(wp_path)
    
    # 3. Cria arquivos falsos na Área de Trabalho
    create_fake_errors()
    print("[+] Área de trabalho contaminada com 34 arquivos suspeitos")
    
    time.sleep(2)
    print("[*] Iniciando ataques visuais...")
    
    # 4. Inicia o caos em threads
    threading.Thread(target=fullscreen_gallery, daemon=True).start()
    time.sleep(1)
    threading.Thread(target=popup_bomb, daemon=True).start()
    time.sleep(1)
    threading.Thread(target=mouse_ghost, daemon=True).start()
    
    print("[!] PRANK ATIVO - Pressione Ctrl+C para encerrar (ou faça logoff)")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[✓] Prank encerrado. Seu amigo já está traumatizado.")

if __name__ == "__main__":
    main()
