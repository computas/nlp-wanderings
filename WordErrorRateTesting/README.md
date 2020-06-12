# Word Error Rate Test

Vi utførte en word error rate test av Azure Cognitive services sin baseline modell. Testen er gjennomført ved å lese opp store norske leksikon sin side om politikk. 
https://snl.no/politikk
Man trenger et Azure abonement og opprette en cognetive service resource. 

### Transkriber lydfil 

``` python transkribeText.py <cognetive_service_key>```

### Prosesser tekstfilene så de er sammenlignbare ved å ta vekk tegnsetting etc ###
``` python lagtekstfiler.py ```

### Bruk pakken wer til å finne Word Error Rate ###

``` pip install asr-evaluation ``` 

```  wer tts.txt orginal.txt  ``` 

