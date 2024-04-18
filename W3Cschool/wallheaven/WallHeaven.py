# -*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
    target = 'https://unsplash.com/'
    target="https://wallhaven.cc/w/6do9zx";
    req = requests.get(url=target)
    print(req.text)
    headers = {'authorization':'your Client-ID'}
    req = requests.get(url=target, headers=headers, verify=False)
    #https://w.wallhaven.cc/full/6d/wallhaven-6do9zx.png
   #<img id="wallpaper" src="https://w.wallhaven.cc/full/6d/wallhaven-6do9zx.png"
# alt="General 4829x3622 Louis Coyle digital art landscape nature birds sunset Sun artwork summer i
# llustration palm trees leaves water reflection" data-wallpaper-id="6do9zx" data-wallpaper-w
# idth="4829" data-wallpaper-height="3622" crossorigin="anonymous" class="fill-horizontal">
