import os
import time

links = {
    "2Dimensions": "https://2Dimensions.com/a/{}",
    "7Cups": "https://www.7cups.com/@{}",
    "9GAG": "https://www.9gag.com/u/{}",
    "About.me": "https://about.me/{}",
    "Academia.edu": "https://independent.academia.edu/{}",
    "Alik.cz": "https://www.alik.cz/u/{}",
    "Apple Discussions": "https://discussions.apple.com/profile/{}",
    "Asciinema": "https://asciinema.org/~{}",
    "Ask Fedora": "https://ask.fedoraproject.org/u/{}",
    "AskFM": "https://ask.fm/{}",
    "Audiojungle": "https://audiojungle.net/user/{}",
    "BLIP.fm": "https://blip.fm/{}",
    "Bandcamp": "https://www.bandcamp.com/{}",
    "Bazar.cz": "https://www.bazar.cz/{}/",
    "Behance": "https://www.behance.net/{}",
    "BitBucket": "https://bitbucket.org/{}/",
    "Blogger": "https://{}.blogspot.com",
    "Bookcrossing": "https://www.bookcrossing.com/mybookshelf/{}/",
    "BuyMeACoffee": "https://buymeacoff.ee/{}",
    "BuzzFeed": "https://buzzfeed.com/{}",
    "CNET": "https://www.cnet.com/profiles/{}/",
    "Carbonmade": "https://{}.carbonmade.com",
    "Career.habr": "https://career.habr.com/{}",
    "Championat": "https://www.championat.com/user/{}",
    "Chatujme.cz": "https://profil.chatujme.cz/{}",
    "Chess": "https://www.chess.com/member/{}",
    "CloudflareCommunity": "https://community.cloudflare.com/u/{}",
    "Codecademy": "https://www.codecademy.com/profiles/{}",
    "Codepen": "https://codepen.io/{}",
    "Codewars": "https://www.codewars.com/users/{}",
    "ColourLovers": "https://www.colourlovers.com/lover/{}",
    "Contently": "https://{}.contently.com/",
    "Coroflot": "https://www.coroflot.com/{}",
    "Crevado": "https://{}.crevado.com",
    "DEV Community": "https://dev.to/{}",
    "DailyMotion": "https://www.dailymotion.com/{}",
    "Designspiration": "https://www.designspiration.net/{}/",
    "DeviantART": "https://{}.deviantart.com",
    "Discogs": "https://www.discogs.com/user/{}",
    "Discuss.Elastic.co": "https://discuss.elastic.co/u/{}",
    "Disqus": "https://disqus.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Ello": "https://ello.co/{}",
    "Etsy": "https://www.etsy.com/shop/{}",
    "EyeEm": "https://www.eyeem.com/u/{}",
    "F3.cool": "https://f3.cool/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "Facebook Groups": "https://www.facebook.com/groups/{}",
    "Fandom": "https://www.fandom.com/u/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Flipboard": "https://flipboard.com/@{}",
    "Football": "https://www.rusfootball.info/user/{}/",
    "FortniteTracker": "https://fortnitetracker.com/profile/all/{}",
    "Freelance.habr": "https://freelance.habr.com/freelancers/{}",
    "Freelancer.com": "https://www.freelancer.com/u/{}",
    "Freesound": "https://freesound.org/people/{}/",
    "Gamespot": "https://www.gamespot.com/profile/{}/",
    "GetMyUni": "https://www.getmyuni.com/user/{}",
    "Giphy": "https://giphy.com/{}",
    "GitHub": "https://www.github.com/{}",
    "GitHub Support Community": "https://github.community/u/{}/summary",
    "GitLab": "https://gitlab.com/{}",
    "Gitee": "https://gitee.com/{}",
    "GoodReads": "https://www.goodreads.com/{}",
    "Gravatar": "http://en.gravatar.com/{}",
    "Gumroad": "https://www.gumroad.com/{}",
    "GunsAndAmmo": "https://forums.gunsandammo.com/profile/{}",
    "GuruShots": "https://gurushots.com/{}/photos",
    "HackTheBox": "https://forum.hackthebox.eu/profile/{}",
    "Hackaday": "https://hackaday.io/{}",
    "HackerOne": "https://hackerone.com/{}",
    "Houzz": "https://houzz.com/user/{}",
    "HubPages": "https://hubpages.com/@{}",
    "ICQ": "https://icq.im/{}",
    "IFTTT": "https://www.ifttt.com/p/{}",
    "ImgUp.cz": "https://imgup.cz/{}",
    "Instagram": "https://instagram.com/{}",
    "Instructables": "https://www.instructables.com/member/{}",
    "Issuu": "https://issuu.com/{}",
    "Itch.io": "https://{}.itch.io/",
    "Jimdo": "https://{}.jimdosite.com",
    "Kaggle": "https://www.kaggle.com/{}",
    "Keybase": "https://keybase.io/{}",
    "Kik": "https://kik.me/{}",
    "Kongregate": "https://www.kongregate.com/accounts/{}",
    "LOR": "https://www.linux.org.ru/people/{}/profile",
    "Launchpad": "https://launchpad.net/~{}",
    "LeetCode": "https://leetcode.com/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Likee": "https://likee.com/@{}",
    "LiveJournal": "https://{}.livejournal.com",
    "Lobsters": "https://lobste.rs/u/{}",
    "Medium": "https://medium.com/@{}",
    "Memrise": "https://www.memrise.com/user/{}/",
    "Munzee": "https://www.munzee.com/m/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "MyMiniFactory": "https://www.myminifactory.com/users/{}",
    "Myspace": "https://myspace.com/{}",
    "NameMC (Minecraft.net skins)": "https://namemc.com/profile/{}",
    "Naver": "https://blog.naver.com/{}",
    "Newgrounds": "https://{}.newgrounds.com",
    "NotABug.org": "https://notabug.org/{}",
    "OK": "https://ok.ru/{}",
    "OpenStreetMap": "https://www.openstreetmap.org/user/{}",
    "Opensource": "https://opensource.com/users/{}",
    "PCPartPicker": "https://pcpartpicker.com/user/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Periscope": "https://www.periscope.tv/{}/",
    "Pinkbike": "https://www.pinkbike.com/u/{}/",
    "PlayStore": "https://play.google.com/store/apps/developer?id={}",
    "Plug.DJ": "https://plug.dj/@/{}",
    "Pokémon Showdown": "https://pokemonshowdown.com/users/{}",
    "Polygon": "https://www.polygon.com/users/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "PromoDJ": "http://promodj.com/{}",
    "PyPi": "https://pypi.org/user/{}",
    "Quizlet": "https://quizlet.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Raidforums": "https://raidforums.com/User-{}",
    "Rajce.net": "https://{}.rajce.idnes.cz/",
    "RapidAPI": "https://rapidapi.com/users/{}",
    "Rate Your Music": "https://rateyourmusic.com/~{}",
    "Redbubble": "https://www.redbubble.com/people/{}",
    "Repl.it": "https://repl.it/@{}",
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "RubyGems": "https://rubygems.org/profiles/{}",
    "Sbazar.cz": "https://www.sbazar.cz/{}",
    "Scratch": "https://scratch.mit.edu/users/{}",
    "Scribd": "https://www.scribd.com/{}",
    "ShitpostBot5000": "https://www.shitpostbot.com/user/{}",
    "Signal": "https://community.signalusers.org/u/{}",
    "Slack": "https://{}.slack.com",
    "Slashdot": "https://slashdot.org/~{}",
    "SlideShare": "https://slideshare.net/{}",
    "Snapchat": "https://snapchat.com/add/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "SourceForge": "https://sourceforge.net/u/{}",
    "Speedrun.com": "https://speedrun.com/user/{}",
    "Splits.io": "https://splits.io/users/{}",
    "Sporcle": "https://www.sporcle.com/user/{}/people",
    "SportsRU": "https://www.sports.ru/profile/{}/",
    "Spotify": "https://open.spotify.com/user/{}",
    "Star Citizen": "https://robertsspaceindustries.com/citizens/{}",
    "SublimeForum": "https://forum.sublimetext.com/u/{}",
    "Tellonym.me": "https://tellonym.me/{}",
    "Test PyPi": "https://test.pypi.org/user/{}",
    "TikTok": "https://tiktok.com/@{}",
    "Ultimate-Guitar": "https://ultimate-guitar.com/u/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "VK": "https://vk.com/{}",
    "VSCO": "https://vsco.co/{}",
    "Venmo": "https://venmo.com/{}",
    "Vero": "https://vero.co/{}",
    "Vimeo": "https://vimeo.com/{}",
    "VirusTotal": "https://www.virustotal.com/ui/users/{}/trusted_users",
    "Warrior Forum": "https://www.warriorforum.com/members/{}.html",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "We Heart It": "https://weheartit.com/{}",
    "WebNode": "https://{}.webnode.cz/",
    "Whonix Forum": "https://forums.whonix.org/u/{}",
    "Wikipedia": "https://www.wikipedia.org/wiki/User:{}",
    "Windy": "https://community.windy.com/user/{}",
    "Wix": "https://{}.wix.com",
    "WordPressOrg": "https://profiles.wordpress.org/{}/",
    "Xbox Gamertag": "https://xboxgamertag.com/search/{}",
    "YouPic": "https://youpic.com/photographer/{}/",
    "YouTube": "https://www.youtube.com/{}",
    "Zhihu": "https://www.zhihu.com/people/{}",
    "Akniga": "https://akniga.org/profile/{}",
    "AllMyLinks": "https://allmylinks.com/{}",
    "AminoApp": "https://aminoapps.com/u/{}",
    "authorSTREAM": "http://www.authorstream.com/{}/",
    "babyRU": "https://www.baby.ru/u/{}/",
    "chaos.social": "https://chaos.social/@{}",
    "CouchSurfing": "https://www.couchsurfing.com/people/{}",
    "d3RU": "https://d3.ru/user/{}/posts",
    "Dailykos": "https://www.dailykos.com/user/{}",
    "datingRU": "http://dating.ru/{}",
    "Drive2": "https://www.drive2.ru/users/{}",
    "eGPU": "https://egpu.io/forums/profile/{}/",
    "Eintracht": "https://community.eintracht.de/fans/{}",
    "Fixya": "https://www.fixya.com/users/{}",
    "FL": "https://www.fl.ru/users/{}",
    "GeoCaching": "https://www.geocaching.com/p/default.aspx?u={}",
    "Habr": "https://habr.com/ru/users/{}",
    "Hackster": "https://www.hackster.io/{}",
    "irecommend": "https://irecommend.ru/users/{}",
    "Jeuxvideo": "http://www.jeuxvideo.com/profil/{}?mode=infos",
    "Kofi": "https://ko-fi.com/{}",
    "kwork": "https://kwork.ru/user/{}",
    "Last.fm": "https://last.fm/user/{}",
    "LeaseHackr": "https://forum.leasehackr.com/u/{}/summary/",
    "LiveLib": "https://www.livelib.ru/reader/{}",
    "mastodon.cloud": "https://mastodon.cloud/@{}",
    "mastodon.social": "https://mastodon.social/@{}",
    "Mercadolivre": "https://www.mercadolivre.com.br/perfil/{}",
    "Moikrug": "https://moikrug.ru/{}",
    "Mstdn.io": "https://mstdn.io/@{}",
    "Nairaland.com": "https://www.nairaland.com/{}",
    "nnRU": "https://{}.www.nn.ru/",
    "Note": "https://note.com/{}",
    "npm": "https://www.npmjs.com/~{}",
    "Opennet": "https://www.opennet.ru/~{}",
    "Osu!": "https://osu.ppy.sh/users/{}",
    "satsisRU": "https://satsis.info/user/{}",
    "social.tchncs.de": "https://social.tchncs.de/@{}",
    "Svidbook": "https://www.svidbook.ru/user/{}",
    "uid": "http://uid.me/{}"
}

