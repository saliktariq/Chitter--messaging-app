#! /bin/bash
echo "1: add 2: subtract 3: multiple 4: divide"
read -p "Enter choice = " ch
read -p "Enter value of a = " a
read -p "Enter value of b = " b
if (( $ch == 1 ))
then 
	sum=$((a+b))
	echo "Sum = $sum"
elif (( $ch == 2 ))
then
	diff=$((a-b))
	echo "Difference = $diff"
elif (( $ch == 3 ))
then
	product=$((a*b))
	echo "Product = $product"
else
	division=$((a/b))
	echo "Division = $division"
fi

