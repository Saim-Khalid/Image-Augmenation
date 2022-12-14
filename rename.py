import os
import glob

def main():
    path = "Add Dataset Path/" # path to your dataset
    suffix = '.png' #change to any Image format
    files = glob.glob(path + '*' + suffix)
    for idx, filename in enumerate(sorted(files)):
        os.rename(
            filename,
            os.path.join(path, f"({1471 + idx})" + suffix) #add the starting number
        )

if __name__=="__main__":
    main()
