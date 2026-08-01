with open ("user.txt", "r")as f:
    fo= f.read()
    role = fo.strip()
    for r in fo:
        print("checking "+ r)
