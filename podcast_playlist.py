import feedparser
from datetime import datetime, timezone

FEEDS = [
    ("How to Invent a Country", "https://podcasts.files.bbci.co.uk/p0683ms3.rss"),
    ("In Our Time History", "https://podcasts.files.bbci.co.uk/p01dh5yg.rss"),
    ("In Our Time", "https://podcasts.files.bbci.co.uk/b006qykl.rss"),
    ("Sideways", "https://podcasts.files.bbci.co.uk/m000s2kt.rss"),
    ("All in the Mind", "https://podcasts.files.bbci.co.uk/b006qxx9.rss"),
    ("The History Hour", "https://podcasts.files.bbci.co.uk/p016tmt2.rss"),
    ("Desert Island Discs", "https://podcasts.files.bbci.co.uk/b006qnmr.rss"),
    ("Czech Easily Slow & Easy", "https://feeds.libsyn.com/514073/rss"),
    ("slowczech", "https://slowczech.com/feed/podcast/"),
    ("Nutrition Facts Dr Greger", "https://nutritionfacts.org/feed/podcast/"),
    ("A Small Voice", "https://asmallvoicepod.simplecast.com/rss"),
    ("Three Bean Salad", "https://feeds.captivate.fm/threebeansalad"),
    ("Very Bad Wizards", "https://feeds.simplecast.com/verybadwizards"),
    ("Revisionist History", "https://feeds.simplecast.com/revisionisthistory"),
    ("You Must Remember This", "https://feeds.simplecast.com/youmustrememberthis"),
    ("The Daily NYT", "https://feeds.simplecast.com/54nAGcIl"),
    ("Hard Fork", "https://feeds.simplecast.com/hardfork_nyt"),
    ("Ezra Klein Show", "https://feeds.simplecast.com/ezra_klein_show"),
    ("Search Engine", "https://feeds.simplecast.com/searchengine"),
    ("99% Invisible", "https://feeds.simplecast.com/99invisible"),
    ("Heavyweight", "https://feeds.simplecast.com/heavyweight"),
    ("This American Life", "https://feed.thisamericanlife.org/talpodcast"),
    ("The Rewatchables", "https://feeds.megaphone.fm/therewatchables"),
    ("The Vergecast", "https://feeds.megaphone.fm/vergecast"),
    ("Version History", "https://feeds.megaphone.fm/VMP9592065957"),
    ("Totally Football Show", "https://feeds.acast.com/public/shows/the-totally-football-show-with-james-richardson"),
    ("Elis James and John Robins", "https://feeds.acast.com/public/shows/elis-james-and-john-robins"),
    ("Adam Buxton Podcast", "https://feeds.acast.com/public/shows/adam-buxton-podcast"),
    ("The Rest Is Football", "https://feeds.acast.com/public/shows/the-rest-is-football"),
    ("Josh Widdicombe Archive", "https://feeds.acast.com/public/shows/josh-widdicombes-archive-of-pop-culture"),
    ("The Athletic FC", "https://feeds.acast.com/public/shows/the-athletic-fc"),
    ("Arseblog Arsecast", "https://arseblog.com/feed/podcast/"),
    ("Football Weekly", "https://feeds.guardian.co.uk/football-weekly-podcast/rss"),
    ("Radiolab", "https://feeds.wnyc.org/radiolab"),
    ("New Yorker Radio Hour", "https://feeds.wnyc.org/newyorkerradiohour"),
    ("Making Sense Sam Harris", "https://feeds.samharris.org/makingsense"),
    ("The Interview NYT", "https://feeds.simplecast.com/the_interview_nyt"),
    ("Offline Jon Favreau", "https://feeds.simplecast.com/offline_jon_favreau"),
    ("Fresh Air NPR", "https://feeds.npr.org/381444908/podcast.xml"),
    ("The Gray Area", "https://feeds.megaphone.fm/thegrayarea"),
    ("Totally Football Show", "https://feeds.acast.com/public/shows/the-totally-football-show-with-james-richardson"),
    ("The Ezra Klein Show", "https://feeds.simplecast.com/ezra_klein_show"),
    ("Seriously BBC R4", "https://podcasts.files.bbci.co.uk/b01mk3f8.rss"),
    ("Ear Hustle", "https://feeds.simplecast.com/earhustle"),
    ("Red Scare", "https://feeds.simplecast.com/redscare"),
    ("Kermode and Mayos Take", "https://podcasts.files.bbci.co.uk/p02pc9pj.rss"),
    ("The Rest Is Football", "https://feeds.acast.com/public/shows/the-rest-is-football"),
    ("Richard Herring RHLSTP", "https://feeds.acast.com/public/shows/rhlstp"),
    ("Generation Why", "https://feeds.simplecast.com/generationwhy"),
    ("No Stupid Questions", "https://feeds.simplecast.com/nostupidquestions"),
    ("Blank Check", "https://feeds.simplecast.com/blankcheck"),
    ("Ed Gamble Matthew Crosby Radio X", "https://feeds.acast.com/public/shows/ed-gamble-and-matthew-crosby-on-radio-x"),
    ("The Complete Guide to Everything", "https://feeds.simplecast.com/completeguide"),
    ("The Socially Distant Sports Bar", "https://feeds.acast.com/public/shows/the-socially-distant-sports-bar"),
    ("Thinking Allowed BBC", "https://podcasts.files.bbci.co.uk/b006qy05.rss"),
    ("Evil Genius Russell Kane", "https://podcasts.files.bbci.co.uk/p0fcrs8m.rss"),
    ("Panic World", "https://feeds.simplecast.com/panicworld"),
    ("Dear Art Producer", "https://feeds.simplecast.com/dearartproducer"),
    ("Sidedoor Smithsonian", "https://feeds.simplecast.com/sidedoor"),
    ("Soho Bites", "https://feeds.acast.com/public/shows/soho-bites-podcast"),
    ("Fotbal fokus", "https://feeds.simplecast.com/fotbalfokus"),
    ("Prague Talk", "https://feeds.simplecast.com/praguetalk"),
    ("Endless Thread", "https://feeds.wbur.org/endless-thread/podcast"),
    ("Middlebrow", "https://feeds.simplecast.com/middlebrow"),
    ("Taste of Prague", "https://feeds.simplecast.com/tasteofprague"),
    ("Moving Offline Podcast", "https://feeds.simplecast.com/movingoffline"),
    ("What's Contemporary Now", "https://feeds.megaphone.fm/whatscontemporary"),
    ("The Messy Truth Photography", "https://feeds.simplecast.com/themessytruth"),
    ("Magic Hour Photography", "https://feeds.simplecast.com/magichour"),
    ("The Exposed Negative", "https://feeds.simplecast.com/theexposednegative"),
    ("VICE Culture Club", "https://feeds.acast.com/public/shows/vice-culture-club"),
    ("SOLVED Mark Manson", "https://feeds.simplecast.com/solvedmarkmanson"),
    ("Personality Hacker", "https://feeds.simplecast.com/personalityhacker"),
    ("Revolution Now Peter Joseph", "https://feeds.simplecast.com/revolutionnow"),
    ("Over the Road", "https://feeds.simplecast.com/overtheroad"),
    ("Brian Gittins and Friends", "https://feeds.acast.com/public/shows/brian-gittins-and-friends"),
    ("World War II Tom Hanks", "https://feeds.simplecast.com/wwii_tom_hanks"),
    ("Broken Record", "https://feeds.simplecast.com/brokenrecord"),
    ("Adam Friedland Show", "https://feeds.simplecast.com/adamfriedland"),
    ("Heavyweight Gimlet", "https://feeds.simplecast.com/heavyweight"),
    ("Learn Czech CzechClass101", "https://www.czechclass101.com/feed/podcast/"),
    ("Gardeners Question Time", "https://podcasts.files.bbci.co.uk/b006tp52.rss"),
    ("Great Lives BBC", "https://podcasts.files.bbci.co.uk/b007qlvb.rss"),
    ("70mm podcast", "https://feeds.simplecast.com/70mm"),
    ("How Do You Cope", "https://feeds.simplecast.com/howdoyoucope"),
    ("Where Should We Begin Esther Perel", "https://feeds.simplecast.com/whereshouldwebegin"),
    ("The Audio Long Read Guardian", "https://feeds.guardian.co.uk/audio-long-reads/rss"),
    ("The Luke and Pete Show", "https://feeds.acast.com/public/shows/the-luke-and-pete-show"),
    ("The Upshot", "https://feeds.simplecast.com/theupshot"),
    ("Football Ramble", "https://feeds.acast.com/public/shows/the-football-ramble"),
    ("Cestina s Michalem", "https://feeds.simplecast.com/cestinasmichalem"),
    ("Vinohradska 12", "https://feeds.simplecast.com/vinohradska12"),
    ("The Vergecast", "https://feeds.megaphone.fm/vergecast"),
    ("Fresh Air NPR", "https://feeds.npr.org/381444908/podcast.xml"),
    ("Great Lives", "https://podcasts.files.bbci.co.uk/b007qlvb.rss"),
    ("The Thing About Arsenal", "https://feeds.acast.com/public/shows/the-thing-about-arsenal"),
    ("Stadio Football Podcast", "https://feeds.acast.com/public/shows/stadio"),
    ("Handbrake Off Athletic Arsenal", "https://feeds.acast.com/public/shows/handbrake-off"),
    ("Czechia in 30 minutes", "https://feeds.simplecast.com/czechia30"),
    ("The Athletic FC Podcast", "https://feeds.acast.com/public/shows/the-athletic-fc"),
    ("Economist Podcasts", "https://rss.acast.com/theeconomistmorningbriefing"),
    ("Josh Widdicombe Archive", "https://feeds.acast.com/public/shows/josh-widdicombes-archive-of-pop-culture"),
]

