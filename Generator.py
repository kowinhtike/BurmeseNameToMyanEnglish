import json
class Myanmar:

    alphabet_represent = {}
    one_word = []
    word_format_list = []
    one_name_custom = {}
    two_name_custom = []

    def parse_double_word(self,input_text):
      double_word_list = ["hh","ww","tt"]
      ans = ""
      ans = input_text
      for word in double_word_list:
        if word in input_text:
           ans = ans.replace(word,word[0:1])
      return ans

    def add_alphabet_represent(self,object):
        for key in object:
            self.alphabet_represent[key] = object[key]

    def get_alphabet_represent(self,key):
        return self.alphabet_represent[key]

    def checkPreValue(self,var_map):
        get_key = ""
        find_index = -1
        loop_index = 0

        for i in var_map:
            get_key = i
            break
        for data in self.one_word:
            for key in data:
                if key in get_key:
                    find_index = loop_index
            loop_index += 1

        if(find_index >= 0):
            self.one_word.insert(find_index,var_map)
        else:
            self.one_word.append(var_map)


    def text_replace(self,unicode,e,custom_word = [], custom_list = {}):  
      for m in custom_word:
        if "ဝ" in unicode:
            unicode_character = unicode.replace("ဝ",m)
        else:
            unicode_character = unicode.replace("က",m)
        obj = {}
        obj[unicode_character] = self.parse_double_word((self.alphabet_represent[m]["e"] + e)) #to check double word
        self.checkPreValue(obj)
        #for custom list
        for list in custom_list:
            obj = {}
            obj[list] = custom_list[list]
            self.checkPreValue(obj)

    def save_generate_word(self,file_name):
        #for one name custom 
        for name in self.one_name_custom:
            obj = {}
            obj[name] = self.one_name_custom[name]
            self.checkPreValue(obj)

        #to get the previous list data
        mylist = self.one_word
        #to reset the original array
        self.one_word = []
        #to insert the two name dataset at the beginning of the array
        self.one_word = self.two_name_custom
        #to restart the one name data to behind of two name dataset
        for data in mylist:
          self.checkPreValue(data)
        #and save the data as word_data.json
        with open(file_name, "w",encoding='utf-8') as json_file:
            json.dump(self.one_word, json_file)
    
