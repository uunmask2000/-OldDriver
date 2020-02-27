#!/usr/bin/env bash
chcp 65001
TITLE JKF_H
FOR /F %%a IN ('TIME /T') DO set a=%%a 
cd D:\JIM\GIT\gitHub\OldDriver 
python JKF_H.py
fast.bat
pause