import time
from PIL import Image
from des import*

def encrypt_sep_RGB(d):
    en_data = []

    # encrypt start time
    tStart = time.time()
    # encrypt data with separate R.G.B
    tempR = d.encrypt(R)
    tempG = d.encrypt(G)
    tempB = d.encrypt(B)
    # encrypt end time
    tEnd = time.time()
    print "%s_sep_encrypt: %f sec" % (d.mode, (tEnd - tStart))

    # binary to 0~255
    for i in range(n*m):
        en_data.append(int(tempR[:8], 2))
        tempR = tempR[8:]
        en_data.append(int(tempG[:8], 2))
        tempG = tempG[8:]
        en_data.append(int(tempB[:8], 2))
        tempB = tempB[8:]

    en_data = np.array(en_data).reshape(n, m, 3)
    outputImg = Image.new("RGB", (n, m))
    outputImg = Image.fromarray(np.uint8(en_data))
    outputImg.save(d.mode + "_sep_encrypt.bmp")

def decrypt_sep_RGB(d):
    im = Image.open(d.mode + "_sep_encrypt.bmp")
    width, height = im.size

    # read raw data
    en_data = np.asarray(im)
    # spilt data to R.G.B
    tempR = tempG = tempB = ''
    for i in range(width):
        for j in range(height):
            tempR += '{:08b}'.format(en_data[i][j][0])
            tempG += '{:08b}'.format(en_data[i][j][1])
            tempB += '{:08b}'.format(en_data[i][j][2])

    # decrypt start time
    tStart = time.time()
    # decrypt data with separate R.G.B
    tempR = d.decrypt(tempR)
    tempG = d.decrypt(tempG)
    tempB = d.decrypt(tempB)
    # decrypt end time
    tEnd = time.time()
    print "%s_sep_decrypt: %f sec" % (d.mode, (tEnd - tStart))

    de_data = []
    # binary to 0~255
    for i in range(width*height):
        de_data.append(int(tempR[:8], 2))
        tempR = tempR[8:]
        de_data.append(int(tempG[:8], 2))
        tempG = tempG[8:]
        de_data.append(int(tempB[:8], 2))
        tempB = tempB[8:]

    de_data = np.array(de_data).reshape(width, height, 3)
    outputImg = Image.new("RGB", (width, height))
    outputImg = Image.fromarray(np.uint8(de_data))
    outputImg.save(d.mode+ "_sep_decrypt.bmp")

def encrypt_con_RGB(d):
    # continuous R.G.B
    con_data = data.reshape(-1)
    temp = ''
    for i in range(n*m*3):
        temp += '{:08b}'.format(con_data[i])
    
    # decrypt start time
    tStart = time.time()
    temp = d.encrypt(temp)
    # decrypt end time
    tEnd = time.time()
    print "%s_con_encrypt: %f sec" % (d.mode, (tEnd - tStart))

    en_data = []
    for i in range(n*m*3):
        en_data.append(int(temp[:8], 2))
        temp = temp[8:]

    en_data = np.array(en_data).reshape(n, m, 3)
    outputImg = Image.new("RGB", (n, m))
    outputImg = Image.fromarray(np.uint8(en_data))
    outputImg.save(d.mode + "_con_encrypt.bmp")

def decrypt_con_RGB(d):
    im = Image.open(d.mode + "_con_encrypt.bmp")
    width, height = im.size
    # continuous R.G.B
    con_data = np.asarray(im)
    con_data = con_data.reshape(-1)
    temp = ''
    for i in range(width*height*3):
        temp += '{:08b}'.format(con_data[i])
    
    # decrypt start time
    tStart = time.time()
    temp = d.decrypt(temp)
    # decrypt end time
    tEnd = time.time()
    print "%s_con_decrypt: %f sec" % (d.mode, (tEnd - tStart))

    en_data = []
    for i in range(width*height*3):
        en_data.append(int(temp[:8], 2))
        temp = temp[8:]

    en_data = np.array(en_data).reshape(width, height, 3)
    outputImg = Image.new("RGB", (width, height))
    outputImg = Image.fromarray(np.uint8(en_data))
    outputImg.save(d.mode + "_con_decrypt.bmp")

if __name__ == '__main__':
    # open bmp file
    img = Image.open("test.bmp")
    n, m = img.size

    # read raw data
    data = np.asarray(img)
    # spilt data to R.G.B
    R = G = B = ''
    for i in range(n):
        for j in range(m):
            R += '{:08b}'.format(data[i][j][0])
            G += '{:08b}'.format(data[i][j][1])
            B += '{:08b}'.format(data[i][j][2])

    key = "10101011"*8
    IV = "11111011"*8

    d = []
    d.append(des(key, "ECB", None))
    d.append(des(key, "CBC", IV))
    d.append(des(key, "OFB", IV))
    d.append(des(key, "CTR", IV))

    for i in d:
        # encrypt bmp with separate R.G.B
        encrypt_sep_RGB(i)
        # decrypt bmp wit separate R.G.B
        decrypt_sep_RGB(i)
        # encrypt bmp with continuous R.G.B
        encrypt_con_RGB(i)
        # decrypt bmp with continuous R.G.B
        decrypt_con_RGB(i)