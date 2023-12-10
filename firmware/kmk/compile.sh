#!/bin/bash

MPY_CROSS=$(which mpy-cross 2>/dev/null)
MPY_FLAGS='-O2'

compile () {
    mkdir -p $2
    out_file="$2/$(basename -- "$1" .py).mpy"
    echo Compiling $1 to $out_file
    "$MPY_CROSS" $MPY_FLAGS "$1" -o "$out_file"
}

cd $(dirname $0)

compile Adafruit_CircuitPython_NeoPixel/neopixel.py out/lib

find kmk_firmware/kmk -name "*.py" -print0 | while read -d $'\0' file
do
    in_dir=$(dirname $file)
    out_dir="${in_dir/kmk_firmware/out}"
    compile $file $out_dir
done

cp boot.py out
compile kb.py out
cp code.py out
