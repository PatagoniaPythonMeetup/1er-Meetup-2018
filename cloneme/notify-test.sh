while true
do
    python3 -m unittest
    if [ $? -ne 0 ]; 
    then
        paplay /usr/share/sounds/freedesktop/stereo/bell.oga 2> /dev/null
    else
        paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2> /dev/null
    fi
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
    inotifywait -e modify $(find . -name '*.py')
done
