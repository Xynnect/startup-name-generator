@echo off
SET FileName=output19.txt

cmd /k "cd /d D:\AnacondaPython\Scripts & activate & cd /d & cd D:\startup-name-generator\startup-name-generator & python generate.py -e 100 -n 30 -t 0.5 wordlists/cleaned-countries-data.txt > %FileName% & cat %FileName%"

pause