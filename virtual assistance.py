import os
import pyttsx3

#set rate of speech
voiceEngine=pyttsx3.init()
voiceEngine.setProperty('rate',180)



#using list of programs/files for sorting user input
list=["open","execute","Open","Run","Launch","launch","run","Execute","yes","Yes","how's","my","want","know","How's","play","Play","How","how","take","","Take","download","friend","Friend","wish"]

lis=["chrom","Chrome","browser"]
lis1=["firefox","Firefox","browser","Browser","mozilla","Mozilla"]
lis2=["notepad","Notepad","Pad","pad"]
lis3=["windows","Windows"," media","Media", "player","Play","wmplayer","wm","WM"]
lis0=["This","Pc","this","pc","expl","Exp","documents","Documents"]
lis4=["calc","Calc","calculator"]
lis5=["mspaint","Paint","paint","MSpaint"]
lis6=["WINWORD","word","Microsoft","microsoft","Word","msword","MSWORD"]
lis7=["microsoft","point","Power","Point","power","windows"]
lis8=["excel","Excel","Microsoft","microsoft","MSexcel","EXCEL"]
lis9=["control","Control","Panel","controlpanel","pan","Pan","Con"]
lis10=["iexplor","internet","internet exp","IE","ie","Internet Exp","Iexplorer"]
lis11=["Ado","acrobat","Acrobat","reader","Reader","PDF","pdf","acrord32","Acrord32"]
lis12=["shutdown","poweroff","Shut","Off"]
lis13=["logoff","logout","Logout","lock","Lock"]
lis14=["Restart","restart","reboot","Reboot"]
lis15=["PC","device","computer",""]
lis16=["camera","selfie","Cam","Camera","era","capture"]
lis17=["calendar","Calendar","year","month"]
lis18=["outlookmail" ,"mail","outloo","Mail"]
lis19=["ms-windows-store","store","apps","applications"]
lis20=["message","Mess","chat","Chat"]
lis21=["microsoftEdge","edge","Edg","MicrosoftEdge"]
lis22=["msvideo","moviies and tv","Movies","TV","vid","tv","movies","movie"]
lis23=["gallery","phot","Phot","Galler","pictu","Pictures"]
lis24=["settings","Setti","setting","setti"]
lis25=["vlc","VLC"]
lis26=["bingweather","weath","Weather"]
lis27=["xbox","Xbox","XBOX","games","game"]
lis28=["security","windows security","Security","threat","Virus","antivirus","protec","defend","health of my pc","Health of my PC"]
lis29=["twitter","twitt","tweet","Tweet","Twitter"]
lis30=["onen","Onen","one","Onenote"]
lis31=["minecraft","Minecraft","Craf"]
lis32=["bingmaps","maps","map","location","Map"]
lis33=["mswindowsmusic","Groove","groove","groove music"]
lis34=["candycrushsodasaga","candy","crush","saga"]
lis35=["ms-clock","clock","alarm"]
lis36=["ms-cortana","Cort","corto","Cortana","cortana","cort"]
lis37=["date","time","Time","Date"]
lis38=["pycharm","Pycharm","charm","Charm"]
lis39=["jupyter notebook","book","Jupyter Notebook"]
lis40=["recycle bin","bin","Bin","Recycle"]
lis41=["winrar","WinRAR","Winrar","Rar"]
lis42=["vmware","VM","VMware"]
lis43=["info","msinfo32","system information"]
lis44=["task sheduler","Task Sheduler","sheduler","Shed"]
lis45=["Task manager","task manger","manager","Manager"]
lis46=["Wall","wall"]
lis47=["google search","find","Find","brow"]
lis48=["youtube search","Youtube search","youtube"]
lis49=["soundcloud search","Soundcloud search","soundcl"]
lis50=["screenshot","snipping tool","snip","Snip","Snipping tool","ScreenShot"]





ng=["dont","Don't","don't","Dont","Not","NOT"]
acc=["yes","Y","y","Yes"]
quit=["bye","later","good bye","quit","see","you","ok"]
conv=["How are you","fine","how","good","Good"]


#title
print("--------------------------------------------------------------------------------")
print("********Welcome to Virtual Assistant/Menu Driven Program using  Python********")
pyttsx3.speak("Welcome to Virtual Assistant/Menu Driven Program using Python")
print("                 ***Created by Tejas M N***")
print("--------------------------------------------------------------------------------")

