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

path_exemple_negative = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\ExempleNegative\\"
        
f = open(andy_addnotations_path,"r")
dictionar_file_annotations = {}
lines = f.readlines()
for line in lines: 
    line = line.split()
    if line[0] not in dictionar_file_annotations.keys():
        dictionar_file_annotations[line[0]]=[]
        dictionar_file_annotations[line[0]].append([int(line[1]),int(line[2]),int(line[3]),int(line[4])])
    else:
        dictionar_file_annotations[line[0]].append([int(line[1]),int(line[2]),int(line[3]),int(line[4])])

def overlap(x1_min,y1_min,x1_max,y1_max,x2_min,y2_min,x2_max,y2_max):
    if y1_min>y2_max or y2_min>y1_max:
        return False
    if x1_max>x2_min or x2_max>x1_min:
        return False
    return True

def memoreazaExempleNegative(path_ex_negative,image_folder,dictionar):
    files = os.listdir(image_folder)
    index=0
    for file in files:
        if(file[-3:]=="jpg"):
            img = cv.imread(image_folder+file)
            number_of_rows = img.shape[1]
            number_of_cols = img.shape[0]
            ok = 0
            index+=1
            time_spent = 0
            while ok == 0:
                x_min = np.random.randint(0,number_of_rows-75)
                y_min = np.random.randint(0,number_of_cols-75)
                x_max = x_min+72
                y_max = y_min+72
                time_spent+=1
                if time_spent>10000:
                    x_min = np.random.randint(0,number_of_rows-22)
                    y_min = np.random.randint(0,number_of_cols-22)
                    x_max = x_min+20
                    y_max = y_min+20
                    print(time_spent)
                number_of_faces = 0
                for list in dictionar[file]:
                    if(overlap(-x_min,y_min,-x_max,y_max,-list[0],list[1],-list[2],list[3])==False):
                        number_of_faces+=1
                if number_of_faces == len(dictionar[file]):
                    ok=1
                    # print(y_min,y_max,x_min,x_max)
                    # show_image("patchNeg",img[y_min:y_max,x_min:x_max])
                    patch = img[y_min:y_max,x_min:x_max]
                    patch = cv.resize(patch,(72,72))
                    cv.imwrite(path_ex_negative+"negEx_"+str(index)+".jpg",patch)


# memoreazaExempleNegative(path_exemple_negative,andy_path,dictionar_file_annotations)