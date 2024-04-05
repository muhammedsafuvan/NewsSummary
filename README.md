How to run?

Run the server:
uvicorn main:app --reload

Run GUI:
python gui.py

UI:
<img width="1213" alt="image" src="https://github.com/muhammedsafuvan/NewsSummary/assets/72472792/55d76d85-ba5f-4374-ad13-ff32e08b4742">

O/P:
<img width="1204" alt="image" src="https://github.com/muhammedsafuvan/NewsSummary/assets/72472792/7602b52b-b859-46f1-8ba2-31135b6be94d">

API Testing: Postman
<img width="1026" alt="image" src="https://github.com/muhammedsafuvan/NewsSummary/assets/72472792/6550df1f-259a-4292-bf22-1cfbd3a4ffcc">


Tkinter package issue:

'''
import tkinter as tk
  File "/usr/local/Cellar/python@3.10/3.10.14/Frameworks/Python.framework/Versions/3.10/lib/python3.10/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter' 

'''

Fix:
If you are facing the aforementioned erro, try this.
'tkinter' is no longer included with this formula, but it is available separately:
'''
  brew install python-tk@3.10

'''
