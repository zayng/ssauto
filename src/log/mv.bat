@echo off

if exist %date:~0,10%.log (echo "�Ѵ���") else (copy output.log %date:~0,10%.log&del output.log) 
