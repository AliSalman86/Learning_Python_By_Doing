# This script assumes that the current directory is where we want the new repository to be created locally
# create new repository:
git init

# create a dummy commit to initiate the new repository
git add .
git commit -m 'Initial empty merge repo' -allow-empty

# add remote for and fetch the old repo
git remote add -f LPBD_ErrorsInPython https://github.com/AliSalman86/LPBD_ErrorsInPython.git
git fetch --all
git merge LPBD_ErrorsInPython/main --allow-unrelated-histories

# removing the dummy file, it is not neede anymore
# git rm ./deleteme.txt
# git commit -m 'clean up initial file'

# Moving old repo files and folders into a subdirectory so they don’t collide with the other repo coming later
mkdir LPBD_ErrorsInPython
dir -exclude LPBD_ErrorsInPython | %{git mv $_.Name LPBD_ErrorsInPython}

# Commit the files and folders moving
git commit -m 'Move LPBD_ErrorsInPython files into subdir'

# Same repeated for all remote repositories need to be moved to the new repo as subdir
git remote add -f LPBD_MileStoneProject1 https://github.com/AliSalman86/LPBD_MileStoneProject1.git
git fetch --all
git merge LPBD_MileStoneProject1/main --allow-unrelated-histories
mkdir LPBD_MileStoneProject1
dir -exclude LPBD_ErrorsInPython, LPBD_MileStoneProject1 | %{git mv $_.Name LPBD_MileStoneProject1}
git commit -m 'Move LPBD_MileStoneProject1 files into subdir'

# LPBD_FilesInPython
git remote add -f LPBD_FilesInPython https://github.com/AliSalman86/LPBD_FilesInPython.git
git fetch --all
git merge LPBD_FilesInPython/main --allow-unrelated-histories
mkdir LPBD_FilesInPython
dir -exclude LPBD_ErrorsInPython, LPBD_MileStoneProject1, LPBD_FilesInPython | %{git mv $_.Name LPBD_FilesInPython}
git commit -m 'Move LPBD_FilesInPython files into subdir'