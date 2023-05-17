t = "demo.txt"
try:
    with open(t) as fp:
        fp.read()

except:
    print("except block")
print("thanks for visiting")