def moduleimport():
    print('Installing libraries...')
    os.system('pip install colorama phonenumbers requests bs4')

try:
    import json
    from colorama import init, Fore, Back, Style
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    pass
    moduleimport()

author = 'memb3r'
version = 'v1.0.1'
byauthor = 'by memb3r'
authorurl = 'https://github.com/memb3r/'

def banner():
    print(f'{Fore.RED} _____     _       _____ _____ _____ __    ')
    print(f'|     |___| |_ ___|_   _|     |     |  |   ')
    print(f'|  |  |   |  _| . | | | |  {Fore.WHITE}|{Fore.RED}  |  {Fore.WHITE}|{Fore.RED}  |  |__ ')
    print(f'|_____|_|_|_| |___| |_| |_____|_____|_____| {Back.GREEN}{Fore.BLACK}{version}{Style.RESET_ALL}\n')

def start():
    banner()
    print(f'{Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Hi! Welcome to {Fore.RED}OntoTOOL{Fore.WHITE} - proffesional OSINT tool. There you can find information from Open Sources.')
    print(f'{Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Author: {Fore.RED}{authorurl}{Fore.WHITE}')
    print(f'{Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Type {Fore.RED}"help"{Fore.WHITE} to see all commands.\n')

def choose():
    while True:
        answer = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}] {Fore.WHITE}Input answer {Fore.RED}here{Fore.WHITE}: ')
        if (answer == ''):
            print(f'{Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}This answer is not exist!')
        elif (answer == 'help'):
            help()
        elif (answer == 'phone'):
            phonee()
        elif (answer == 'email'):
            emaill()
        elif (answer == 'user'):
            usernamm()
        elif (answer == 'ip'):
            iplook()
        else:
            print(f'{Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Answer {Fore.WHITE}"{answer}"{Fore.RED} is not exist!')

