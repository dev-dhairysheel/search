import streamlit as st #line:1
import time #line:2
import os #line:3
st .set_page_config (page_title ='CleverMate',page_icon ='🔍')#line:6
st .title ("CleverMate")#line:5
huggingfacehub_api_token =st .secrets ["hf_token"]#line:8
google_api =st .secrets ["google_api"]#line:9
from langchain import HuggingFaceHub ,PromptTemplate ,LLMChain #line:11
repo_id ="tiiuae/falcon-7b-instruct"#line:13
llm =HuggingFaceHub (huggingfacehub_api_token =huggingfacehub_api_token ,repo_id =repo_id ,model_kwargs ={"temperature":0.2 ,"max_new_tokens":2000 })#line:15
template ="""
You are an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
{question}
"""#line:20
prompt =PromptTemplate (template =template ,input_variables =["question"])#line:22
llm_chain =LLMChain (prompt =prompt ,verbose =True ,llm =llm )#line:24
def has_num (OOOO00O00000OOO0O ):#line:26
    return any (OOOO00O00000OOO0O .isnumeric ()for OOO0000OO000O0OOO in OOOO00O00000OOO0O )#line:27
def chat (OOO00O000OOO0000O ):#line:29
    if 'dhairysheel'in OOO00O000OOO0000O  or 'Dhairysheel' in OOO00O000OOO0000O:#line:30
        return """
Dhairysheel Durgule is a young data science enthusiast from India, making waves in the tech world as a 9th-grade IGCSE student. He's on a mission to redefine what's possible in the field, driven by a belief that age is just a number when it comes to passion and innovation.

Here's a deeper dive into what makes Dhairysheel tick:

Data with a storytelling twist: Dhairysheel goes beyond just crunching numbers. He sees data as a powerful tool to weave narratives, uncover hidden insights, and make a positive impact.

Mastery in the making: He's actively honing his skills in data analysis, statistics, and machine learning, devouring knowledge like a coding prodigy. His dedication proves that age is no barrier to expertise.

Curiosity that never quits: Dhairysheel embodies the spirit of a lifelong learner, his enthusiasm radiating like a supernova. He thrives in the ever-evolving world of data, embracing its challenges with an infectious curiosity.

Breaking barriers, building bridges: Dhairysheel is a firm believer in collaboration. He actively seeks connections with other data enthusiasts and forward-thinking professionals, aiming to break stereotypes and rewrite the data science narrative.

A glimpse into the future: Dhairysheel represents the next generation of data-driven changemakers. He's not just looking ahead; he's actively shaping the future with his unwavering passion and commitment.

Remember, Dhairysheel's story is still being written. But one thing's for sure: this young data maverick is definitely one to watch!

I hope this expanded answer gives you a better sense of who Dhairysheel Durgule is and what he's all about. While there might not be tons of information available online yet, his journey is just beginning, and it's sure to be an exciting one!"""#line:48
    if any (OOOOOO0O0OOO00OOO in OOO00O000OOO0000O for OOOOOO0O0OOO00OOO in ['+','-','/','*'])and has_num (OOO00O000OOO0000O ):#line:49
        return "Apologies, but I am not currently equipped to perform mathematical expressions. My primary function is to provide assistance and information in various areas. If there's anything else you need help with or any other topic you'd like to discuss, please let me know, and I'll be glad to assist you."#line:50
    O0OO0OOO00000OOO0 =llm_chain .predict (question =OOO00O000OOO0000O )#line:52
    if any (OO00O00O0000O0000 in O0OO0OOO00000OOO0 for OO00O00O0000O0000 in ['actor','actress','fictional character','Bharatiya Janata Party','Indian National Congress','Indian entrepreneur']):#line:54
        return "I apologize for the inconvenience. At the moment, I don't have sufficient information to provide a precise answer to your question. Could you kindly provide additional context or details regarding your inquiry? This will enable me to offer more accurate and tailored assistance."#line:55
    return O0OO0OOO00000OOO0 #line:57
def main ():#line:59
    OO00000000OOO0000 =st .text_input ("What do you want to ask about",placeholder ="Input your question here")#line:60
    O00OO000OOOOOO0OO =OO00000000OOO0000 .lower ()#line:61
    with st .sidebar :#line:63
        O00O0O00O00OOOO00 =st .sidebar .radio ('Please select mode for the Search',('Brief','Normal','Descriptive'),index =1 )#line:64
        if O00O0O00O00OOOO00 =='Brief':#line:65
            O00OO000OOOOOO0OO =OO00000000OOO0000 +", give short answer"#line:66
        elif O00O0O00O00OOOO00 =='Descriptive':#line:67
            O00OO000OOOOOO0OO =OO00000000OOO0000 +'. Please explain it in detail, be descriptive'#line:68
        else :#line:69
            O00OO000OOOOOO0OO =OO00000000OOO0000 #line:70
        OO00OOOO0O0O0OO0O =st .checkbox ('Include example')#line:72
        if OO00OOOO0O0O0OO0O :#line:73
            O00OO000OOOOOO0OO =O00OO000OOOOOO0OO +'. Give me example'#line:74
    if OO00000000OOO0000 :#line:76
        O00OOO0OOO0OOOOO0 =chat (O00OO000OOOOOO0OO )#line:77
        O0O0OOOO00O0OOOO0 =O00OOO0OOO0OOOOO0 #line:78
        O0O0OOOO00O0OOOO0 =O0O0OOOO00O0OOOO0 .replace ('<p>','').replace ('</p>','')#line:79
        OO0OOO00OOOOO00O0 =''#line:80
        OO00O0O00OO000O0O =st .empty ()#line:81
        for OO0OOO0OO0OOOO0O0 in O0O0OOOO00O0OOOO0 :#line:82
            OO0OOO00OOOOO00O0 =OO0OOO00OOOOO00O0 +OO0OOO0OO0OOOO0O0 #line:83
            time .sleep (0.01 )#line:84
            OO00O0O00OO000O0O .write (OO0OOO00OOOOO00O0 )#line:85
if __name__ =='__main__':#line:87
    main ()
