import subprocess
import os
# c++ 
# c
# python ke extension mai convert karna hai fir usko respective .
# extension ke respect mai compile karna hai and then 
# jo output aayega wo ile mai save karke read karna hai


def CodeCompiler(filepath, language):
    if language =='c':
       compiler = 'gcc'
    elif language =='c++':
        compiler = 'g++'
    else: 
         return   
    #python ko compile nahi interprete karna hota hai   
#     try:
# #      path, code, ??? kya karu iska
#        curr_dir = os.getcwd()
#        os.chdir("")
#        subprocess.run([compiler,filepath], capture_output=True)
#        os.chdir(curr_dir)
#     except:
#       return "Code cant be Compiled!"
#     #  except:


def CodeRunner(language, inputdata):
    # try:
    #     curr_dir = os.getcwd() 
    #     os.chdir() 

    #     if language == 'py':
    #         result = subprocess.run(['python'])
    #     else:
    #         result = subprocess.run(['./a.out'])
    #     os.chdir(curr_dir)


    #  except FileNotFoundError:
    #    print("file not found.")
    pass