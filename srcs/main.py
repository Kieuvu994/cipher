import rail_fence

if __name__ == '__main__':
    med = input(' Please choose cipher or decipher (c/d) : ')
    if med == 'c':
        pl = input('Enter method 1.cesar 2.rail-fencer 3.cesar X rail-fence : ')
        if pl == '1':
            pt = input('Enter plaintext (cesar) : ')
            # key = int(input('Enter key (cesar) : '))
            # print('------------------->>>>>> CipherText (cesar) :', rail_fence.cesar(pt, 15))
        elif pl == '2':
            pt = input('Enter plaintext (rail-fence) : ')
            print('------------------->>>>>> CipherText (rail-fence) :',
                rail_fence.rail_fence(pt, 4))
    
