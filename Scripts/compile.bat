pyinstaller --noconsole main.py -F

del build
del __pycache__
del PC_Term.spec
ren dist Compiled
copy readme.txt Compiled\readme.txt