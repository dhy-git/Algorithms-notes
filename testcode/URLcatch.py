import re 
  
def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url 
      
 
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))



'''
(?:x) 的使用：
匹配 x 但是不记住匹配项。这种括号叫作非捕获括号，
使得你能够定义与正则表达式运算符一起使用的子表达式。
    看看这个例子 /(?:foo){1,2}/。
    如果表达式是 /foo{1,2}/，{1,2} 将只应用于 'foo' 的最后一个字符 'o'。
    如果使用非捕获括号，则 {1,2} 会应用于整个 'foo' 单词。

'''