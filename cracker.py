import string
import hashlib
import time

def crack(hash_, type_):
    hashtypes = {"sha1":hashlib.sha1, "md5":hashlib.md5, "sha256":hashlib.sha256, "sha512":hashlib.sha512}
    data = {}
    a = 0
    while len(data) < 99:
        for x in string.letters+string.digits+string.punctuation:
            if len(data) == 100:
                break
            data[a] = x
            a += 1
    #print data
    on_ = 0
    hps = 0
    st = time.time()
    while True:
        on = list(str(on_))
        lenlist = len(on)
        remainder = None
        even = True
        if lenlist % 2 != 0:
            even = False
        if even:
            out = []
            div = []
            while on:
                div.append(on.pop())
                if len(div) == 2:
                    out.append(''.join(div))
                    div = []
        else:
            out = []
            remainder = ''.join(on[lenlist-1:])
            div = []
            while on:
                div.append(on.pop())
                if len(div) == 2:
                    out.append(''.join(div))
                    div = []
        word = ""
        for x in out:
            word += data[int(x)]
        if time.time() -st >= 1:
            print str(hps) + " h/s" + " on: "+ word
            hps = 0
            st = time.time()
        else:
            hps += 1
        check = hashtypes[type_](word).hexdigest()
        if check == hash_:
            print word, hash_
            break
        on_ += 1

if __name__ == "__main__":
    #crack("f9dc77cece7fa16f6edd2d1d64853e4b", "md5")
    #crack("d077f244def8a70e5ea758bd8352fcd8", "md5") 
    crack(raw_input("Hash: "), raw_input("Type: "))
