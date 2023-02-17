import os
print(os)
print('Current working directory(CWD):',os.getcwd())

#os.chdir(path='')#FileNotFoundError

os.chdir('..')#or os.chdir('../')
print('Current working directory(CWD):',os.getcwd())
os.chdir('./')#or os.chdir('.')
print('Current working directory(CWD):',os.getcwd())
os.chdir('/home/adede/os')
print('We are in:',os.getcwd())

#os.mkdir(path='')#FileNotFoundError
#os.mkdir('.') #FileExistsError
#osmkdir('../')#FileExistsError
#osmkdir('./')#FileExistsError
#os.mkdir('...')#there is no Error
#os.mkdir('my_dir')
#os.chdir('1')##FileNotFoundError

print('Current working directory(CWD):',os.getcwd())
#os.chdir('~/')
#raised a "FileNotFoundError" because the tilde ""
# character is not recognized as a valid path by the
# "os.chdir()" method.

# Change to home directory
home_dir = os.path.expanduser("~")
os.chdir(home_dir)
print("Current working directory(CWD):", os.getcwd())
dir=os.path.expanduser('~')# or '' or any string else
print("Current working directory(CWD):", os.getcwd())

new_dir='new_dir'
# Path
path = os.path.join(dir, new_dir)


#os.mkdir(path)
print("Directory '% s' created" % new_dir)
pth=os.path.join(dir,new_dir,'d1/d2/d3/d4')
#os.makedirs(pth)
os.chdir(pth)
print("Current working directory(CWD):", os.getcwd())
os.chdir('../../../../')
print("Current working directory(CWD):", os.getcwd())
ls=os.listdir()
print('ls:',ls)

os.chdir('../')
print("Current working directory(CWD):", os.getcwd())
ls=os.listdir()
print('ls:',ls)
print(type(ls))

ls=os.listdir('../')
print('ls:',ls)
print(os.name)
path=os.path.join(os.path.expanduser('~'),'os/','to_be_removed.txt')
print('path:',path)
#os.remove(path)

path=os.path.join(os.path.expanduser('~'),'os/','direct')
#os.mkdir(path)
#os.rmdir(path)
path=os.path.join(os.path.expanduser('~'),'os/','my_dir')
print(path)
#os.rename(src=path,dst='new_name/')
print(os.path.exists(path))
