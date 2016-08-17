#!/bin/bash

NEW_NAME=$1

function is_include() {
    local line=$1
	local word=$2
	local replaced=$(echo $line | sed "s#$word##")
	test "$line" != "$replaced"
	return $?
}

function is_gitdir() {
    local path=$(readlink -f $1)
	is_include $path "\\.git"
	return $?
}

function is_toolsdir() {
    test $1 != $(echo $1 | sed "s#\\./tools/##")
	return $?
}

find . | while read line
do
    if [ -z "$line" ]; then
        continue
    fi
    if is_gitdir $line
    then
        continue
    fi

	if is_toolsdir $line
	then
		continue
	fi

	if [ -f $line ]
	then
		sed -i "s/skeleton/$NEW_NAME/g" $line
	fi

	if is_include $line skeleton
	then
		mv $line $(echo $line | sed "s/skeleton/${NEW_NAME}/g")
	fi
done

