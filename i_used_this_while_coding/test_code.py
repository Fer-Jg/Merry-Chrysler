from ursina import *
import ursina as u


from os import path

app = Ursina()
window.color = color.black

from ursina.shaders import basic_lighting_shader
# tree = Entity(model=Cone(), color='#1d591e', scale=3, shader=basic_lighting_shader)
# tree.model.generate_normals()
fake_light = Entity(model='quad', texture='radial_gradient', parent=None, y=1, billboard=True, color=color.yellow, render_queue=1, alpha=.5)

counter = 0
def update():
    global counter
    counter +=1
    fake_light.scale = 0 + 2 * sin(counter * 0.005)


import subprocess
from os import path
from requests import get as gimmeMyRequest

global icon_file
icon_file = "icon.ico"
def download_icon(self):
    download_stuff = not path.exists(icon_file)
    
    if download_stuff:
        url = "https://cdn3d.iconscout.com/3d/premium/thumb/python-6815592-5602757.png"
        req = gimmeMyRequest(url)
        with open(icon_file, "wb") as file:
            file.write(req.content)
    icoed_icon = icon_file.replace(".png",".ico")
    print(f"{icoed_icon} {not path.exists(icoed_icon)}")
    if not path.exists(icoed_icon):
        subprocess.run(['convert', icon_file, icoed_icon])

global bg_music_name
global bg_music
def download_music(self):
    global bg_music_name
    bg_music_name = "Best_Chrimu_Song.mp3"
    
    download_stuff = not path.exists(bg_music_name)
    # If there is no mp3 file we should just avoid requests and other processes, right?
    if download_stuff:
        url = "https://cdn.trendybeatz.com/audio/Mariah-Carey-All-I-Want-For-Christmas-Is-You-(TrendyBeatz.com).mp3"
        download = gimmeMyRequest(url)
    
    # All utility names
    initial_output_name = "fix_" + bg_music_name.replace(".mp3",".wav")
    fixed_output_name = initial_output_name.replace("fix_","")
    bg_music_name = fixed_output_name

    # Actually download the song, but in a mp3 format, so let's fix that later...
    if download_stuff:
        with open(bg_music_name, "wb") as f:    f.write(download.content)

    # Make song a wav file
    subprocess.run(['ffmpeg', '-y', '-i', bg_music_name, initial_output_name], 
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Cut the wav file from the first 7.5 seconds because the download site has some annoying ad through that bit
    subprocess.run(['ffmpeg', '-y', '-i', initial_output_name, '-ss', '00:00:07.5', '-c', 'copy', fixed_output_name], 
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def play_music(self):
    global bg_music_name
    global bg_music
    bg_music = Audio(
            bg_music_name,
            volume=.2,
            loop = True,
            autoplay = True,
            enabled = [])

# music_t = 0
# def input(key):
#     global bg_music
#     global music_t
#     if key == 'e':
#         if bg_music.playing:
#             music_t = bg_music.time
#             bg_music.stop(destroy=False)
#         else:
#             print(music_t)
#             bg_music.play(start=music_t)

download_music(0)
# play_music(0)
download_icon(0)

# Blender object
# blend = u.load_model("chrimu_star.blend")
# obj = u.Entity(model=blend, color=u.color.green, shader=basic_lighting_shader)


EditorCamera()

app.run()