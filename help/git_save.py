import subprocess
#import os

print('adding to git..')
command =r'git add .'
subprocess.run(command, shell=True, capture_output=False, text=True)

comment=input('Insert a comment to commit:\n')
print('commiting to git..')
command =r'git commit -m '+comment
subprocess.run(command, shell=True, capture_output=False, text=True)

print('pushing to git..')
command =r'git push -u origin master'
subprocess.run(command, shell=True, capture_output=False, text=True)
