espeak -ven+f2 -k5 -s150 --stdout "Waht can I help you?" | aplay
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_zipcode.wav
python3 prototype.py recorded_zipcode.wav
