from scraper.hanime import Hanime

config = {
  "target_path": './images/'
}

hanime = Hanime(config)
hanime.run()
hanime.download()

#This downloads imaages from https://hanime.tv/browse/images and puts in a folder
