Option Explicit

On Error Resume Next



WScript.Echo "The Script has Started."


  Dim xlApp1 
  Dim xlBook1

  Set xlApp1 = CreateObject("Excel.Application") 
  Set xlBook1 = xlApp1.Workbooks.Open("G:\Fractal\Europe PSC (15-SPG-1056)\Automation\Macro_all\Inventory Marco.xlsm", 0, False) 
  xlApp1.Run "Inventory_IMEA"


xlBook1.Close False
set xlBook1 = Nothing

xlApp1.Quit
Set xlApp1 = Nothing

WScript.Echo "The Script has Finished."
WScript.Quit