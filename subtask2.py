def list_ifname_ip():
  t = dict()
  
  fin = open("running-config.cfg","r")
  for word in fin:
    if "no" not in word:
      word = word.strip()
      if "ip address" in word:
        tmp = word.split()
        for i in tmp:
          i = i.split(".")
          for n, p in enumerate(i):
            if p == "172" or p=="192": 
              i[n]= "10"
              k = ".".join(i)
              print(k)

(list_ifname_ip())
fout = open("newfile","a")
fout.write("k")