def help():
    print(f'{Fore.RED}[{Fore.CYAN}HELP{Fore.RED}]{Fore.WHITE}:')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}]       {Fore.WHITE}Author: {authorurl}')
    print(f'    {Fore.RED}[{Fore.CYAN}help{Fore.RED}]    {Fore.WHITE}Shows this help message.')
    print(f'    {Fore.RED}[{Fore.CYAN}phone{Fore.RED}]   {Fore.WHITE}Shows information about phone number.')
    print(f'    {Fore.RED}[{Fore.CYAN}ip{Fore.RED}]      {Fore.WHITE}Shows information about IP address.')
    print(f'    {Fore.RED}[{Fore.CYAN}user{Fore.RED}]    {Fore.WHITE}Shows information about username.')
    print(f'    {Fore.RED}[{Fore.CYAN}email{Fore.RED}]   {Fore.WHITE}Shows information about email.')

def phonee():
    print(f'{Fore.RED}[{Fore.CYAN}PHONE{Fore.RED}]{Fore.WHITE}:')
    phonenum = input(f'    {Fore.RED}[{Fore.CYAN}?{Fore.RED}] {Fore.WHITE}Input phone {Fore.RED}here{Fore.WHITE}: ')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching basic information...')
    if (phonenum == ''):
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}This is not a number!')
        return
    try:
        parsed_number = phonenumbers.parse(phonenum, None)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        region = phonenumbers.region_code_for_number(parsed_number)
        country = geocoder.description_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)
        carriers = carrier.name_for_number(parsed_number, "en")
    except phonenumbers.NumberParseException:
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}This is not a number!')
        return
    if (is_valid == False):
        print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Valid: {is_valid}')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Valid: {is_valid}')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country: {country}')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Timezone: {timezones}')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Operator: {carriers}')
    if (phonenum.startswith('+380')):
        formattednum = phonenum[1:]
        print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {formattednum} on ktozvonil.net...')
        tdurl = "https://ktozvonil.net/nomer/" + formattednum
        response = requests.get(tdurl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            count_comments = soup.find("div", itemprop="reviewBody")
            try:
                print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Review: {count_comments.text}')
            except AttributeError:
                print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Failed searching review about number on ktozvonil.net.')
        else:
            print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}')
        formattednum2 = phonenum[3:]
        print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {formattednum} on ktozvonit.com.ua...')
        print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Number on ktozvonit.com.ua: https://ktozvonit.com.ua/nomer/{formattednum2}')
    if (phonenum.startswith('+7')):
        formattednum = phonenum[2:]
        print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {formattednum} on netrubi.ru...')
        nturl = "https://netrubi.ru/nomer/" + formattednum
        response = requests.get(nturl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            revieww = soup.find("div", itemprop="description")
            try:
                print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Review: {revieww.text}')
            except AttributeError:
                print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Failed searching reviews count number on netrubi.ru.')
        else:
            print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}')
        print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {formattednum} on getscam.com...')
        formattednum2 = phonenum[1:]
        print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Number on getscam.com: https://getscam.com/{formattednum2}')
        print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {formattednum} on mysmsbox.ru...')
        msmurl = "https://mysmsbox.ru/phone-search/" + formattednum2
        response = requests.get(msmurl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            reviewww = soup.find("span", class_="color-grey")
            try:
                print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Review: {reviewww.text}')
            except AttributeError:
                print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Failed searching reviews count number on mysmsbox.ru.')
        else:
            print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}')
    formattednum3 = phonenum[1:]
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {phonenum} on Telegram...')
    teleurl = 'https://t.me/' + phonenum
    response = requests.get(teleurl)
    if response.status_code == 200:
        print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Telegram URL: {teleurl}')
    else:
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {phonenum} on Skype...')
    skypeurl = f'skype:{phonenum}?chat'
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Skype URL: {skypeurl}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {phonenum} on Viber...')
    viberurl = f'viber://chat?number={formattednum3}/'
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Viber URL: {viberurl}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching {phonenum} on WhatsApp...')
    whaurl = f'https://wa.clck.bar/{formattednum3}?text=%D0%92%D1%8B%20%D0%B7%D0%B2%D0%BE%D0%BD%D0%B8%D0%BB%D0%B8%20%D0%BC%D0%BD%D0%B5?'
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}WhatsApp URL: {whaurl}')

