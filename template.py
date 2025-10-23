import os

# we will create folder
dirs= [
    os.path.join('data', 'row'),
    os.path.join('data', 'processed'),
    'notebooks',
    'saved_models',
    'src',
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)

    # To initialize git repo empty folder must have some file
    with open(os.path.join(dir_, '.gitkeep'), 'w') as f: # just creating file not adding anything
        pass

# files
files = [
    'dvc.yaml',
    'params.yaml',
    os.path.join('src', '__init__.py'),
    '.gitignore',
    'README.md'
]

for file_ in files:
    with open(file_, 'w') as f:
        pass