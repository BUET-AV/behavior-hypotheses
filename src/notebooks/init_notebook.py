import os, sys
currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

projectFolder = 'C:\\Users\\ASUS\\Desktop\\buetav\\behavior-hypotheses-main\\src'
# projectFolder = 'D:\\AV\\Code\\behavior-hypotheses\\src'
# projectFolder = 'F:/behavior-hypothesis/src'
#sys.path.append(str(projectFolder))
#os.chdir(projectFolder)
#print( f"current working dir{os.getcwd()}")

# import os