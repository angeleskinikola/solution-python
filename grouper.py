import copy


def group(items, keys):
    tempKeys = copy.copy(keys)
    if len(tempKeys) == 0:
        return items

    key = tempKeys[0]
    tempKeys.pop(0)
    finalMap = {}

    for item in items:
        if check_key_exist(finalMap, item[key]):
            keyToValue = {}
            for k in item:
                if k != key:
                    keyToValue[k] = item[k]
            finalMap[item[key]].append(keyToValue)
        else:
            itemsList = []
            keyToValue = {}
            for k in item:
                if k != key:
                    keyToValue[k] = item[k]
            itemsList.append(keyToValue)
            finalMap[item[key]] = itemsList

    if len(tempKeys) == 0:
        return finalMap
    else:
        for k in finalMap:
            tempKeys2 = copy.copy(tempKeys)
            finalMap[k] = group(finalMap[k], tempKeys2)

    return finalMap


def check_key_exist(dic, key):
    if key in dic:
        return True
    else:
        return False

