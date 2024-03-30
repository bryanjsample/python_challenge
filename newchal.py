import os
import shutil

dir = os.getcwd()

challenge_num = input('What number? ')

if challenge_num not in os.listdir(dir):
    shutil.copytree(f'{dir}/template', f'{dir}/{challenge_num}')
    shutil.move(f'{dir}/{challenge_num}/challenge00.ipynb', f'{dir}/{challenge_num}/challenge{challenge_num}.ipynb')
else:
    print('Already exists. Check yoself.')
    quit()