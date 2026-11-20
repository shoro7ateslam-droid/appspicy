import re
Q = chr(34)
label = open("/tmp/label.txt", encoding="utf-8").read().strip()
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
pattern = "android:label=" + Q + "[^" + Q + "]*" + Q
repl = "android:label=" + Q + label + Q
s = re.sub(pattern, repl, s)
open(p, "w", encoding="utf-8").write(s)
