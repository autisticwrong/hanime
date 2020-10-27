# hanime
This a side project on a hanime scraper im making. basically its a discord bot that sends images of the most recent hentai on hanime. code is pretty messy. I might implement this to the main project where it downloads images to a folder.

# General Usage:
from scraper.hanime import Hanime

config = {
  "target_path": './images/'
}

Hanime(config).run()
