from bs4 import BeautifulSoup
import requests
import operator

def get_list(url_site):
    wordlist=[]
    sup=requests.get(url_site).text
    soup= BeautifulSoup(sup,'lxml')
    for link in soup.findAll('a'):
        sentence = link.text
        words = sentence.lower().split()
        for word in words:
            wordlist.append(word)
    for link in soup.findAll('p'):
        sentence = link.text
        words = sentence.lower().split()
        for word in words:
            wordlist.append(word)
    for link in soup.findAll('h'):
        sentence = link.text
        words = sentence.lower().split()
        for word in words:
            wordlist.append(word)
    #print(wordlist)
    clean_up_list(wordlist)
    #for i in range(0,len(wordlist)-1):
        #print(wordlist[i].encode('utf-8'))

def clean_up_list(wordlist):
    clean_word_list=[]
    symbols="`1234567890~!@#$%^&*()_-+=\{\[}]:;,.<>/?\"\'"
    for word in wordlist:
        for i in range(0,len(symbols)):
            word=word.replace(symbols[i],"")
        if(len(word)>0):
            #print(word.encode('utf-8'))
            clean_word_list.append(word.encode('utf-8'))
    get_word_count(clean_word_list)

def get_word_count(word_list_passed):
    word_count={}
    for word in word_list_passed:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word]=1
    file=open("wordcount.txt",'w')
    for key,value in sorted(word_count.items(),key= operator.itemgetter(1)):
        if(ch==1):
            file.write(key +" "+ str(value)+"\n")
        elif ch==2:
            print(key,value)
    file.close()
url=raw_input("whats the url?")
ch = input("do you want to  1.add to  a file or 2.print")
get_list(url)
