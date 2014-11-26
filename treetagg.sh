FILES=$1

for f in $FILES
do
	eval "cat $f | cmd/tree-tagger-english > newTagged/$f"
done
