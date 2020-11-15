Dim oPlayer
Set oPlayer = CreateObject("WMPlayer.OCX")

i = 0
Do While i = 0
oPlayer.URL = "WakeupHum.wav"
oPlayer.controls.play
While oPlayer.playState <> 1 ' 1 = Stopped
WScript.Sleep 100
Wend

Loop

oPlayer.close
WScript.Quit

