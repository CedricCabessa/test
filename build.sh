#!/bin/sh

NODE=$1
date > test_$NODE
echo $@ >> test_$NODE
