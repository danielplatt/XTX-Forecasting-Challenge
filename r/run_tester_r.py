import os
import subprocess
import platform

def printUsage():
    print("---------------------------------------------------------------------------------------------------------------------")
    print("Usage: Should run in the /r directory. Please do not move this file!")
    print("On Mac/Linux OS: python3 run_tester_r.py, on Windows OS: py run_tester_r.py")
    print("This script will ensure that all required components for the model tester are present and in the correct directories.")
    print("Additionally, the script will run the model tester on your R submissions.")
    print("It is HIGHLY recommended to run this script and fix any errors prior to submitting your code.")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("")

def printExpectedFolderStructure():
    print("|--README.md")
    print("|-- r")
    print( "--|-- core.r")
    print("---|-- requirements.txt")
    print("---|-- run_tester_python.py")
    print("---|-- submission.r")
    print("|-- src")
    print("---|-- model_tester.py")
    print("---|-- scorer.py")
    print("|-- data.csv")

def checkDataFilePresent():
    if not os.path.isfile("../data.csv"):
        print("[ERROR] data.csv file not found at expected location.")
        print("[ERROR] Please, refer to the structure below:")
        print("")
        printExpectedFolderStructure()
        quit()
    else:
        print("[SUCCESS] data.csv found!")

def checkSubmissionFile():
    if not os.path.isfile("submission.r"):
        print("[ERROR] submission.r file not found at expected location.")
        print("[ERROR] Please, refer to the structure below:")
        print("")
        printExpectedFolderStructure()
        quit()
    else:
        print("[SUCCESS] submission.r found!")

def checkModelTester():
    if not os.path.isfile("../src/model_tester.py"):
        print("[ERROR] model_tester.py file not found at expected location.")
        print("[ERROR] Please, refer to the structure below:")
        print("")
        printExpectedFolderStructure()
        quit()
    else:
        print("[SUCCESS] model_tester.py found!")
    
def checkScorerFile():
    if not os.path.isfile("../src/scorer.py"):
        print("[ERROR] scorer.py file not found at expected location.")
        print("[ERROR] Please, refer to the structure below:")
        print("")
        printExpectedFolderStructure
        quit()
    else:
        print("[SUCCESS] scorer.py found!")

def checkRequirementsFile():
    if not os.path.isfile("requirements.txt"):
        print("[ERROR] requirements.txt file not found at expected location.")
        print("[ERROR] Please, refer to the structure below:")
        print("")
        printExpectedFolderStructure()
        quit()
    else:
        print("[SUCCESS] requirements.txt found!")

def checkCoreFile():
    if not os.path.isfile("core.r"):
        print("[ERROR] core.r file not found at expected location.")
        print("[ERROR] Please, refer to the structure below:")
        print("")
        printExpectedFolderStructure()
        quit()
    else:
        print("[SUCCESS] core.r  found!")

def folderValidation():
    print("----------------------------")
    print("Starting Folder Validation.")
    print("----------------------------")
    print("")
    checkDataFilePresent()
    checkSubmissionFile()
    checkModelTester()
    checkScorerFile()
    checkRequirementsFile()
    checkCoreFile()
    print("")
    print("-----------------------------------")
    print("Finished Running Folder Validation.")
    print("-----------------------------------")

def checkPWD():
    if not os.getcwd().endswith("r"):
        print("[ERROR] This script is not being run from the r directory!")
        quit()
    else:
        print("[SUCCESS] script running in python directory.")

def runModelTester():
    if platform.system == 'Windows':
        subprocess.run(["py", "../src/model_tester.py", "r"])
    else:
        subprocess.run(["python3", "../src/model_tester.py", "r"])

def main():
    printUsage()
    checkPWD()
    folderValidation()
    runModelTester()

if __name__ == "__main__":
    main()