#while True:
print("Hey there! What's your name? ")
pyttsx3.speak("Hey there! What's your name? ")
name=input()
print("Hello "+ name + " Nice to meet you")
pyttsx3.speak("Hello "+ name + " Nice to meet you")
print("So how can i help you?")
pyttsx3.speak("So how can i help you? ")

while True:
        
        
        a=input(">>")

        if any(word in a for word in list ) and (any(word in a for word in lis )and not(any(word in a for word in ng ))):
            c=input("Enter website/url?: ")
            os.system(f"start chrome {c}")
            print("Opening chrome for you...")
            pyttsx3.speak("Opening chrome for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis0 )and not(any(word in a for word in ng ))):
            c=input("Enter file location/directory: ")
            os.system(f" start explorer {c}")
            print("Opening explorer for you...")
            pyttsx3.speak("Opening explorer for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis2 )and not(any(word in a for word in ng ))):
            c=input("Enter file name: ")
            os.system(f"start notepad {c}")
            print("Opening notepad for for you...")
            pyttsx3.speak("Opening notepad for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis1 )and not(any(word in a for word in ng ))):
            c=input("Enter website/url?: ")
            os.system(f"start firefox {c}")
            print("Opening firefox for you...")
            pyttsx3.speak("Opening firefox for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis3 )and not(any(word in a for word in ng ))):
            os.system(f"start wmplayer")
            print("Opening windows media player for you...")
            pyttsx3.speak("Opening windows media player for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis4 )and not(any(word in a for word in ng ))):
            os.system(f"start calc ")
            print("Opening calculator for you...")
            pyttsx3.speak("Opening calculator for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis5 )and not(any(word in a for word in ng ))):
            os.system("start mspaint")
            print("Opening paint for you...")
            pyttsx3.speak("Opening paint for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis6 )and not(any(word in a for word in ng ))):
            
            os.system("start WINWORD ")
            print("Opening Word for you...")
            pyttsx3.speak("Opening Word  for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis7 )and not(any(word in a for word in ng ))):
            
            os.system("start POWERPNT ")
            print("Opening powerpoint for you...")
            pyttsx3.speak("Opening powerpoint for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis8 )and not(any(word in a for word in ng ))):
            
            os.system("start EXCEL ")
            print("Opening excel for you...")
            pyttsx3.speak("Opening excel for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis16 )and not(any(word in a for word in ng ))):
            os.system(f"start microsoft.windows.camera:  ")
            print("Opening camera for you...")
            pyttsx3.speak("Opening camera for you")
        
        elif any(word in a for word in list ) and (any(word in a for word in lis17 )and not(any(word in a for word in ng ))):
            os.system(f"start outlookcal:  ")
            print("Opening calendar for you...")
            pyttsx3.speak("Opening calendar for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis18)and not(any(word in a for word in ng ))):
            os.system(f"start outlookmail: ")
            print("Opening outlookmail for you...")
            pyttsx3.speak("Opening outlookmail for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis19)and not(any(word in a for word in ng ))):
            os.system(f"start ms-windows-store: ")
            print("Opening ms windows store for you...")
            pyttsx3.speak("Opening microsoft windows store  for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis20)and not(any(word in a for word in ng ))):
            os.system(f"start ms-chat:  ")
            print("Opening messages for you...")
            pyttsx3.speak("Opening messages for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis21)and not(any(word in a for word in ng ))):
            os.system(f"start microsoft-edge:  ")
            print("Opening microsoft edge for you...")
            pyttsx3.speak("Opening microsoft edge for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis22)and not(any(word in a for word in ng ))):
            os.system(f"start mswindowsvideo:  ")
            print("Opening microsoft windows video for you")
            pyttsx3.speak("Opening microsoft windows video for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis23)and not(any(word in a for word in ng ))):
            os.system(f"start ms-photos:  ")
            print("Opening microsoft photos for you")
            pyttsx3.speak("Opening microsoft photos for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis24)and not(any(word in a for word in ng ))):
            os.system(f"start ms-settings:  ")
            print("Opening  settings for you")
            pyttsx3.speak("Opening settings for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis25 )and not(any(word in a for word in ng ))):
            os.system(f"start vlc")
            print("Opening vlc media player for you...")
            pyttsx3.speak("Opening vlc media player for you")
        
        elif any(word in a for word in list ) and (any(word in a for word in lis26 )and not(any(word in a for word in ng ))):
            os.system(f"start bingweather:")
            print("Opening weather for you...")
            pyttsx3.speak("Opening weather for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis27 )and not(any(word in a for word in ng ))):
            os.system(f"start xbox:")
            print("Opening xbox  for you...")
            pyttsx3.speak("Opening xbox for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis28 )and not(any(word in a for word in ng ))):
            os.system(f"start windowsdefender:")
            print("Opening windows defender  for you...")
            pyttsx3.speak("Opening windows defender for you")
        
        elif any(word in a for word in list ) and (any(word in a for word in lis29 )and not(any(word in a for word in ng ))):
            os.system(f"start twitter:")
            print("Opening twitter  for you...")
            pyttsx3.speak("Opening twitter for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis30 )and not(any(word in a for word in ng ))):
            os.system(f"start onenote:")
            print("Opening onenote for you...")
            pyttsx3.speak("Opening onenote  for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis31 )and not(any(word in a for word in ng ))):
            os.system(f"start minecraft: ")
            print("Opening minecraft for you...")
            pyttsx3.speak("Opening minecraft:  for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis32 )and not(any(word in a for word in ng ))):
            os.system(f"start bingmaps: ")
            print("Opening map for you...")
            pyttsx3.speak("Opening map  for you")
        
        
        elif any(word in a for word in list ) and (any(word in a for word in lis33 )and not(any(word in a for word in ng ))):
            os.system(f"start mswindowsmusic: ")
            print("Opening groove music for you...")
            pyttsx3.speak("Opening groove music  for you ")

            
        elif any(word in a for word in list ) and (any(word in a for word in lis34 )and not(any(word in a for word in ng ))):
            os.system(f"start candycrushsodasaga: ")
            print("Opening candycrush soda saga for you...")
            pyttsx3.speak("Opening  candycrush soda saga for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis35 )and not(any(word in a for word in ng ))):
            os.system(f"start ms-clock:  ")
            print("Opening alarm and clock for you...")
            pyttsx3.speak("Opening  alarm and clock for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis36 )and not(any(word in a for word in ng ))):
            os.system(f"start ms-cortana:  ")
            print("Opening cortana for you...")
            pyttsx3.speak("Opening  cortana for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis37 )and not(any(word in a for word in ng ))):
            os.system(f"start  timedate.cpl ")
            print("Opening date and time for you...")
            pyttsx3.speak("Opening  date and time for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis38 )and not(any(word in a for word in ng ))):
            os.system(f"start pycharm64 ")
            print("Opening pycharm for you...")
            pyttsx3.speak("Opening  pycharm  for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis39 )and not(any(word in a for word in ng ))):
            os.system("start jupyter notebook ")
            print("Opening jupyter notebook for you...")
            pyttsx3.speak("Opening  jupyter notebook for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis40 )and not(any(word in a for word in ng ))):
            os.system("start shell:RecycleBinFolder ")
            print("Opening recycle bin for you...")
            pyttsx3.speak("Opening  recycle bin for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis41 )and not(any(word in a for word in ng ))):
            os.system("start WinRAR ")
            print("Opening winrar for you...")
            pyttsx3.speak("Opening  winrar for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis42 )and not(any(word in a for word in ng ))):
            os.system("start VMware ")
            print("Opening VMware for you...")
            pyttsx3.speak("Opening  VMware for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis43)and not(any(word in a for word in ng ))):
            os.system("start msinfo32 ")
            print("Opening system information for you...")
            pyttsx3.speak("Opening  system information for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis44)and not(any(word in a for word in ng ))):
            os.system("start taskschd.msc ")
            print("Opening task sheduler for you...")
            pyttsx3.speak("Opening  task sheduler for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis45)and not(any(word in a for word in ng ))):
            os.system("start taskmgr ")
            print("Opening task manager  for you...")
            pyttsx3.speak("Opening  task manager for you")
            
        elif any(word in a for word in list ) and (any(word in a for word in lis46)and not(any(word in a for word in ng ))):
            os.system("start firewall.cpl ")
            print("Opening firewall  for you...")
            pyttsx3.speak("Opening  firewall for you")
        
        elif any(word in a for word in lis47 ):
            find=input("Search for?: ")
            new=find.replace(" ","+")
            print(f"Searching for {find}...")
            pyttsx3.speak(f"Searching for {find} ")
            os.system(f" chrome google.com/search?q={new}")
            
        elif any(word in a for word in lis48 ):
            find=input("Search for?: ")
            new=find.replace(" ","+")
            print(f"Searching for {find}...")
            pyttsx3.speak(f"Searching for {find} ")
            os.system(f" chrome https://youtube.com/results?search_query={new}")
            
        elif any(word in a for word in lis49 ):
            find=input("Search for?: ")
            new=find.replace(" ","+")
            print(f"Searching for {find}...")
            pyttsx3.speak(f"Searching for {find} ")
            os.system(f" chrome https://m.soundcloud.com/search?q={new}")
        
        elif any(word in a for word in list ) and (any(word in a for word in lis50)and not(any(word in a for word in ng ))):
            os.system(f"start snippingtool")
            print("Opening snipping tool for you...")
            pyttsx3.speak("Opening snipping tool for you")
            

        elif any(word in a for word in list ) and (any(word in a for word in lis9 )and not(any(word in a for word in ng ))):
            os.system(f"start control")
            print("Opening control panel for you...")
            pyttsx3.speak("Opening control panel for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis10 )and not(any(word in a for word in ng ))):
            c=input("Enter website/url?: ")
            os.system(f"start iexplore {c}")
            print("Opening internet explorer for you...")
            pyttsx3.speak("Opening internet explorer for you")

        elif any(word in a for word in list ) and (any(word in a for word in lis11 )and not(any(word in a for word in ng ))):
            c=input("Enter file name: ")
            os.system(f"start acrord32 {c}")
            
        elif any(word in a for word in lis15 ) and (any(word in a for word in lis12 )and not(any(word in a for word in ng ))):
            print("Warning : Before you proceed to shutdown/restart/logoff save and close the programs running in the background ")
            pyttsx3.speak("Warning : Before you proceed to shutdown or restart or logoffsave and close the programs running in the background ")
            print("Do you wish to continue?(y/n)")
            pyttsx3.speak("Do you wish to continue?")
            p=input()
            if any(word in p for word in acc ):
                os.system("shutdown -s")
            elif any(word in p for word in ng) :
                print("Oops I didn't get you try something else ")
                pyttsx3.speak("Oops I didn't get you try something else")
                           
        elif any(word in a for word in lis15 ) and (any(word in a for word in lis13 )and not(any(word in a for word in ng ))):
            print("Warning : Before you proceed to shutdown/restart/logoff save and close the programs running in the background ")
            pyttsx3.speak("Warning : Before you proceed to shutdown or restart or logoffsave and close the programs running in the background ")
            print("Do you wish to continue?(y/n)")
            pyttsx3.speak("Do you wish to continue?")
            p=input()
            if any(word in p for word in acc ):
                os.system("shutdown -l")
            elif any(word in p for word in ng) :
                print("Oops I didn't get you try something else ")
                pyttsx3.speak("Oops I didn't get you try something else") 
               
            
            
        elif any(word in a for word in lis15 ) and (any(word in a for word in lis14 )and not(any(word in a for word in ng ))):
            print("Warning : Before you proceed to shutdown/restart/logoff save and close the programs running in the background ")
            pyttsx3.speak("Warning : Before you proceed to shutdown or restart or logoffsave and close the programs running in the background ")
            print("Do you wish to continue?(y/n)")
            pyttsx3.speak("Do you wish to continue?")
            p=input()
            if any(word in p for word in acc ):
                os.system("shutdown -r")
            elif any(word in p for word in ng) :
                print("Oops I didn't get you try something else ")
                pyttsx3.speak("Oops I didn't get you try something else")
        
        elif any(word in a for word in conv ):
            print("I am fine ")
            pyttsx3.speak("I am fine")
            print("How are you? ")
            pyttsx3.speak("How are you")
            greet=input()
            if any(word in  greet for word in conv ) and not(any(word in a for word in ng )):
                print("Nice to hear from you...")
                pyttsx3.speak("Nice to hear from you")
            
            
                
        elif any(word in a for word in quit ):
                print("Good Bye See you next time " + name + "....")
                pyttsx3.speak("Good Bye See you next time " + name)
                exit(1)
                break
        else:
            print("Oops I didn't get you try something else ")
            pyttsx3.speak("Oops I didn't get you try something else")   

       


