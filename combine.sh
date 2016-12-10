# need to make a new version so it can read file in another folder
# rather than the current directory

for file in "$@"
do
	echo "$file"
	cat header.txt "$file" > processed/$file
	python ../gc_gene_plot_filename.py processed/$file
done


