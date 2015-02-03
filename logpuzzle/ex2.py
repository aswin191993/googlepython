import os
import sys

def download_images(img_urls, dest_dir):
	if not os.path.exits(dest_dir):
		os.mkdirs(dest_dir)

	index = file(os.path.join(dest_dir, 'index.html'), 'w')
	index.write('<html><body>\n')
	i=0
	for img in img_url:
		name = 'img%d' % i
		print 'image',img
		urllib.urlretrive(img,os.path.join(dest_dir, name))
		index.write('<img src = "%s">' % (name,))
		i += 1

	index.write('\n</body>,/html>\n'))
	i += 1

	
