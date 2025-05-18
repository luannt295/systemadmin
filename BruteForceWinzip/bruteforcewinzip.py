import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print(f'Wrong password: {password}')
    return None

def main():
    zfile = zipfile.ZipFile('test.zip')
    with open('passlist.txt') as passFile:
        for line in passFile:
            password = line.strip()
            guess = extractFile(zfile, password)
            if guess:
                print('✅ Password found: ' + password)
                break

if __name__ == '__main__':
    main()
