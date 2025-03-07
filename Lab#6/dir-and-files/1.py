#1. Write a Python program to list only directories, files and all directories, files in a specified path. 
import os
path = "/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)
#RESULTS:
#Output: ['$Recycle.Bin', '$SysReset', '$WINDOWS.~BT', 'Config.Msi', 'Documents and Settings', 'DRIVER', 'DumpStack.log.tmp', 'hiberfil.sys', 'MSOCache', 'msys64', 'OpenBox', 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Recovery', 'swapfile.sys', 'System Volume Information', 'test', 'Users', 'Windows']