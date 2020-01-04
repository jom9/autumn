import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from RulesEngine.BoardState import BoardState
def compareFiles(filename1,filename2):
    file1 = open(filename1,'r')
    file2 = open(filename2,'r')
    if file1.read()== file2.read():
        return True
    else:
        return False
def IslandTest():
        if compareFiles('CardAnalyzer\\GeneratedCards\\Island.py','Test\\ExampleGeneratedCards\\Island.py'):
            return True
        return False
def Underground_Sea():
    if compareFiles('CardAnalyzer\\GeneratedCards\\Underground_Sea.py','Test\\ExampleGeneratedCards\\Underground_Sea.py'):
        return True
    return False
def main():
    print('Island Test Failed:',IslandTest())
    print('Underground Sea Faild',Underground_Sea())
    
