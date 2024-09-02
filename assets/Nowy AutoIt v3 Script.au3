; Wskaźnik okna, w którym chcemy kliknąć
$windowTitle = "Minecraft* 1.20.6 - Singleplayer"

; Wskaźnik kontrolki, w którą chcemy kliknąć
$controlID = "GLFW30" ; Można użyć klasy kontrolki lub tekstu kontrolki

; Kliknięcie kontrolki
ControlSend($windowTitle, "", $controlID, "{LButton down}")
