import glob
import cv2 as cv
import numpy as np
from copy import deepcopy
import os

andy_path = 'D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\\andy\\'
louie_path = 'D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\\louie\\'
ora_path = 'D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\ora\\'
tommy_path = 'D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\\tommy\\'

andy_addnotations_path= "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\\andy_annotations.txt" 
louie_addnotations_path = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\louie_annotations.txt"
ora_addnotations_path = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\ora_annotations.txt"
tommy_addnotations_path = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\\antrenare\\tommy_annotations.txt"

def show_image(title, image):
    # image = cv.resize(image, (0, 0), fx=0.3, fy=0.3)
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

path_exemple_pozitive_andy = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\ExemplePozitive\ExemplePozitiveAndy\\"

f = open(andy_addnotations_path,"r")
lines_andy = f.readlines()

def memoreazaExemplePozitive(path_ex_poz):
    files = os.listdir(andy_path)
    index=0
    for file in files:
        if(file[-3:]=="jpg"):
            img = cv.imread(andy_path+file)
            current_annotation = lines_andy[index].split()
            ok = 0
            while(current_annotation[0]!=file or current_annotation[5]!="andy"):
                if(current_annotation[0] > file):
                    ok=1
                    break
                current_annotation = lines_andy[index].split()
                index+=1
            if(ok == 1):
                continue
            x_min = int(current_annotation[1])
            y_min = int(current_annotation[2])
            x_max = int(current_annotation[3])
            y_max = int(current_annotation[4])

            patch = img[y_min:y_max,x_min:x_max]
            patch = cv.resize(patch,(72,72))
            cv.imwrite(path_ex_poz+"andy_"+str(index)+".jpg",patch)


# memoreazaExemplePozitive(path_exemple_pozitive_andy)

        
            
