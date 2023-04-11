#! /bin/bash
echo "Please enter the names"
read -a names
i=0

#echo "${names[@]}"
while [ $i -lt ${#names[@]} ]
	do 
		echo "names = ${names[$i]}"
		i=$((i+1))
	done

echo "-----"
for j in "${names[@]}"
do 
	echo $j
done


