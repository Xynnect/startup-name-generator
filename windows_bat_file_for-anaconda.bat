@echo off

D:
cmd /k "cd /d D:\AnacondaPython\Scripts & activate & cd /d & cd D:\startup-name-generator\startup-name-generator & python generate.py -e 500 -n 30 -t 0.7 -s models/gallicc_500epochs.h5 wordlists/gallic.txt > output6.txt & cat output4.txt"

pause