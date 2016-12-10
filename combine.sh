for file in "$@"
do
	echo "$file"
	cat header.txt "$file" > processed/$file
	python ../gc_gene_plot_filename.py processed/$file
done


