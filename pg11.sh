#! /bin/bash
read -p "Enter marks1 " marks1
read -p "Enter marks2 " marks2
read -p "Enter the subject for marks1" sub1
read -p "Enter the subject for marks2" sub2

if [[ "$marks1" -gt "$marks2" && "$sub1" == "$sub2" ]]
then
	echo "marks1 is greater than marks2"
elif [[ "$marks2" -gt "$marks1" && "$sub1" == "$sub2" ]]
then
	echo "marks2 is greater than marks1"
elif [ "$marks2" == "$marks1" ] && [ "$sub1" == "$sub2" ]
then
	echo "marks are equal and subjects are equal"
else 
	echo "subjects are different"
fi