def emaill():
    print(f'{Fore.RED}[{Fore.CYAN}EMAIL{Fore.RED}]{Fore.WHITE}:')
    emailla = input(f'    {Fore.RED}[{Fore.CYAN}?{Fore.RED}] {Fore.WHITE}Input email {Fore.RED}here{Fore.WHITE}: ')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching leaks...')
    if (emailla == ''):
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}This is not an email!')
        return
    url = "https://leakcheck.net/api/public?key=49535f49545f5245414c4c595f4150495f4b4559&check=" + emailla
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get("success", False):
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Success: {data["success"]}')
            sources = data.get("sources", [])
            for source in sources:
                name = source.get("name")
                if name:
                    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Leak name: {name}')
        else:
            print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Leaks are not found!')
    else:
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching domain names...')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}URL: https://viewdns.info/reversewhois/?q={emailla}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching basic info...')
    eusername, edomain = emailla.split("@")
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Username: {eusername}')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Domain: {edomain}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching in BkRu...')
    mainurl = 'https://my.mail.ru/bk.ru/' + eusername
    response = requests.get(mainurl)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1_element = soup.find("h1", itemprop="name")
        if h1_element:
            text = h1_element.text
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Name: {text}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Profile URL: {mainurl}')
        else:
            print(f"    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Failed searching name.")
    else:
        print(f"    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}")
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching in InboxRu...')
    mainurl2 = 'https://my.mail.ru/inbox.ru/' + eusername
    response = requests.get(mainurl2)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1_element = soup.find("h1", itemprop="name")
        if h1_element:
            text = h1_element.text
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Name: {text}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Profile URL: {mainurl2}')
        else:
            print(f"    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Failed searching name.")
    else:
        print(f"    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}")

