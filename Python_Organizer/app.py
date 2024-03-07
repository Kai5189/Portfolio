import os
import collections
from pprint import pprint

Move_Audio = ['mp3','wav','raw','wna','nid','midi']
Move_Video = ['mp4','mpg','mpeg','avi','mov','flv','mkv','nmv','m4v','h264']
Move_Imgs = ['png','jpg','jpeg','gif','svg','bmp','psd','tiff','tif','pictures']
Move_Docs = ['txt','pdf','csv','xls','xlsx','ods','doc','docx','html','odt','tex','ppt','pptx','log','to','crdownload','nl','py','pyprompt testing',
             'pem','opera','msi','nl','nro','mobileconfig','jar-infection-scanner','ics','ini','dol','cert','Webview2','Slidesgpt','bin','new folder',
             'xltx','vbs','ups','sha256']
Move_DB = ['db']
Move_Mods = ['jar']
Move_Games = ['gba','nds','xcl','gb', 'gbc', 'nps', 'cia','mcworld','mcpack','mcaddon']
Move_Compress = ['zip','z','7z','rar','tar','gz','rpm','pkg','deb']
Move_Install = ['dmg','exe','iso']
Move_Schems = ['schem', 'schematic']



Base_Path = os.path.expanduser('~'+ "/Downloads/")
Dest_Dirs = ['Music', 'Movie', 'Pictures', 'Documents', 'Compression', 'Installs','Games','DB','Schems','Minecraft_Mods','Unorganized']

for d in Dest_Dirs:
    dir_path = os.path.join(Base_Path,d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


DW_Path = os.path.join(Base_Path)
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DW_Path)

print(files_mapping)
print(files_list)

for file_name in files_list:
  if file_name[0] != '.':
    file_ext = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)

    pprint(files_mapping)


for f_ext,f_list in files_mapping.items():


    if f_ext in Move_Install:
        for file in f_list:
            os.rename(os.path.join(DW_Path,file), os.path.join(Base_Path,'Installs',file))
    
    elif f_ext in Move_Audio:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file), os.path.join(Base_Path,'Music',file))

    elif f_ext in Move_Video:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Movie',file))

    elif f_ext in Move_Imgs:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Pictures',file))

    elif f_ext in Move_Docs:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Documents',file))

    elif f_ext in Move_DB:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'DB',file))

    elif f_ext in Move_Mods:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Minecraft_Mods',file))

    elif f_ext in Move_Games:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Games',file))

    elif f_ext in Move_Compress:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Compression',file))

    elif f_ext in Move_Schems:
       for file in f_list:
          os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Schems',file))

    else:
        for file in f_list:
           os.rename(os.path.join(DW_Path,file),os.path.join(Base_Path,'Unorganized',file))
