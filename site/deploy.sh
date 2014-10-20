#! /bin/sh

echo 'attention: la suppression des fichiers doit se faire manuellement ā la racine de gh-pages mais aussi dans site/:
	git rm -r path/dossier/*
	git rm -r path/site/dossier/*'
cd ..
mv site/categories/* categories/
mv site/output/posts/* posts/
rm -rf site/output
git add .
git commit -m 'update'
git push
