import streamlit as st
import random

plaintext=[]
ciphertext=[]
key=[]

def xor(a,b):
    if a == b:
        return "0"
    else:
        return "1"

def encrypt(c):
    rvalue=list()
    k=random.randint(33,126)
    rvalue.append(chr(k))
    cbin=format(ord(c),"08b")
    kbin=format(k,"08b")
    cibin=[]
    for i in range(8):
        cibin.append(xor(cbin[i],kbin[i]))
    rvalue.append(str(int("".join(cibin),2)))
    return rvalue

def decode(k,ci):
    kbin=format(ord(k),"08b")
    cibin=format(ci,"08b")
    pbin=[]
    for j in range(8):
        pbin.append(xor(kbin[j],cibin[j]))
    return chr(int("".join(pbin),2))

st.title("Vernam encoder & decoder")

st.subheader("\nI made this after learning about vernam encryption because I thought that it would be interesting as well as to port it to web\n")

st.write("made by Peter\n")

mode=st.selectbox("choose mode",["encrypt", "decrypt"])

if mode == "encrypt":
    text=st.text_input("write what you want to encrypt")
    if st.button("encrypt"):
        for i in text:
            encrypted=encrypt(i)
            key.append(encrypted[0])
            ciphertext.append(encrypted[1])
        st.write("ciphertext:"+" ".join(ciphertext))
        st.write("key:"+"".join(key))
elif mode== "decrypt":
    ciphertext=st.text_input("insert ciphertext")
    key=st.text_input("insert key")
    if st.button("decrypt"):
        try:
            cipher=list(map(int,ciphertext.split()))
            for i in range(len(cipher)):
                plaintext.append(decode(key[i],cipher[i]))
            st.write("plaintext: "+"".join(plaintext))
        except:
            st.write("invalid input. try again")
