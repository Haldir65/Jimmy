# -*- coding:utf-8 -*-
import re

## https://segmentfault.com/a/1190000007594620
def test_emoji():
    try:
        # Wide UCS-4 build
        myre = re.compile(u'['
            u'\U0001F300-\U0001F64F'
            u'\U0001F680-\U0001F6FF'
            u'\u2600-\u2B55]+',
            re.UNICODE)
    except re.error:
        # Narrow UCS-2 build
        myre = re.compile(u'('
            u'\ud83c[\udf00-\udfff]|'
            u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
            u'[\u2600-\u2B55])+',
            re.UNICODE)

    sss = u'I have a dog \U0001f436 . You have a cat \U0001f431 ! I smile \U0001f601 to you!'
    print(sss)
    print(myre.sub('[Emoji]', sss))  # 替换字符串中的Emoji
    print(myre.findall(sss))         # 找出字符串中的Emoji

## 有一些控制型的Emoji, 可以对人体肤色进行改变
## 使用Python代码演示 FITZ-* 和 ZWJ:
def chage_emoji_skin_color():
    # man_list 分别是: 男孩  女孩  男人  女人
    man_list = [u'\U0001F466', u'\U0001F467', u'\U0001F468', u'\U0001F469']
    # skin_color_list 分别是: 空字符串,表示默认  白种人 -->(不断加深肤色)  黑种人
    skin_color_list = ['', u'\U0001F3FB', u'\U0001F3FC', u'\U0001F3FD', u'\U0001F3FE', u'\U0001F3FF', ]
    for man in man_list:
        for color in skin_color_list:
            print (man + color),
        print
        print '-' * 20

    # Emoji的连接符<U+200D>  (英文名为: ZERO WIDTH JOINER, 简写ZWJ )
    # 如果系统支持: 连接(男人 + ZWJ + 女人 + ZWJ + 女孩)
    print u'\U0001F468' + u'\u200D' + u'\U0001F469' + u'\u200D' + u'\U0001F467'
    # 如果系统不支持: 连接(狗 + ZWJ + 猫 + ZWJ + 老鼠)
    print u'\U0001f436' + u'\u200D' + u'\U0001f431' + u'\u200D' + u'\U0001f42d'

def change_emoji_style():
    sample_list = [u'\u2139', u'\u231B', u'\u26A0', u'\u2712', u'\u2764', u'\U0001F004', u'\U0001F21A', u'\U0001f436', ]

    # 输出原样式
    for code in sample_list:
        print code,
    print
    print '-' * 20
    # 后面加上VS-15
    for code in sample_list:
        print (code + u'\uFE0E')
    print '-' * 20
    # 后面加上VS-16
    for code in sample_list:
        print (code + u'\uFE0F')



def main():
    print (len(u'汉字')) ##2 
    print (len('汉字')) ##6 被转成utf-8
    test_emoji()
    chage_emoji_skin_color()



if __name__ == '__main__':
    main()