
https://www.rtl-sdr.com/blind-reverse-engineering-wireless-protocol/

https://www.rtl-sdr.com/reverse-engineering-a-vintage-wireless-keypad-with-an-rtl-sdr/

https://mavicpilots.com/threads/wi-fi-vs-occusync-2-0.87616/#:~:text=Yes%2C%20Ocusync%20wins%20by%20far,range%20in%20the%20first%20place.

https://thedroneadventure.com/drone-talk-ocusync-vs-lightbridge-vs-wifi-which-is-the-best-connection

https://mavicpilots.com/threads/occusync-and-sdr.82743/

https://swling.com/blog/tag/sdr-for-beginners/

File uploading:

```sh
┌─[root@parrot]─[/home/sshad0w]
└──╼ #curl -i -X POST -H "Content-Type: multipart/form-data" -F file=@/home/sshad0w/Documents/drone-pwn/first-scans/First_Wireshark_capture.pcapng https://store4.gofile.io/uploadFile

HTTP/2 200 
access-control-allow-origin: *
content-type: application/json; charset=utf-8
date: Wed, 10 Nov 2021 17:58:57 GMT
etag: W/"241-BTUtVdYkF61bmP73IYxyqLo1cQI"
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-powered-by: Express
x-xss-protection: 1; mode=block
content-length: 577

{"status":"ok","data":{"guestToken":"sPXz4smU49929MgumOxbptkjYRR1hlAQ","downloadPage":"https://gofile.io/d/A06HBU","code":"A06HBU","parentFolder":"3d419916-2961-4d05-955d-96d71d00db37","fileId":"0fc12cb9-4a2d-490a-986a-a8d8ac7f91db","fileName":"First_Wireshark_capture.pcapng","md5":"9ae9177fac010a5be8c7eaf9d25f5b73","directLink":"https://store4.gofile.io/download/0fc12cb9-4a2d-490a-986a-a8d8ac7f91db/First_Wireshark_capture.pcapng","info":"Direct links only work if your account is a donor account. Standard accounts will have their links redirected to the download page."}}
```
