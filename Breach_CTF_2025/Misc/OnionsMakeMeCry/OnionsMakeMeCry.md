# Onions Make Me Cry

Nos dan una captura de red entre las que se incluye trafico de la red Tor, debemos  identificar las direcciones IP de los nodos de entrada (Guard Nodes) de Tor 

Un Tor Guard Node es el primer nodo en el circuito Tor. Se comunica mediante TLS, generalmente en el puerto 443 o 9001

Para identificar una conexion a uno de estos nodos hay informacion en este sitio: https://osqa-ask.wireshark.org/questions/13590/tor-detection/

![2025-04-06-215645_714x140_scrot](https://github.com/user-attachments/assets/d35aff17-a661-4fed-9e79-b8c90b8bb3aa)

El SNI es una extensión del protocolo TLS que permite al cliente (navegador, app, etc.) indicar qué servidor web está intentando contactar antes de establecer la conexión cifrada. Tor modifica/oculta el SNI por diseño para proteger el anonimato

Con el comando: `tshark -r onion.pcapng -Y "ssl.handshake.type == 1 and ip.src == 10.53.6.158 and not quic` podemos filtrar los `Client Hello` que fueron enviados por la IP del creador del reto y que no usan el protocolo QUIC
```
> tshark -r onion.pcapng -Y "ssl.handshake.type == 1 and ip.src == 10.53.6.158 and not quic"
  307 15.619753166  10.53.6.158 → 142.250.67.238 TLSv1.2 1176 Client Hello (SNI=www.youtube-nocookie.com)
  322 15.625476337  10.53.6.158 → 13.107.42.14 TLSv1.2 593 Client Hello (SNI=linkedin.com)
  327 15.626826285  10.53.6.158 → 13.107.42.14 TLSv1.2 593 Client Hello (SNI=linkedin.com)
  439 16.307348747  10.53.6.158 → 151.101.155.42 TLSv1.2 597 Client Hello (SNI=static.licdn.com)
  969 16.414622497  10.53.6.158 → 151.101.155.42 TLSv1.2 602 Client Hello (SNI=platform.linkedin.com)
  988 16.415837730  10.53.6.158 → 151.101.155.42 TLSv1.2 602 Client Hello (SNI=platform.linkedin.com)
 1123 16.488122097  10.53.6.158 → 142.251.175.84 TLSv1.2 600 Client Hello (SNI=accounts.google.com)
 1129 16.488683847  10.53.6.158 → 142.251.175.84 TLSv1.2 600 Client Hello (SNI=accounts.google.com)
 1131 16.489045360  10.53.6.158 → 142.251.175.84 TLSv1.2 600 Client Hello (SNI=accounts.google.com)
 1158 16.523921148  10.53.6.158 → 144.2.9.1    TLSv1.2 598 Client Hello (SNI=ponf.linkedin.com)
 1160 16.524241643  10.53.6.158 → 144.2.9.1    TLSv1.2 598 Client Hello (SNI=ponf.linkedin.com)
 1335 16.760537617  10.53.6.158 → 142.250.192.40 TLSv1.2 605 Client Hello (SNI=www.googletagmanager.com)
 1337 16.760863652  10.53.6.158 → 3.108.133.69 TLSv1.2 595 Client Hello (SNI=dpm.demdex.net)
 1339 16.761155823  10.53.6.158 → 3.108.133.69 TLSv1.2 595 Client Hello (SNI=dpm.demdex.net)
 1489 16.800823515  10.53.6.158 → 65.1.46.199  TLSv1.2 596 Client Hello (SNI=lnkd.demdex.net)
 1491 16.801113893  10.53.6.158 → 65.1.46.199  TLSv1.2 596 Client Hello (SNI=lnkd.demdex.net)
 1493 16.801398150  10.53.6.158 → 65.1.46.199  TLSv1.2 596 Client Hello (SNI=lnkd.demdex.net)
 1495 16.801634486  10.53.6.158 → 65.1.46.199  TLSv1.2 596 Client Hello (SNI=lnkd.demdex.net)
 1789 17.063250705  10.53.6.158 → 144.2.9.1    TLSv1.2 735 Client Hello (SNI=ponf.linkedin.com)
 1816 17.390221030  10.53.6.158 → 23.193.114.49 TLSv1.2 588 Client Hello (SNI=trkn.us)
 1818 17.390433381  10.53.6.158 → 23.193.114.49 TLSv1.2 588 Client Hello (SNI=trkn.us)
 1820 17.390664177  10.53.6.158 → 23.193.114.49 TLSv1.2 588 Client Hello (SNI=trkn.us)
 1822 17.390882649  10.53.6.158 → 23.193.114.49 TLSv1.2 588 Client Hello (SNI=trkn.us)
 2048 22.556987216  10.53.6.158 → 87.236.194.23 TLSv1 583 Client Hello (SNI=www.5sft4ga3iyp6f.com)
 2049 22.557098335  10.53.6.158 → 185.241.208.163 TLSv1 583 Client Hello (SNI=www.bibu4eo.com)
 2266 43.402919936  10.53.6.158 → 185.241.208.163 TLSv1 583 Client Hello (SNI=www.kv7tbcmwxn457j5nfrfyllzg.com)
 2267 43.403049470  10.53.6.158 → 87.236.194.23 TLSv1 583 Client Hello (SNI=www.tmhy.com)
 2589 59.864755284  10.53.6.158 → 142.250.67.225 TLSv1.2 1177 Client Hello (SNI=lh3.googleusercontent.com)
 2721 60.034685137  10.53.6.158 → 142.251.42.66 TLSv1.2 605 Client Hello (SNI=www.googleadservices.com)
 2753 60.049820637  10.53.6.158 → 142.250.185.195 TLSv1.2 594 Client Hello (SNI=id.google.com)
 2755 60.050448101  10.53.6.158 → 142.250.185.195 TLSv1.2 594 Client Hello (SNI=id.google.com)
 2891 60.121179018  10.53.6.158 → 142.251.42.35 TLSv1.2 1167 Client Hello (SNI=www.gstatic.com)
 3354 60.694429641  10.53.6.158 → 142.250.183.14 TLSv1.2 607 Client Hello (SNI=encrypted-tbn0.gstatic.com)
 3364 60.696925420  10.53.6.158 → 142.250.183.14 TLSv1.2 607 Client Hello (SNI=encrypted-tbn0.gstatic.com)
 3420 60.756339452  10.53.6.158 → 142.250.183.14 TLSv1.2 607 Client Hello (SNI=encrypted-tbn0.gstatic.com)
 3422 60.756716093  10.53.6.158 → 142.250.183.14 TLSv1.2 607 Client Hello (SNI=encrypted-tbn0.gstatic.com)
 3428 60.757599199  10.53.6.158 → 142.250.67.206 TLSv1.2 607 Client Hello (SNI=encrypted-tbn2.gstatic.com)
 3573 60.811799473  10.53.6.158 → 142.250.67.238 TLSv1.2 607 Client Hello (SNI=encrypted-tbn1.gstatic.com)
 3575 60.812253169  10.53.6.158 → 142.250.67.238 TLSv1.2 607 Client Hello (SNI=encrypted-tbn1.gstatic.com)
 3577 60.812635170  10.53.6.158 → 142.250.67.238 TLSv1.2 607 Client Hello (SNI=encrypted-tbn1.gstatic.com)
 3579 60.812947780  10.53.6.158 → 142.250.67.238 TLSv1.2 607 Client Hello (SNI=encrypted-tbn1.gstatic.com)
 3891 61.044666294  10.53.6.158 → 10.99.99.158 TLSv1.2 598 Client Hello (SNI=moodle.iitb.ac.in)
 3913 61.066049303  10.53.6.158 → 10.99.99.158 TLSv1.2 1169 Client Hello (SNI=moodle.iitb.ac.in)
 3989 61.556425592  10.53.6.158 → 10.99.99.158 TLSv1.2 1169 Client Hello (SNI=moodle.iitb.ac.in)
 4110 64.856390463  10.53.6.158 → 162.159.153.4 TLSv1.2 591 Client Hello (SNI=medium.com)
 4112 64.856706269  10.53.6.158 → 162.159.153.4 TLSv1.2 591 Client Hello (SNI=medium.com)
 4116 64.857609192  10.53.6.158 → 162.159.153.4 TLSv1.2 591 Client Hello (SNI=medium.com)
 4183 64.894357915  10.53.6.158 → 162.159.152.4 TLSv1.2 597 Client Hello (SNI=glyph.medium.com)
 4325 65.636623172  10.53.6.158 → 162.159.152.4 TLSv1.2 602 Client Hello (SNI=cdn-client.medium.com)
 4332 65.638297692  10.53.6.158 → 104.16.79.73 TLSv1.2 610 Client Hello (SNI=static.cloudflareinsights.com)
 4375 65.653865588  10.53.6.158 → 162.159.152.4 TLSv1.2 596 Client Hello (SNI=miro.medium.com)
 4772 66.088768060  10.53.6.158 → 142.250.192.40 TLSv1.2 605 Client Hello (SNI=www.googletagmanager.com)
 4800 66.090901275  10.53.6.158 → 142.250.192.40 TLSv1.2 605 Client Hello (SNI=www.googletagmanager.com)
 4834 66.126769066  10.53.6.158 → 142.250.183.4 TLSv1.2 595 Client Hello (SNI=www.google.com)
 4990 66.339711493  10.53.6.158 → 142.251.42.35 TLSv1.2 596 Client Hello (SNI=www.gstatic.com)
 4997 66.341524504  10.53.6.158 → 142.251.42.35 TLSv1.2 596 Client Hello (SNI=www.gstatic.com)
 5088 66.405901579  10.53.6.158 → 142.251.42.35 TLSv1.2 1167 Client Hello (SNI=www.gstatic.com)
 5251 66.583800611  10.53.6.158 → 18.155.49.57 TLSv1.2 594 Client Hello (SNI=cdn.sprig.com)
 5281 66.591198471  10.53.6.158 → 142.251.42.35 TLSv1.2 596 Client Hello (SNI=www.gstatic.com)
 5283 66.591439396  10.53.6.158 → 142.251.42.35 TLSv1.2 596 Client Hello (SNI=www.gstatic.com)
 5486 67.320590911  10.53.6.158 → 216.239.38.178 TLSv1.2 605 Client Hello (SNI=www.google-analytics.com)
 5488 67.320872803  10.53.6.158 → 216.239.38.178 TLSv1.2 605 Client Hello (SNI=www.google-analytics.com)
 5696 68.054737920  10.53.6.158 → 18.155.49.70 TLSv1.2 594 Client Hello (SNI=cdn.branch.io)
 5736 68.162355957  10.53.6.158 → 18.155.49.127 TLSv1.2 589 Client Hello (SNI=app.link)
 5738 68.162606610  10.53.6.158 → 18.155.49.127 TLSv1.2 589 Client Hello (SNI=app.link)
 5900 68.560606312  10.53.6.158 → 184.72.105.205 TLSv1.2 594 Client Hello (SNI=api.sprig.com)
 5910 68.568334355  10.53.6.158 → 184.72.105.205 TLSv1.2 594 Client Hello (SNI=api.sprig.com)
 5923 68.590350968  10.53.6.158 → 54.230.27.45 TLSv1.2 595 Client Hello (SNI=api2.branch.io)
 5925 68.590880878  10.53.6.158 → 54.230.27.45 TLSv1.2 595 Client Hello (SNI=api2.branch.io)
 6323 73.652580176  10.53.6.158 → 138.197.58.222 TLSv1.2 599 Client Hello (SNI=tlwomenctf.ctfd.io)
 6366 73.696302696  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6369 73.696624603  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6371 73.696845420  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6377 73.697197664  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6381 73.697437978  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6383 73.697641892  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6386 73.697993676  10.53.6.158 → 18.155.33.23 TLSv1.2 598 Client Hello (SNI=cdn.cloud.ctfd.io)
 6483 73.752325745  10.53.6.158 → 138.197.58.222 TLSv1.2 599 Client Hello (SNI=tlwomenctf.ctfd.io)
 6491 73.753880338  10.53.6.158 → 18.155.33.5  TLSv1.2 604 Client Hello (SNI=beacon-v2.helpscout.net)
 6496 73.755445261  10.53.6.158 → 18.155.33.5  TLSv1.2 604 Client Hello (SNI=beacon-v2.helpscout.net)
 6599 73.860337682  10.53.6.158 → 108.157.244.183 TLSv1.2 610 Client Hello (SNI=d3hb14vkzrxvla.cloudfront.net)
 6601 73.860605066  10.53.6.158 → 108.157.244.183 TLSv1.2 610 Client Hello (SNI=d3hb14vkzrxvla.cloudfront.net)
 6605 73.861461823  10.53.6.158 → 108.157.244.183 TLSv1.2 610 Client Hello (SNI=d3hb14vkzrxvla.cloudfront.net)
 6816 79.449320220  10.53.6.158 → 212.227.74.176 TLSv1 583 Client Hello (SNI=www.dqw5uhwsvjj22y3dnlusm7i2.com)
 6819 79.449575341  10.53.6.158 → 95.216.33.30 TLSv1 583 Client Hello (SNI=www.eyv4rjxbur5bb6n.com)
 6833 79.455676824  10.53.6.158 → 185.225.114.53 TLSv1 583 Client Hello (SNI=www.hs2gbhzhbtjxbglbxyspx2p6.com)
```

Ordenamos los nodos por IP y enviamos la flag:

`Breach{87.236.194.23 95.216.33.30 108.157.244.183 185.225.114.53 185.241.208.163 212.227.74.176}`
