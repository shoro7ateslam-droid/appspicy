import re
label = open( /tmp/label.txt , encoding= utf-8 ).read().strip()
p =  android/app/src/main/AndroidManifest.xml 
s = open(p, encoding= utf-8 ).read()
s = re.sub(r android:label="[^"]*" , f android:label="{label}" , s)
open(p,  w , encoding= utf-8 ).write(s)
