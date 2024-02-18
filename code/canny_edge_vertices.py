import numpy as np
import matplotlib.pyplot as plt
import cv2

img_path = '../0_room_imgs/room_0.png'
out_path = '../shapes/raw/'

img2 = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 
edge = cv2.Canny(img, 100, 200)

height, width = img.shape

ans = []
for y in range(0, edge.shape[0]):
    for x in range(0, edge.shape[1]):
        if edge[y, x] != 0:
            ans = ans + [[x, y]]
ans = np.array(ans)

print(ans.shape)
print(ans[0:10, :])

f = open(f'{out_path}/0_room_0_check.txt', 'w')
for point in ans:
    # Normalize (x,y) to (0,1)
    x = (np.double(point[0]) / width) 
    y = (np.double(point[1]) / height) 
    f.write(f'{x} {y}\n')
f.close()