# call the object and assign data
Language = Myanmar()
#build the alphabet to represent
Language.alphabet_represent = {
        "က":{"u":"\u1000","e":"K"},
    "ခ":{"u":"\u1001","e":"Kh"},
    "ဂ":{"u":"\u1002","e":"J"},
    "င":{"u":"\u1004","e":"N"},
    "စ":{"u":"\u1005","e":"S"},
    "ဆ":{"u":"\u1006","e":"Sw"},
    "ဇ":{"u":"\u1007","e":"Z"},
    "ည":{"u":"\u100A","e":"N"},
    "တ":{"u":"\u1010","e":"T"},
    "ထ":{"u":"\u1011","e":"Ht"},
    "ဒ":{"u":"\u1012","e":"D"},
    "န":{"u":"\u1014","e":"N"},
    "ပ":{"u":"\u1015","e":"P"},
    "ဖ":{"u":"\u1016","e":"Ph"},
    "ဗ":{"u":"\u1017","e":"B"},
    "ဘ":{"u":"\u1018","e":"B"},
    "မ":{"u":"\u1019","e":"M"},
    "ယ":{"u":"\u101a","e":"Y"},
    "ရ":{"u":"\u101b","e":"Y"},
    "လ":{"u":"\u101c","e":"L"},
    "ဝ":{"u":"\u101d","e":"W"},
    "သ":{"u":"\u101e","e":"Th"},
    "ဟ":{"u":"\u101f","e":"H"},
    "အ":{"u":"\u1021","e":"A"},
}
#add the word sign format style , join english shortcut response , and custom value for another difference key
Language.text_replace("က","a",["က","ခ","ဂ","စ","ည","တ","ဇ","ဒ","ပ","ဖ","ဘ","မ","လ","ရ","ဝ","သ","ဟ","အ"])
Language.text_replace("ကူ","u",["ဆ","န","ဇ","မ","လ","သ"])
Language.text_replace("ကူး","oo",["က","ခ","ဂ","ဆ","ဇ","ထ","ဖ","မ"],{"ရူး":"Yuu","မူး":"Hmue"})
Language.text_replace("ကိုး","oe",["က","ခ","ဇ","စ","တ","ဒ","န","ပ","ဖ","ဘ","မ","ရ"])
Language.text_replace("ကို","o",["က","ည","န","ပ","ဘ","မ"],{"ညို":"Nyo"})
Language.text_replace("\u101D\u1031","ay",["က","ခ","စ","ည","တ","န","ပ","ဖ","မ","လ","ရ","ဝ","ဟ","အ"],{"ဝေ":"Wai"})
Language.text_replace("ကေး","ay",["က","ခ","ဂ","ဝ","လ","ဟ","အ"],{"အေး":"Aye"})
Language.text_replace("ကဲ","ae",["ပ","ဖ","ဘ","မ","ရ","ဝ","သ","အ"])
Language.text_replace("ကံ","an",["က","ခ","စ","ဇ","မ"])
Language.text_replace("ကော","aw",["စ","ဇ","န","ဖ"])
Language.text_replace("ကာ","ar",["က","ဆ","ဇ","ည","တ","ဖ","ဘ","ရ","မ","သ","အ"])
Language.text_replace("ဝက်","et",["က","ခ","ဂ","စ","ဇ","ည","ထ","န","ဖ","မ","ရ","လ"])
Language.text_replace("ကီ","i",["စ","ည","တ","ဒ","န","ဖ","လ","ဝ","သ","ရ"],{"ရီ":"Yee"})
Language.text_replace("ကု","u",["စ","ဆ","န","ပ","ယ","လ","သ"],{"ငု":"Ngu"})
Language.text_replace("ကံ","an",["က","ဇ","စ"])
Language.text_replace("ကုံ","one",["က","စ","ပ","တ","ဗ"])
Language.text_replace("ကုံး","one",["ဆ","တ"])
Language.text_replace("ကား","ar",["က","ည","မ","သ","အ"],{"အား":"Arr"})
Language.text_replace("ကန်း","an",["စ","ဆ"],{"ဆန်း":"San"})
Language.text_replace("ကန်","an",["ပ","ဖ","မ","ရ","ဟ"])
Language.text_replace("ကန့်","ant",["ခ","သ"])
Language.text_replace("ဝုန်","one",["ဆ","တ","ဒ","မ","သ"])
Language.text_replace("ကိန်","ein",["စ","ပ","ရ"])
Language.text_replace("ကောင်","ung",["န","ဖ","မ","သ","အ"],{"မောင်":"Maung"})
Language.text_replace("ကော်","aw",["ဇ","န","မ"])
Language.text_replace("ကွေ","we",["င","ဆ","န"],{"ငွေ":"Ngwe","နွေ":"Nhway"})
Language.text_replace("ဝေး","way",["က","ခ","ဝ","အ"])
Language.text_replace("ကွေး","way",["ဒ","န","ဖ","သ"],{"ထွေး":"Htwe"})
Language.text_replace("ကောင်း","aung",["က","စ","ဇ","တ","န","သ","အ"])
Language.text_replace("ဝေါင်း","aung",["ဒ","ပ"])
Language.text_replace("ကွန်း","oon",[ "စ","ယ","သ"])
Language.text_replace("ဝွမ်း","wan",[ "စ","လ"])
Language.text_replace("ကည်","i",["စ","တ","န","သ"])
Language.text_replace("ဝြည်","yay",["က","ပ",])
Language.text_replace("ကြည်","yi",["က","ပ","ဖ"])
Language.text_replace("ဝိုက်","ike",["တ","ထ","ပ","ဗ","ဖ","ဘ","မ","လ","ဝ","သ"])
Language.text_replace("ဝင်","in",["က","ခ","စ","ဇ","တ","ဒ","န","ပ","ရ","သ","ဟ","အ"])
Language.text_replace("ဝင်း","in",["ည","မ","လ","ဝ","သ"])
Language.text_replace("ဝွဲ့","we",["န","ဖ","ဘ","သ"])
Language.text_replace("ဝင့်","int",["ဆ","တ","ရ","ဝ"])
Language.text_replace("ဝျာ","ayar",["က","ခ","ပ","ဂ"])
Language.text_replace("ဝီး","ee",["ဒ","ဗ","မ","သ"])
Language.text_replace("ဝယ်","al",["ခ","ဆ","ပ","မ","ဟ","အ"],{"အယ်":"Eh"})
Language.text_replace("ဝျိူး","yo",["ခ","ပ","မ"])
Language.text_replace("ဝျိူ","yo",["ခ","ပ"])
Language.text_replace("ဝိုင်","aing",["န","ပ"])
Language.text_replace("ဝွန်","win",["လ","ဇ"])
#for one word custom name data
Language.one_name_custom = {"ဦး":"Oo","ထား":"Htar","လှိုင်":"Hlaing","လွန်":"Lwin","လဲ့":"Lae","မြတ်":"Myat","မှုံ":"Mone","မုန်း":"Mone","ထွဋ်":"Htut","လတ်":"Lat","ဒေါ်":"Daw","နွယ်":"Nwe","ပေါ":"Paw","ဝါ":"Wah","ဆွိ":"Sweet","ခိုင်":"Khaing","ရွှေ":"Shwe","နိုင်း":"Naing","ကျော်":"Kyaw","ဟိန်း":"Hein","ခန့်":"Khant","အံ့":"Ant","ဇွဲ":"Zwe","လှ":"Hla","မွှေး":"Mhwe","လှိုင်":"Hlaing","ဖုန်း":"Phone","ခြား":"Char","ပြည့်":"Pyae","ဂျယ်":"Gel","ချယ်":"Chel","ထွန်း":"Tun","လွတ်":"Lwet","သွက်":"Thwoot","ရှင်း":"Shin","စစ်":"Sit","ဖြိုး":"Phyo","အိမ်":"Eain","ဥာဏ်":"Nyan","ဘုန်း":"Bhone","ကြီး":"Gyi","မြ":"Mya","ပြေ":"Pyay","ချစ်":"Chit","ပြုံး":"Pyone","မြင့်":"Myint","ဗိုလ်":"Bo"}
#for two word custom name data
Language.two_name_custom = [{"အိန္ဒြာ":"Eaindra"},{ "ဥမ္မာ":"Ohnmar"},{"သန္တာ":"Thandar"},{"စန္တာ":"Sandar"},{"သီတာ":"Thida"}]
#finally save the output file
Language.save_generate_word("word_data.json")
