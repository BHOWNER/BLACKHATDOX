import sys, os, time, signal, webbrowser, platform, subprocess
def FULLDOX():
    Name = input('Псевдоним жертвы: ')
    F_name = input('Имя или фамилия, если нет то оставляйте пробел:')
    print("Black hat Начинает поиск по данному псевдониму")
    webbrowser.open('https://pipl.com/search/?q='+Name+'+'+F_name)
    time.sleep(2)
    webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+' '+F_name)
    time.sleep(2)
    webbrowser.open('https://www.spokeo.com/'+Name+'-'+F_name)
    time.sleep(2)
    webbrowser.open('https://www.flickr.com/search/people/?username='+Name+' '+F_name)
    time.sleep(2)
    webbrowser.open('https://www.linkedin.com/pub/dir/'+Name+'/'+F_name)
    time.sleep(2)
    webbrowser.open('https://plus.google.com/s/'+Name+' '+F_name+'/people')
    time.sleep(2)
    webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
    time.sleep(2)
    webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
    time.sleep(2)
    webbrowser.open('https://www.peekyou.com/'+Name+'_'+F_name)
    time.sleep(2)
    webbrowser.open('https://twitter.com/search?f=users&vertical=default&q= '+Name+' '+F_name)
    time.sleep(2)
    webbrowser.open('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+Name+'&ln='+F_name)
    time.sleep(2)
    webbrowser.open('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+Name+'&ln='+F_name+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
    time.sleep(2)
    webbrowser.open('https://myspace.com/search?q='+Name+' '+F_name)
    time.sleep(2)
    webbrowser.open('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+Name+'+'+F_name)
    time.sleep(2)
    webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
    time.sleep(2)
    webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
    time.sleep(2)
    
FULLDOX()
