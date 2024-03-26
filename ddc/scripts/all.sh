for COLL in speirmix
do
	echo "Executing ${1} for ${COLL}"
	${1} ${COLL}
	echo "--------------------------------------------"
done