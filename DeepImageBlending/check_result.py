import cv2
import matplotlib.pyplot as plt

def visual_txt_annotation_check(img_path, annotation_path):

        colors = {

            0:[110, 64, 170], 1:[143, 61, 178], 2:[178, 60, 178], 3:[210, 62, 167],

            4:[238, 67, 149], 5:[255, 78, 125], 6:[255, 94, 99],  7:[255, 115, 75],

            8:[255, 140, 56], 9:[239, 167, 47], 10:[217, 194, 49], 11:[194, 219, 64],

            12:[175, 240, 91], 13:[135, 245, 87], 14:[96, 247, 96],  15:[64, 243, 115],

            16:[40, 234, 141], 17:[28, 219, 169], 18:[26, 199, 194], 19:[33, 176, 213],

            20:[47, 150, 224], 21:[65, 125, 224], 22:[84, 101, 214], 23:[99, 81, 195]}

        img = cv2.imread(img_path)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_height, img_width  = img.shape[0], img.shape[1]

        with open(annotation_path) as f:

            targets = [line.rstrip('\n') for line in f]

       

        img_comp_bboxes = img.copy()

        for target in targets:

            target = target.split()

            xc_abs = int(float(target[1])*img_width)

            yc_abs = int(float(target[2])*img_height)

            w_abs = int(float(target[3])*img_width)

            h_abs = int(float(target[4])*img_height)

 

            xmin = int(xc_abs-int(w_abs//2))

            xmax = int(xc_abs+int(w_abs//2))

            ymin = int(yc_abs-int(h_abs//2))

            ymax = int(yc_abs+int(h_abs//2))

            img_comp_bboxes = cv2.rectangle(img_comp_bboxes,

                                                (xmin, ymin),

                                                (xmax,ymax),

                                                colors[int(target[0])],

                                                3)

        return img_comp_bboxes


bbox_img = visual_txt_annotation_check(r"C:\Users\Theo\Documents\GitHub\DeepImageBlending\results\765.png", r"C:\Users\Theo\Documents\GitHub\DeepImageBlending\annotations\765.txt")

 

plt.imshow(bbox_img)