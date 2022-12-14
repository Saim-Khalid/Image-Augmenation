import os
import glob

def main():
    path = "/Users/saimkhalid/Documents/iOPTIME Resources/Tuber Dataset/Data_Augmentation/Augmented_dataset/Random Brightness Contrast/"
    suffix = '.png'
    files = glob.glob(path + '*' + suffix)
    for idx, filename in enumerate(sorted(files)):
        os.rename(
            filename,
            os.path.join(path, f"({1471 + idx})" + suffix)
        )

if __name__=="__main__":
    main()
#0