s = "Odesssa"
new_s =''
prev_w =''

for w in s:
    if prev_w != w:
        new_s += w
        prev_w = w
        print( "New word:", new_s)