place1 = 1
place2 = 2
place3 = 3
place4 = 4
place5 = 5
place6 = 6
place7 = 7
place8 = 8
place9 = 9
symbol1 = "X"
symbol2 = "O"
reset:
TextWindow.Clear()
TextWindow.Write(place1 + " ")
TextWindow.Write(place2 + " ")
TextWindow.WriteLine(place3 + " ")
TextWindow.Write(place4 + " ")
TextWindow.Write(place5 + " ")
TextWindow.WriteLine(place6 + " ")
TextWindow.Write(place7 + " ")
TextWindow.Write(place8 + " ")
TextWindow.WriteLine(place9 + " ")
TextWindow.WriteLine("Where would you like to go to (choose a number from 1 to 9 and press enter)?")
n = TextWindow.Read()
If n = 1 then
  If place1 = symbol1 or place1 = symbol2 then
    Goto ai
  Else
    place1 = symbol1
  EndIf
ElseIf n = 2 then
  If place2 = symbol1 or place2 = symbol2 then
    Goto ai
  Else
    place2 = symbol1
  EndIf
ElseIf n = 3 then
  If place3 = symbol1 or place3 = symbol2 then
    Goto ai
  Else
    place3 = symbol1
  EndIf
ElseIf n = 4 then
  If place4 = symbol1 or place4 = symbol2 then
    Goto ai
  Else
    place4 = symbol1
  EndIf
ElseIf n = 5 then
  If place5 = symbol1 or place5 = symbol2 then
    Goto ai
  Else
    place5 = symbol1
  EndIf
ElseIf n = 6 then
  If place6 = symbol1 or place6 = symbol2 then
    Goto ai
  Else
    place6 = symbol1
  EndIf
ElseIf n = 7 then
  If place8 = symbol1 or place7 = symbol2 then
    Goto ai
  Else
    place7 = symbol1
  EndIf
ElseIf n = 8 then
  If place8 = symbol1 or place8 = symbol2 then
    Goto ai
  Else
    place8 = symbol1
  EndIf
ElseIf n = 9 then
  If place9 = symbol1 or place9 = symbol2 then
    Goto ai
  Else
    place9 = symbol1
  EndIf
EndIf
Goto ai
ai:
n = Math.GetRandomNumber(9)
If n = 1 then
  If place1 = symbol1 or place1 = symbol2 then
    Goto ai
  Else
    place1 = symbol2
  EndIf
ElseIf n = 2 then
  If place2 = symbol1 or place2 = symbol2 then
    Goto ai
  Else
    place2 = symbol2
  EndIf
ElseIf n = 3 then
  If place3 = symbol1 or place3 = symbol2 then
    Goto ai
  Else
    place3 = symbol2
  EndIf
ElseIf n = 4 then
  If place4 = symbol1 or place4 = symbol2 then
    Goto ai
  Else
    place4 = symbol2
  EndIf
ElseIf n = 5 then
  If place5 = symbol1 or place5 = symbol2 then
    Goto ai
  Else
    place5 = symbol2
  EndIf
ElseIf n = 6 then
  If place6 = symbol1 or place6 = symbol2 then
    Goto ai
  Else
    place6 = symbol2
  EndIf
ElseIf n = 7 then
  If place7 = symbol1 or place7 = symbol2 then
    Goto ai
  Else
    place7 = symbol2
  EndIf
ElseIf n = 8 then
  If place8 = symbol1 or place8 = symbol2 then
    Goto ai
  Else
    place8 = symbol2
  EndIf
ElseIf n = 9 then
  If place9 = symbol1 or place9 = symbol2 then
    Goto ai
  Else
    place9 = symbol2
  EndIf
EndIf
If place1 = symbol1 and place2 = symbol1 and place3 = symbol1 or place4 = symbol1 and place5 = symbol1 and place6 = symbol1 or place7 = symbol1 and place8 = symbol1 and place9 = symbol1 or place1 = symbol1 and place4 = symbol1 and place7 = symbol1 or place2 = symbol1 and place5 = symbol1 and place8 = symbol1 or place3 = symbol1 and place6 = symbol1 and place9 = symbol1 or place1 = symbol1 and place5 = symbol1 and place9 = symbol1 or place3 = symbol1 and place5 = symbol1 and place7 = symbol1 then
  TextWindow.WriteLine("Player 1 (" + symbol1 + ") wins!")
ElseIf place1 = symbol2 and place2 = symbol2 and place3 = symbol2 or place4 = symbol2 and place5 = symbol2 and place6 = symbol2 or place7 = symbol2 and place8 = symbol2 and place9 = symbol2 or place1 = symbol2 and place4 = symbol2 and place7 = symbol2 or place2 = symbol2 and place5 = symbol2 and place8 = symbol2 or place3 = symbol2 and place6 = symbol2 and place9 = symbol2 or place1 = symbol2 and place5 = symbol2 and place8 = symbol2 or place3 = symbol2 and place5 = symbol2 and place7 = symbol2 then
  TextWindow.WriteLine("Player 2 (" + symbol2 + ") wins!")
Else
  Goto reset
EndIf