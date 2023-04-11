#! /bin/bash
n=45
if [ $n -gt 45 ]
then 
	echo "number is greater than 45"
else
	echo "number is less than or equal to 45"
fi

if (( $n >= 35 ))
then
	echo "pass"
else
	echo "fail"
fi

