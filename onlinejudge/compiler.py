import subprocess
import os
from django import forms
from codemirror import CodeMirrorTextarea
# c++ 
# c
# python ke extension mai convert karna hai fir usko respective .
# extension ke respect mai compile karna hai and then 
# jo output aayega wo ile mai save karke read karna hai

def CodeCompiler(file_path,language):
    if language == 'c':
        compiler = 'gcc'
    elif language == 'cpp':
        compiler = 'g++'
    elif language == 'python':
        return 1
    else :
         return 0
    
    curr_dir = os.getcwd()
    try:
        
        os.chdir("question/trash")
        compiledFile = subprocess.run([compiler, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir(curr_dir)
        stderror = compiledFile.stderr.decode("utf-8")
        if stderror =="":
            return 1
        else:
            return 0
    except:
        os.chdir(curr_dir)
        return 0







###############################################
def codeExecute(language,ip_data):
    curr_dir = os.getcwd()
    try:
        os.chdir("question/trash")
        if language == 'py':
            result = subprocess.run(['python','temp.py'],input=ip_data.encode(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=5)
        else:
            result = subprocess.run(['./a.exe'],input=ip_data.encode(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=5)
         
        os.chdir(curr_dir)
        stdout_output = result.stdout
        stderr_output = result.stderr

        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, cmd=result.args, output=result.stdout, stderr=result.stderr)

        return result.stdout.decode('utf8')
    
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
        return "Error: File not found."
   
    except PermissionError as e:
        print(f"Error: Permission denied for {e.filename}.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error: Command {e.cmd} returned non-zero exit code {e.returncode}.")
        print(f"Stadard Output: {e.output}")
        print(f"Standard Error: {e.stderr}")
        os.chdir(curr_dir)
        return "Error occurred during Execution."
###############################################################