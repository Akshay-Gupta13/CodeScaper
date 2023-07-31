import subprocess
import os

def compile_code(file_path, language):
    compilers = {
        'c': 'gcc',
        'cpp': 'g++',
    }
    compiler = compilers.get(language)
    if not compiler:
        return 0

    try:
        curr_dir = os.getcwd()
        trash_dir = os.path.join("onlinejudge", "trash")
        os.chdir(trash_dir)
        compiled_file = subprocess.run([compiler, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir(curr_dir)

        std_error = compiled_file.stderr.decode("utf-8")
        if std_error == "":
            return 1
        else:
            return 0
    except Exception as e:
        os.chdir(curr_dir)
        return f"CodeError: {e}"

def  run_code(language, input_data):
    try:
        curr_dir = os.getcwd()
        trash_dir = os.path.join("onlinejudge", "trash")
        os.chdir(trash_dir)

        if language == 'py':
            result = subprocess.run(['python', 'temp.py'], input=input_data.encode(),
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        else:
            result = subprocess.run(['./a.exe'], input=input_data.encode(),
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)

        os.chdir(curr_dir)
        output = (result.stdout + result.stderr).decode('utf8')

        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, cmd=result.args, output=output)

        return output
    except FileNotFoundError as e:
        os.chdir(curr_dir)
        return f"Error: {e.filename} not found."
    except PermissionError as e:
        os.chdir(curr_dir)
        return f"Error: Permission denied for {e.filename}."
    except subprocess.CalledProcessError as e:
        os.chdir(curr_dir)
        return f"Error: Command {e.cmd} returned non-zero exit code {e.returncode}."
    except Exception as e:
        os.chdir(curr_dir)
        return f"Error occurred during execution: {e}"


def check_tc(tc, language):
    for idx, test_case in enumerate(tc, 1):
        formatted_input = str(test_case.tc_input).replace(" ", "\n")
        expected_output = test_case.tc_output.strip()
        actual_output = run_code(language, formatted_input).strip()

        if actual_output != expected_output:
            return f"Wrong Answer on test case {idx}"

    return "Accepted"
 