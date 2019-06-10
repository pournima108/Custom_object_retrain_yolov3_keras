import os

imdir = 'annotations'
if not os.path.isdir(imdir):
    os.mkdir(imdir)
    print ("dir created")

helmet_txt = [folder for folder in os.listdir('.') if 'helmet_annotations' in folder]
print(helmet_txt)

n = 0
for folder in helmet_txt:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:}.xml'.format(n)))
        print("renaming completed")
        n += 1