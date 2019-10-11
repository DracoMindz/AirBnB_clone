Private intRand As Integer = 1
Private intButtonID As Integer = 0


Private Sub btnStart_Click(sender As Object, e As EventArgs) _
         Handles btnStart.Click
 
         Reset()
 
         btnPlay1.Text = "O"
         intButtonID = 1
         Timer1.Start()
 
      End Sub
      

Private Sub Reset()   'Reset Defaults'
 
         For Each ctl In Controls
 
            If TypeOf ctl Is Button Then
 
               ctl.Text = ""
 
               ctl.Enabled = True
 
            End If
 
            Next ctl
 
            btnStart.Text = "Start / Restart"
      End Sub
Private Sub Timer1_Tick(sender As Object, e As EventArgs) _
         Handles Timer1.Tick
 
         intRand += 1
 
         If intRand = 10 Then
 
            intRand = 1
 
         End If
 
      End Sub
       Private Sub Button1_Click(ByVal sender As System.Object,_
            ByVal e As System.EventArgs) Handles btnPlay1.Click, _
            btnPlay2.Click, btnPlay3.Click, btnPlay4.Click, _
            btnPlay5.Click, btnPlay6.Click, btnPlay7.Click, _
            btnPlay8.Click, btnPlay9.Click
 
         sender.Text = "X"
         sender.Enabled = False
 
         Timer1.Stop()
 
         intButtonID = Int32.Parse(sender.Tag)
 
         If intRand = intButtonID Then
 
            intRand = intRand + 1
 
         End If
 
         If intRand > 0 Then
 
            ComputerPlayer()
 
            intRand = 0
 
         ElseIf intRand = 0 Then
 
            Choices()
 
         End If
 
 
         WhoWins()
 
      End Sub
      
 Public Sub ComputerPlayer()   'Computer Player'
 
         Select Case intRand
 
            Case 1
 
               btnPlay1.Text = "O"
               btnPlay1.Enabled = False
 
            Case 2
 
               btnPlay1.Text = "O"
               btnPlay2.Enabled = False
 
            Case 3
 
               btnPlay1.Text = "O"
               btnPlay3.Enabled = False
 
            Case 4
 
               btnPlay1.Text = "O"
               btnPlay4.Enabled = False
 
            Case 5
 
               btnPlay1.Text = "O"
               btnPlay5.Enabled = False
 
            Case 6
 
               btnPlay1.Text = "O"
               btnPlay6.Enabled = False
 
            Case 7
 
               btnPlay1.Text = "O"
               btnPlay7.Enabled = False
 
            Case 8
 
               btnPlay1.Text = "O"
               btnPlay8.Enabled = False
 
            Case 9
 
               btnPlay1.Text = "O"
               btnPlay9.Enabled = False
 
         End Select
 
      End Sub
      'checks which buttons were pressed,'
      'then set all properties accordingly'
      Public Sub Choices()
 
         Select Case intButtonID
            Case 1
 
               If btnPlay2.Text = "X" And _
                  btnPlay3.Enabled = True Then
 
                  btnPlay3.Text = "O"
                  btnPlay3.Enabled = False
 
               ElseIf btnPlay3.Text = "X" And _
                  btnPlay2.Enabled = True Then
 
                  btnPlay2.Text = "O"
                  btnPlay2.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay9.Enabled = True Then
 
                  btnPlay9.Text = "O"
                  btnPlay9.Enabled = False
 
               ElseIf btnPlay9.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay4.Text = "X" And _
                  btnPlay7.Enabled = True Then
 
                  btnPlay7.Text = "O"
                  btnPlay7.Enabled = False
 
               ElseIf btnPlay7.Text = "X" And _
                  btnPlay4.Enabled = True Then
 
                  btnPlay4.Text = "O"
                  btnPlay4.Enabled = False
 
               ElseIf btnPlay8.Text = "X" Or _
                  btnPlay6.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 2
 
               If btnPlay1.Text = "X" And _
                  btnPlay3.Enabled = True Then
 
                  btnPlay3.Text = "O"
                  btnPlay3.Enabled = False
 
               ElseIf btnPlay1.Text = "X" And _
                  btnPlay1.Enabled = True Then
 
                  btnPlay1.Text = "O"
                  btnPlay1.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay8.Enabled = True Then
 
                  btnPlay8.Text = "O"
                  btnPlay8.Enabled = False
 
               ElseIf btnPlay8.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay6.Text = "X" Or _
                  btnPlay4.Text = "X" Or _
                  btnPlay7.Text = "X" Or _
                  btnPlay9.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 3
 
               If btnPlay1.Text = "X" And _
                  btnPlay2.Enabled = True Then
 
                  btnPlay2.Text = "O"
                  btnPlay2.Enabled = False
 
               ElseIf btnPlay2.Text = "X" And _
                  btnPlay1.Enabled = True Then
 
                  btnPlay1.Text = "O"
                  btnPlay1.Enabled = False
 
               ElseIf btnPlay6.Text = "X" And _
                  btnPlay9.Enabled = True Then
 
                  btnPlay9.Text = "O"
                  btnPlay9.Enabled = False
 
               ElseIf btnPlay9.Text = "X" And _
                  btnPlay6.Enabled = True Then
 
                  btnPlay6.Text = "O"
                  btnPlay6.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay7.Enabled = True Then
 
                  btnPlay7.Text = "O"
                  btnPlay7.Enabled = False
 
               ElseIf btnPlay7.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay8.Text = "X" Or _
                  btnPlay4.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 4
 
               If btnPlay1.Text = "X" And _
                  btnPlay7.Enabled = True Then
 
                  btnPlay7.Text = "O"
                  btnPlay7.Enabled = False
 
               ElseIf btnPlay7.Text = "X" And _
                  btnPlay1.Enabled = True Then
 
                  btnPlay1.Text = "O"
                  btnPlay1.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay6.Enabled = True Then
 
                  btnPlay6.Text = "O"
                  btnPlay6.Enabled = False
 
               ElseIf btnPlay6.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay2.Text = "X" Or _
                  btnPlay3.Text = "X" Or _
                  btnPlay8.Text = "X" Or _
                  btnPlay9.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 5
 
               If btnPlay1.Text = "X" And _
                  btnPlay9.Enabled = True Then
 
                  btnPlay9.Text = "O"
                  btnPlay9.Enabled = False
 
               ElseIf btnPlay9.Text = "X" And _
                  btnPlay1.Enabled = True Then
 
                  btnPlay1.Text = "O"
                  btnPlay1.Enabled = False
 
               ElseIf btnPlay2.Text = "X" And _
                  btnPlay8.Enabled = True Then
 
                  btnPlay8.Text = "O"
                  btnPlay8.Enabled = False
 
               ElseIf btnPlay8.Text = "X" And _
                  btnPlay2.Enabled = True Then
 
                  btnPlay2.Text = "O"
                  btnPlay2.Enabled = False
 
               ElseIf btnPlay3.Text = "X" And _
                  btnPlay7.Enabled = True Then
 
                  btnPlay7.Text = "O"
                  btnPlay7.Enabled = False
 
               ElseIf btnPlay7.Text = "X" And _
                  btnPlay3.Enabled = True Then
 
                  btnPlay3.Text = "O"
                  btnPlay3.Enabled = False
 
               ElseIf btnPlay6.Text = "X" And _
                  btnPlay4.Enabled = True Then
 
                  btnPlay4.Text = "O"
                  btnPlay4.Enabled = False
 
               ElseIf btnPlay4.Text = "X" And _
                  btnPlay6.Enabled = True Then
 
                  btnPlay6.Text = "O"
                  btnPlay6.Enabled = False
 
               End If
 
            Case 6
 
               If btnPlay3.Text = "X" And _
                  btnPlay9.Enabled = True Then
 
                  btnPlay9.Text = "O"
                  btnPlay9.Enabled = False
 
               ElseIf btnPlay9.Text = "X" And _
                  btnPlay3.Enabled = True Then
 
                  btnPlay3.Text = "O"
                  btnPlay3.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay4.Enabled = True Then
 
                  btnPlay4.Text = "O"
                  btnPlay4.Enabled = False
 
               ElseIf btnPlay4.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay1.Text = "X" Or _
                  btnPlay2.Text = "X" Or _
                  btnPlay7.Text = "X" Or _
                  btnPlay8.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 7
 
               If btnPlay1.Text = "X" And _
                  btnPlay4.Enabled = True Then
 
                  btnPlay4.Text = "O"
                  btnPlay4.Enabled = False
 
               ElseIf btnPlay4.Text = "X" And _
                  btnPlay1.Enabled = True Then
 
                  btnPlay1.Text = "O"
                  btnPlay1.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay3.Enabled = True Then
 
                  btnPlay3.Text = "O"
                  btnPlay3.Enabled = False
 
               ElseIf btnPlay3.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay8.Text = "X" And _
                  btnPlay9.Enabled = True Then
 
                  btnPlay9.Text = "O"
                  btnPlay9.Enabled = False
 
               ElseIf btnPlay9.Text = "X" And _
                  btnPlay8.Enabled = True Then
 
                  btnPlay8.Text = "O"
                  btnPlay8.Enabled = False
 
               ElseIf btnPlay6.Text = "X" Or _
                  btnPlay2.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 8
 
               If btnPlay2.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay2.Enabled = True Then
 
                  btnPlay2.Text = "O"
                  btnPlay2.Enabled = False
 
               ElseIf btnPlay9.Text = "X" And _
                  btnPlay7.Enabled = True Then
 
                  btnPlay7.Text = "O"
                  btnPlay7.Enabled = False
 
               ElseIf btnPlay7.Text = "X" And _
                  btnPlay9.Enabled = True Then
 
                  btnPlay9.Text = "O"
                  btnPlay9.Enabled = False
 
               ElseIf btnPlay6.Text = "X" Or _
                  btnPlay3.Text = "X" Or _
                  btnPlay1.Text = "X" Or _
                  btnPlay4.Text = "X" Then
 
                  Play()
 
               End If
 
            Case 9
 
               If btnPlay6.Text = "X" And _
                  btnPlay3.Enabled = True Then
 
                  btnPlay3.Text = "O"
                  btnPlay3.Enabled = False
 
               ElseIf btnPlay3.Text = "X" And _
                  btnPlay6.Enabled = True Then
 
                  btnPlay6.Text = "O"
                  btnPlay6.Enabled = False
 
               ElseIf btnPlay5.Text = "X" And _
                  btnPlay1.Enabled = True Then
 
                  btnPlay1.Text = "O"
                  btnPlay1.Enabled = False
 
               ElseIf btnPlay1.Text = "X" And _
                  btnPlay5.Enabled = True Then
 
                  btnPlay5.Text = "O"
                  btnPlay5.Enabled = False
 
               ElseIf btnPlay8.Text = "X" And _
                  btnPlay7.Enabled = True Then
 
                  btnPlay7.Text = "O"
                  btnPlay7.Enabled = False
               ElseIf btnPlay7.Text = "X" And _
                  btnPlay8.Enabled = True Then
 
                  btnPlay8.Text = "O"
                  btnPlay8.Enabled = False
 
               ElseIf btnPlay2.Text = "X" Or _
                  btnPlay4.Text = "X" Then
 
                  Play()
 
               End If
 
         End Select
 
      End Sub
      Public Sub Play()   'Play'
 
         For Each ctl As Control In Me.Controls
 
            If intButtonID < 9 Then
 
               If (ctl.Name.StartsWith("Button" _
                  & intButtonID + 1)) Then
 
                  Dim btn As Button = DirectCast(ctl, Button)
 
               If btn.Enabled = True Then
 
                  btn.Text = "O"
                  btn.Enabled = False
 
               Else
 
                  intButtonID = intButtonID + 1
 
               End If
 
            End If
 
            Else
 
               If (ctl.Name.StartsWith("btnPlay1")) Then
 
                  Dim btn As Button = DirectCast(ctl, Button)
 
                  If btn.Enabled = True Then
 
                     btn.Text = "O"
                     btn.Enabled = False
 
                  Else
 
                     intButtonID = intButtonID + 1
 
                  End If
 
               End If
 
            End If
 
         Next
 
      End Sub
      'Checks who wins between player and computer'
      Public Sub WhoWins()
 
         If (btnPlay1.Text = "O" And btnPlay2.Text = "O" _
            And btnPlay3.Text = "O") _
            Or (btnPlay4.Text = "O" And btnPlay5.Text = "O" _
            And btnPlay6.Text = "O") _
            Or (btnPlay7.Text = "O" And btnPlay8.Text = "O" _
            And btnPlay9.Text = "O") _
            Or (btnPlay1.Text = "O" And btnPlay4.Text = "O" _
            And btnPlay7.Text = "O") _
            Or (btnPlay2.Text = "O" And btnPlay5.Text = "O" _
            And btnPlay8.Text = "O") _
            Or (btnPlay3.Text = "O" And btnPlay6.Text = "O" _
            And btnPlay9.Text = "O") _
            Or (btnPlay1.Text = "O" And btnPlay5.Text = "O" _
            And btnPlay9.Text = "O") _
            Or (btnPlay7.Text = "O" And btnPlay5.Text = "O" _
            And btnPlay3.Text = "O") Then
 
            MessageBox.Show ("You Lose")
 
            Reset()
 
         ElseIf (btnPlay1.Text = "X" And btnPlay2.Text = "X" _
            And btnPlay3.Text = "X") _
            Or (btnPlay4.Text = "X" And btnPlay5.Text = "X" _
            And btnPlay6.Text = "X") _
            Or (btnPlay7.Text = "X" And btnPlay8.Text = "X" _
            And btnPlay9.Text = "X") _
            Or (btnPlay1.Text = "X" And btnPlay4.Text = "X" _
            And btnPlay7.Text = "X") _
            Or (btnPlay2.Text = "X" And btnPlay5.Text = "X" _
            And btnPlay8.Text = "X") _
            Or (btnPlay3.Text = "X" And btnPlay6.Text = "X" _
            And btnPlay9.Text = "X") _
            Or (btnPlay1.Text = "X" And btnPlay5.Text = "X" _
            And btnPlay9.Text = "X") _
            Or (btnPlay7.Text = "X" And btnPlay5.Text = "X" _
            And btnPlay3.Text = "X") Then
 
            MessageBox.Show ("You Win")
 
            Reset()
 
         End If
    
    End Sub
    


