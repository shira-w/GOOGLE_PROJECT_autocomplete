# GOOGLE PROJECT: autocomplete sentences 21/07/2020
### (~30h challenge)

Search and auto-completion for sentences within given input text files. Manipulating the data
with complex data-structures and algorithmic optimizations using Python and C++.

## Description

With the purpose to improve search engine users experience, 
the development team decided to enable sentences autocomplete from blogs,
documentation and information files in different technology topics.

In a wonderful experience, with the Google’s mentors team, 
this project implemented demo of the Google’s autocomplete: 

In reaction to letters sequence input,
user accept most suitable sentences from large buffers of text files. 
The requirement take place by 2 models: online and offline. 

In the ONLINE model: user enters a word and accept the expected sentence.
implementation in auto_complete_data.py, auto_complete.py & main.py. 
The goal is to keep it in minimal TIME-COMPLEXITY…

In the OFFLINE model: advance preparing; 
scanning of the files and mapping them in comfortable way. 
Also here exist challenges of SPACE and TIME.

Json-files : w.json, y.json ect. are examples to the solution of little json-files each for another letter in A-B. 
in order  to keep memory from crashing which achieves system in case of only one great dictionary in RAM.

What else? The program forgives user- mistakes; 
forgetting or adding a letter, replacing by another one, etc. The sentence will still appear.
To achieve that, has been required use of self-product regular expression.

## Team Members
* Shira Weinstein (Me)
* Shira Dayan
* Rivka Shenberger

## Libraries/Technologies Used
* python 3.7




