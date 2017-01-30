#!/bin/sh

NODE=$1
if [ $NODE = "error" ]; then
	echo "borked" >&2
	exit 1
fi
date > test_$NODE
echo $@ >> test_$NODE