def usernamm():
    print(f'{Fore.RED}[{Fore.CYAN}USER{Fore.RED}]{Fore.WHITE}:')
    eusername = input(f'    {Fore.RED}[{Fore.CYAN}?{Fore.RED}] {Fore.WHITE}Input username {Fore.RED}here{Fore.WHITE}: ')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching leaks...')
    if (eusername == ''):
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}This is not a username!')
        return
    url = "https://leakcheck.net/api/public?key=49535f49545f5245414c4c595f4150495f4b4559&check=" + eusername
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get("success", False):
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Success: {data["success"]}')
            sources = data.get("sources", [])
            for source in sources:
                name = source.get("name")
                if name:
                    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Leak name: {name}')
        else:
            print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Leaks are not found!')
    else:
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status code: {response.status_code}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching all social media...')
    results = {}
    for networks, url_templates in links.items():
        full_urls = url_templates.format(eusername)
        response = requests.get(full_urls)
        if response.status_code == 200:
            time.sleep(0.1)
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}{networks}: {full_urls}')
            results[networks] = full_urls
    if not results:
        print(f"    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Social media accounts by {eusername} are not found.")

def iplook():
    print(f'{Fore.RED}[{Fore.CYAN}IP{Fore.RED}]{Fore.WHITE}:')
    ipinp = input(f'    {Fore.RED}[{Fore.CYAN}?{Fore.RED}] {Fore.WHITE}Input IP {Fore.RED}here{Fore.WHITE}: ')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching information...')
    if (ipinp == ''):
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}This is not an IP!')
        return
    request_url = f'https://ipapi.co/{ipinp}/json/'
    try:
        headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
        response = requests.get(request_url, headers=headers)
        if response.status_code == 200:
            ipvalues = response.json()
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}IP: {ipinp}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Network: {ipvalues["network"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Version: {ipvalues["version"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}City: {ipvalues["city"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Region: {ipvalues["region"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Region Code: {ipvalues["region_code"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country: {ipvalues["country"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Name: {ipvalues["country_name"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Code: {ipvalues["country_code"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Code ISO3: {ipvalues["country_code_iso3"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Capital: {ipvalues["country_capital"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country TLD: {ipvalues["country_tld"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Continent Code: {ipvalues["continent_code"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}In Europe: {ipvalues["in_eu"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Postal: {ipvalues["postal"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Latitude: {ipvalues["latitude"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Longitude: {ipvalues["longitude"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Timezone: {ipvalues["timezone"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}UTC Offset: {ipvalues["utc_offset"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Phone Code: {ipvalues["country_calling_code"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Currency: {ipvalues["currency"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Currency Name: {ipvalues["currency_name"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Languages: {ipvalues["languages"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Area: {ipvalues["country_area"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Country Population: {ipvalues["country_population"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}ASN: {ipvalues["asn"]}')
            print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Organisation: {ipvalues["org"]}')
        else:
            print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Response status: {response.status_code}. Failed to fetch data from ipapi.co.')
            return
    except requests.exceptions.SSLError as e:
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}SSL Error: {e}')
    except KeyError as e:
        print(f'    {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.RED}Failed to fetch {e}. Invalid IP.')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching information on whatismyipaddress.com...')
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}whatismyipaddress.com URL: https://whatismyipaddress.com/ip/{ipinp}')
    print(f'    {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.WHITE}Searching geolocation...')
    ipgeolocation = f'{ipvalues["latitude"]}+{ipvalues["longitude"]}'
    print(f'    {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.WHITE}Google Maps URL: https://www.google.com/maps/search/{ipgeolocation}')

if __name__ == '__main__':
    start()
    choose()
