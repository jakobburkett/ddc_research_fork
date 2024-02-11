FILES="scripts/*"
for f in $FILES
do
	tr -d '\r' ${f} > ${f}
done
