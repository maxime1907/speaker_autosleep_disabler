Write-Output "Speaker autosleep disabler"
while ($true) {
  $song = New-Object Media.SoundPlayer 'WakeupHum.wav'
  $song.PlaySync()
}
