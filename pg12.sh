#! /bin/bash
num1=50
num2=25
echo $(( num1 + num2))
echo $(( num1 - num2))
echo $(( num1 * num2))
echo $(( num1 / num2))
echo $(( num1 % num2))

echo $(expr $num1 + $num2)
echo $(expr $num1 - $num2)
echo $(expr $num1 \* $num2)
echo $(expr $num1 / $num2)
echo $(expr $num1 % $num2)

num3=`expr $num1 \* $num2`
echo $num3

