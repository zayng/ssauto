@echo off

if exist %date:~0,10%.log (echo "ÒÑ´æÔÚ") else (copy output.log %date:~0,10%.log&del output.log) 
