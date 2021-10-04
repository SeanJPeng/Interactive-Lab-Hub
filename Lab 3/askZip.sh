espeak -ven+f2 -k5 -s150 --stdout "Enter your zip code" | aplay
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_zipcode.wav
python3 test_words.py recorded_zipcode.wav