OUTPUT_FILE = "podcast_daily.m3u"

def get_latest_episode(name, url):
    try:
        feed = feedparser.parse(url)
        if not feed.entries:
            return None
        entry = feed.entries[0]
        audio_url = None
        if hasattr(entry, 'enclosures') and entry.enclosures:
            audio_url = entry.enclosures[0].get('href') or entry.enclosures[0].get('url')
        if not audio_url:
            return None
        pub = entry.get('published_parsed') or entry.get('updated_parsed')
        if pub:
            dt = datetime(*pub[:6], tzinfo=timezone.utc)
        else:
            dt = datetime.min.replace(tzinfo=timezone.utc)
        title = entry.get('title', name)
        return (dt, name, title, audio_url)
    except Exception as e:
        print(f"Error fetching {name}: {e}")
        return None

seen_shows = set()
episodes = []
for name, url in FEEDS:
    if name in seen_shows:
        continue
    seen_shows.add(name)
    ep = get_latest_episode(name, url)
    if ep:
        episodes.append(ep)

episodes.sort(key=lambda x: x[0], reverse=True)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("#EXTM3U\n")
    for dt, show, title, audio_url in episodes:
        f.write(f"#EXTINF:-1,{show} - {title} [{dt.strftime('%d %b %Y')}]\n")
        f.write(f"{audio_url}\n")

print(f"Done - {len(episodes)} episodes written to {OUTPUT_FILE}")
