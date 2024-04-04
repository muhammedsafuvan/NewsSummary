How to run?
uvicorn main:app --reload

Tkinter package issue:

'''
import tkinter as tk
  File "/usr/local/Cellar/python@3.10/3.10.14/Frameworks/Python.framework/Versions/3.10/lib/python3.10/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter' 

'''

Fix:
'tkinter' is no longer included with this formula, but it is available separately:
'''
  brew install python-tk@3.10

'''
