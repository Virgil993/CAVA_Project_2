import os

class Parameters:
    def __init__(self):
        self.base_dir = 'D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\data'
        self.dir_pos_examples = os.path.join(self.base_dir, 'exemplePozitive/ExemplePozitiveTotale')
        self.dir_neg_examples = os.path.join(self.base_dir, 'exempleNegative')
        self.dir_test_examples = os.path.join(self.base_dir,'exempleTest/Validare')
        self.path_annotations = os.path.join(self.base_dir, 'exempleTest/Validare_adnotari/task1_gt_validare.txt')
        self.dir_save_files = os.path.join(self.base_dir, 'salveazaFisiere')
        if not os.path.exists(self.dir_save_files):
            os.makedirs(self.dir_save_files)
            print('directory created: {} '.format(self.dir_save_files))
        else:
            print('directory {} exists '.format(self.dir_save_files))

        # directorul in care vor fi salvate solutiile sub format npy pentru a fi procesate de scriptul evalueaza_solutie
        self.dir_save_solutions = "D:\Materiale Pentru Facultate\Concepte Si Aplicatii in Vederea Artificiala\CAVA_Project_2\Project_2\evaluare\\fisiere_solutie\\333_Virgil_Turcu\\"
        self.dir_save_solutions_task1 = os.path.join(self.dir_save_solutions,"task1")

        # set the parameters
        self.dim_window = 72  # exemplele pozitive (fete de oameni cropate) au 36x36 pixeli
        self.dim_hog_cell = 6  # dimensiunea celulei
        self.dim_descriptor_cell = 72  # dimensiunea descriptorului unei celule
        self.overlap = 0.3
        self.number_positive_examples = 4907  # numarul exemplelor pozitive
        self.number_negative_examples = 10000  # numarul exemplelor negative
        self.overlap = 0.3
        self.has_annotations = False
        self.threshold = 0