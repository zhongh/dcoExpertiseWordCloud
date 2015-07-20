import datetime
import string


def Main():
    print("Hello World!")
    f = open('stats.csv', 'r')
    fout = open('statsArray.js', 'w')

    f.readline()
    fout.write("var leaders = [\n")

    line = f.readline()
    line = line.rstrip('\n')
    lineList = line.split(',')
    tmp = '{text:"' + lineList[0] + '", size:' + lineList[2] + ', link:"' + lineList[1] + '"}'
    fout.write(tmp)

    while True:

        line = f.readline()
        line = line.rstrip('\n')
        if line == '':
            fout.write('];')
            break
        else:
            fout.write(',\n')
            lineList = line.split(',')
            tmp = '{text:"' + lineList[0] + '", size:' + lineList[2] + ', link:"' + lineList[1] + '"}'
            fout.write(tmp)
            pass
        pass




if __name__ == '__main__':
    Main()
#EOF












