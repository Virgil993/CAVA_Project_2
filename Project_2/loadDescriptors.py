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
path_exemple_pozitive_louie = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\ExemplePozitive\ExemplePozitiveLouie\\"
path_exemple_pozitive_ora = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\ExemplePozitive\ExemplePozitiveOra\\"
path_exemple_pozitive_tommy = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\ExemplePozitive\ExemplePozitiveTommy\\"
path_exemple_pozitive_unknown = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\ExemplePozitive\ExemplePozitiveUnknown\\"

def memoreazaExemplePozitive(path_ex_poz,image_folder,lines,unique):
    files = os.listdir(image_folder)
    index=0
    for file in files:
        if(file[-3:]=="jpg"):
            img = cv.imread(image_folder+file)
            current_annotation = lines[index].split()
            ok = 0
            while(current_annotation[0]!=file or current_annotation[5]!="unknown"):
                if(current_annotation[0] > file):
                    ok=1
                    break
                current_annotation = lines[index].split()
                index+=1
            if(ok == 1):
                continue
            x_min = int(current_annotation[1])
            y_min = int(current_annotation[2])
            x_max = int(current_annotation[3])
            y_max = int(current_annotation[4])

            patch = img[y_min:y_max,x_min:x_max]
            patch = cv.resize(patch,(72,72))
            cv.imwrite(path_ex_poz+"unknown_"+str(index)+unique+".jpg",patch)

# f = open(tommy_addnotations_path,"r")
# lines = f.readlines()
# memoreazaExemplePozitive(path_exemple_pozitive_unknown,tommy_path,lines,"0004")

        
            
