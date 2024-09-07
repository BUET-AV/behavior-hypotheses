import os, sys
currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

projectFolder = "/home/torr20/Documents/project-autonomous vehicle/behavior-hypotheses/src"
# projectFolder = 'D:\\AV\\Code\\behavior-hypotheses\\src'
# projectFolder = 'F:/behavior-hypothesis/src'
sys.path.append(str(projectFolder))
os.chdir(projectFolder)
print( f"current working dir{os.getcwd()}")
