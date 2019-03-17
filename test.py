import re
import json

def sortlist(hex,colours):
    for i in range(len(hex)-1):
        for j in range(i+1,len(hex)):
            if int(hex[i],16) > int(hex[j],16):
                temp = hex[i]
                hex[i] = hex[j]
                hex[j] = temp
                temp = colours[i]
                colours[i] = colours[j]
                colours[j] = temp
    return hex,colours

def mergelists(hex1,hex2,colours1,colours2):
    merged = {}
    # print(len(hex1))
    for i in range(len(hex1)):
        if colours1[i] in merged and hex1[i] != merged[colours1[i]]:
            # print('%s %s %s'%(colours1[i],hex1[i],merged[colours1[i]]))
            merged[colours1[i][1:-1]+ ' ' + str(i)] = hex1[i]
            continue
        merged[colours1[i][1:-1]] = hex1[i]
    for i in range(len(hex2)):
        if colours2[i] in merged and hex2[i] != merged[colours2[i]]:
            # print('%s %s %s'%(colours2[i],hex2[i],merged[colours2[i]]))
            merged[colours2[i]+ ' ' + str(i)] = hex2[i]
            continue
        merged[colours2[i]] = hex2[i]
    return merged

def main():
    colours = []
    hexcodes = []
    colours1 = []
    hexcodes1 = []
    file1 = open('colours.json',"r")
    x = json.load(file1)
    for c in x["colors"]:
        colours1.append(c['name'])
        hexcodes1.append(c['hex'])
        # print(c['name'])
        # print(c['hex'])
    hexcodes1,colours1 = sortlist(hexcodes1,colours1)
    for i in range(len(hexcodes1)):
        hexcodes1[i] = '#' + str(hexcodes1[i])
        colours1[i] = str(colours1[i])
    with open("wiki_colours.txt","r") as f:
        # i = 0
        for line in f:
            # i+=1
            colours.append(str(re.findall('^[A-Z a-z]+[A-Z a-z]?[-]?[A-Z a-z]?[(]?[A-Z a-z]*[)]?',line))[1:-1])
            hexcodes.append(str(re.findall('#[A-Fa-z0-9]+',line))[3:-2])
        # print(i)
    # for i in range(len(colours)):
    #     print("%s %s"%(hexcodes[i],colours[i]))
    hexcodes,colours = sortlist(hexcodes,colours)
    for i in range(len(hexcodes)):
        hexcodes[i] = '#' + str(hexcodes[i])
    merged = mergelists(hexcodes,hexcodes1,colours,colours1)
    # print(merged)
    # print()
    # print(len(merged))
    # print(len(colours1))
    # print(len(colours))

    counter = 0
    sorted_names = sorted(list(merged))
    for name in sorted_names:
        print("<div class=colorbox"+ "%d"%counter + "></div>" + "<h2>%s: %s"%(name,merged[name]) + "</h2>")
        counter +=1
    # counter = 0
    # for name in sorted_names:
    #     print(".colorbox%d"%counter + "{ height:100px; width:100px; background-color:%s;}"%merged[name])
    #     counter += 1

    # for i in range(len(colours)):
    #     print("%s %s"%(hexcodes[i],colours[i]))
    # print(type(colours[1]))




if __name__ == '__main__':
    main()
