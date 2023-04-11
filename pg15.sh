#! /bin/bash
var1="strawberry"
case $var1 in 
	"apple" )
		echo "pay 50";;
	"grapes" )
		echo "pay 60";;
	"mango" )
		echo "pay 80";;
	* )
		echo "fruit not listed";;
esac

