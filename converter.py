from PIL import Image
import sys, os
import pathlib as pl

from_folder = str()
to_folder=str()

from_folder, to_folder = sys.argv[1], sys.argv[2]

while True:
    try:    
        if not os.path.exists(from_folder):
            raise FileNotFoundError
        if not os.path.exists(to_folder):
            os.mkdir(to_folder)
    except FileNotFoundError as er1:
        print(f"No folder {from_folder} found.")
        sys.exit()
    except OSError as er2:
        print("Inappropriate folder name")
    else:
        print(f"Converting from {from_folder} and saving in {to_folder}")
        break

from_dir=pl.Path.cwd() / from_folder
to_dir=pl.Path.cwd() / to_folder

pathlist=pl.Path(str(from_dir)).glob("**/*.jpg")

im=0

for path in pathlist:
    while True:
        try:
            im=Image.open(path)
        except OSError as er3:
            print("Could not open file.")
        except FileNotFoundError as er4:
            raise OSError
        else:
            im.save(str(to_dir) + "/" + path.stem + ".png" , format="PNG")
            break