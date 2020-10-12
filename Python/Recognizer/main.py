import cv2
import numpy as np
import pytesseract
from subprocess import Popen, PIPE, STDOUT

file_name = "9C320C8A-6E73-4EAE-B008-E5B16B613AAE.jpeg"


img = cv2.imread(file_name)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray_img, lang="eng")
print(text)

p = Popen(["python3"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

python_proc_stdout = p.communicate(input=b'print("meow")\nprint("meiwwe")')[0]
print(python_proc_stdout.decode())
