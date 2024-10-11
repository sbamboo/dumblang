def ansi_code_to_rgb(ansi_code_str, eightbit_to_rgb, eightbit_to_ansi_fg):
    for k,v in eightbit_to_ansi_fg.items():
        if v == ansi_code_str or str(v) == ansi_code_str:
            return eightbit_to_rgb[k]

eightbit_to_rgb = {"0": "0,0,0", "1": "128,0,0", "2": "0,128,0", "3": "128,128,0", "4": "0,0,128", "5": "128,0,128", "6": "0,128,128", "7": "192,192,192", "8": "128,128,128", "9": "255,0,0", "10": "0,255,0", "11": "255,255,0", "12": "0,0,255", "13": "255,0,255", "14": "0,255,255", "15": "255,255,255", "16": "0,0,0", "17": "0,0,51", "18": "0,0,102", "19": "0,0,153", "20": "0,0,204", "21": "0,0,255", "22": "0,51,0", "23": "0,51,51", "24": "0,51,102", "25": "0,51,153", "26": "0,51,204", "27": "0,51,255", "28": "0,102,0", "29": "0,102,51", "30": "0,102,102", "31": "0,102,153", "32": "0,102,204", "33": "0,102,255", "34": "0,153,0", "35": "0,153,51", "36": "0,153,102", "37": "0,153,153", "38": "0,153,204", "39": "0,153,255", "40": "0,204,0", "41": "0,204,51", "42": "0,204,102", "43": "0,204,153", "44": "0,204,204", "45": "0,204,255", "46": "0,255,0", "47": "0,255,51", "48": "0,255,102", "49": "0,255,153", "50": "0,255,204", "51": "0,255,255", "52": "51,0,0", "53": "51,0,51", "54": "51,0,102", "55": "51,0,153", "56": "51,0,204", "57": "51,0,255", "58": "51,51,0", "59": "51,51,51", "60": "51,51,102", "61": "51,51,153", "62": "51,51,204", "63": "51,51,255", "64": "51,102,0", "65": "51,102,51", "66": "51,102,102", "67": "51,102,153", "68": "51,102,204", "69": "51,102,255", "70": "51,153,0", "71": "51,153,51", "72": "51,153,102", "73": "51,153,153", "74": "51,153,204", "75": "51,153,255", "76": "51,204,0", "77": "51,204,51", "78": "51,204,102", "79": "51,204,153", "80": "51,204,204", "81": "51,204,255", "82": "51,255,0", "83": "51,255,51", "84": "51,255,102", "85": "51,255,153", "86": "51,255,204", "87": "51,255,255", "88": "102,0,0", "89": "102,0,51", "90": "102,0,102", "91": "102,0,153", "92": "102,0,204", "93": "102,0,255", "94": "102,51,0", "95": "102,51,51", "96": "102,51,102", "97": "102,51,153", "98": "102,51,204", "99": "102,51,255", "100": "102,102,0", "101": "102,102,51", "102": "102,102,102", "103": "102,102,153", "104": "102,102,204", "105": "102,102,255", "106": "102,153,0", "107": "102,153,51", "108": "102,153,102", "109": "102,153,153", "110": "102,153,204", "111": "102,153,255", "112": "102,204,0", "113": "102,204,51", "114": "102,204,102", "115": "102,204,153", "116": "102,204,204", "117": "102,204,255", "118": "102,255,0", "119": "102,255,51", "120": "102,255,102", "121": "102,255,153", "122": "102,255,204", "123": "102,255,255", "124": "153,0,0", "125": "153,0,51", "126": "153,0,102", "127": "153,0,153", "128": "153,0,204", "129": "153,0,255", "130": "153,51,0", "131": "153,51,51", "132": "153,51,102", "133": "153,51,153", "134": "153,51,204", "135": "153,51,255", "136": "153,102,0", "137": "153,102,51", "138": "153,102,102", "139": "153,102,153", "140": "153,102,204", "141": "153,102,255", "142": "153,153,0", "143": "153,153,51", "144": "153,153,102", "145": "153,153,153", "146": "153,153,204", "147": "153,153,255", "148": "153,204,0", "149": "153,204,51", "150": "153,204,102", "151": "153,204,153", "152": "153,204,204", "153": "153,204,255", "154": "153,255,0", "155": "153,255,51", "156": "153,255,102", "157": "153,255,153", "158": "153,255,204", "159": "153,255,255", "160": "204,0,0", "161": "204,0,51", "162": "204,0,102", "163": "204,0,153", "164": "204,0,204", "165": "204,0,255", "166": "204,51,0", "167": "204,51,51", "168": "204,51,102", "169": "204,51,153", "170": "204,51,204", "171": "204,51,255", "172": "204,102,0", "173": "204,102,51", "174": "204,102,102", "175": "204,102,153", "176": "204,102,204", "177": "204,102,255", "178": "204,153,0", "179": "204,153,51", "180": "204,153,102", "181": "204,153,153", "182": "204,153,204", "183": "204,153,255", "184": "204,204,0", "185": "204,204,51", "186": "204,204,102", "187": "204,204,153", "188": "204,204,204", "189": "204,204,255", "190": "204,255,0", "191": "204,255,51", "192": "204,255,102", "193": "204,255,153", "194": "204,255,204", "195": "204,255,255", "196": "255,0,0", "197": "255,0,51", "198": "255,0,102", "199": "255,0,153", "200": "255,0,204", "201": "255,0,255", "202": "255,51,0", "203": "255,51,51", "204": "255,51,102", "205": "255,51,153", "206": "255,51,204", "207": "255,51,255", "208": "255,102,0", "209": "255,102,51", "210": "255,102,102", "211": "255,102,153", "212": "255,102,204", "213": "255,102,255", "214": "255,153,0", "215": "255,153,51", "216": "255,153,102", "217": "255,153,153", "218": "255,153,204", "219": "255,153,255", "220": "255,204,0", "221": "255,204,51", "222": "255,204,102", "223": "255,204,153", "224": "255,204,204", "225": "255,204,255", "226": "255,255,0", "227": "255,255,51", "228": "255,255,102", "229": "255,255,153", "230": "255,255,204", "231": "255,255,255", "232": "8,8,8", "233": "18,18,18", "234": "28,28,28", "235": "38,38,38", "236": "48,48,48", "237": "58,58,58", "238": "68,68,68", "239": "78,78,78", "240": "88,88,88", "241": "98,98,98", "242": "108,108,108", "243": "118,118,118", "244": "128,128,128", "245": "138,138,138", "246": "148,148,148", "247": "158,158,158", "248": "168,168,168", "249": "178,178,178", "250": "188,188,188", "251": "198,198,198", "252": "208,208,208", "253": "218,218,218", "254": "228,228,228", "255": "238,238,238"}
eightbit_to_ansi_fg = {"0": 30, "1": 31, "2": 32, "3": 33, "4": 34, "5": 35, "6": 36, "7": 37, "8": 90, "9": 91, "10": 92, "11": 93, "12": 94, "13": 95, "14": 96, "15": 97, "16": 30, "17": 34, "18": 34, "19": 34, "20": 94, "21": 94, "22": 32, "23": 34, "24": 34, "25": 34, "26": 94, "27": 94, "28": 32, "29": 32, "30": 36, "31": 36, "32": 94, "33": 34, "34": 32, "35": 32, "36": 92, "37": 36, "38": 36, "39": 96, "40": 92, "41": 92, "42": 92, "43": 96, "44": 96, "45": 96, "46": 92, "47": 92, "48": 92, "49": 96, "50": 96, "51": 96, "52": 31, "53": 31, "54": 35, "55": 34, "56": 94, "57": 94, "58": 33, "59": 90, "60": 90, "61": 34, "62": 94, "63": 94, "64": 32, "65": 32, "66": 36, "67": 36, "68": 36, "69": 94, "70": 32, "71": 32, "72": 92, "73": 96, "74": 36, "75": 36, "76": 92, "77": 92, "78": 92, "79": 36, "80": 96, "81": 96, "82": 92, "83": 92, "84": 92, "85": 92, "86": 96, "87": 96, "88": 31, "89": 31, "90": 35, "91": 35, "92": 34, "93": 94, "94": 33, "95": 33, "96": 95, "97": 35, "98": 35, "99": 94, "100": 33, "101": 33, "102": 93, "103": 96, "104": 96, "105": 96, "106": 92, "107": 92, "108": 92, "109": 37, "110": 96, "111": 96, "112": 92, "113": 92, "114": 92, "115": 92, "116": 96, "117": 96, "118": 92, "119": 92, "120": 96, "121": 93, "122": 96, "123": 96, "124": 31, "125": 31, "126": 31, "127": 35, "128": 35, "129": 34, "130": 31, "131": 31, "132": 31, "133": 35, "134": 35, "135": 34, "136": 33, "137": 33, "138": 93, "139": 96, "140": 96, "141": 94, "142": 33, "143": 33, "144": 93, "145": 37, "146": 90, "147": 36, "148": 32, "149": 92, "150": 92, "151": 92, "152": 37, "153": 96, "154": 92, "155": 92, "156": 92, "157": 92, "158": 37, "159": 96, "160": 91, "161": 91, "162": 91, "163": 35, "164": 95, "165": 95, "166": 91, "167": 91, "168": 91, "169": 35, "170": 95, "171": 95, "172": 33, "173": 33, "174": 93, "175": 95, "176": 95, "177": 35, "178": 33, "179": 33, "180": 33, "181": 93, "182": 37, "183": 95, "184": 93, "185": 93, "186": 93, "187": 37, "188": 37, "189": 37, "190": 93, "191": 93, "192": 93, "193": 37, "194": 37, "195": 97, "196": 91, "197": 91, "198": 91, "199": 95, "200": 95, "201": 95, "202": 91, "203": 91, "204": 91, "205": 95, "206": 95, "207": 95, "208": 91, "209": 91, "210": 91, "211": 91, "212": 95, "213": 95, "214": 93, "215": 93, "216": 93, "217": 93, "218": 95, "219": 95, "220": 93, "221": 93, "222": 93, "223": 93, "224": 93, "225": 95, "226": 93, "227": 93, "228": 93, "229": 93, "230": 97, "231": 97, "232": 30, "233": 30, "234": 30, "235": 30, "236": 30, "237": 30, "238": 90, "239": 90, "240": 90, "241": 90, "242": 90, "243": 90, "244": 90, "245": 90, "246": 90, "247": 90, "248": 37, "249": 37, "250": 37, "251": 37, "252": 37, "253": 37, "254": 97, "255": 97}
import sys
r = ansi_code_to_rgb(sys.argv[1],eightbit_to_rgb,eightbit_to_ansi_fg)
print(r)