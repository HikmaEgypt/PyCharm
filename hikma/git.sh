echo  $2 >> README.md
git init
git remote add origin git@github.com:$1/$2
git add $3
git commit -m "$4"
git push -u origin master
