import os
import shutil
files = os.listdir('/Users/arjunrajdev/Downloads/arjun')

for x in files :
    print(x)
    root, ext = os.path.splitext('/Users/arjunrajdev/Downloads/arjun/'+x)
    ex=ext[1:]
    isExist = os.path.exists('/Users/arjunrajdev/Downloads/arjun/'+ex)
    if (ex == '') :
        continue
    elif (isExist == False) :
        os.mkdir('/Users/arjunrajdev/Downloads/arjun/'+ex)
        shutil.move('/Users/arjunrajdev/Downloads/arjun/'+x,'/Users/arjunrajdev/Downloads/arjun/'+ex)
    elif (isExist == True) :
        shutil.move('/Users/arjunrajdev/Downloads/arjun/'+x,'/Users/arjunrajdev/Downloads/arjun/'+ex)