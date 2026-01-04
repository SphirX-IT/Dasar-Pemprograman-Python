iq_input = input('IQ mu brp bro? ')
iq = int(iq_input)

if iq < 0 :
    print('ga normal lu')
elif iq >= 0 and iq <=60 :
    print('RS jiwa siap menampung')
elif iq >= 61 and iq <=80 :
    print('SDM Indo banget')
elif iq >= 81 and iq <=95 :
    print('rata-rata')
elif iq >= 96 and iq <=110 :
    print('diatas rata-rata')
elif iq >= 111 and iq <=130 :
    print('lu pintar')
elif iq >= 131 and iq <=200 :
    print('Genius')
elif iq >= 201 and iq <=300 :
    print('ilmuan')
elif iq >= 301 :
    print('Alien')
else :
    print('error')