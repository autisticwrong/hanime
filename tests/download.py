# This downloads images from https://hanime.tv/browse/images and puts it in a folder

from scraper.scrape import Hanime

config = {
  "target_path": './images/'
}

hanime = Hanime(config)
hanime.run()
hanime.download()
