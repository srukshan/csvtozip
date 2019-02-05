# csvtozip
Download All the links in a csv and zip all the files

This Downloader will iterate over all the links in the csv and download the files to the specified location. Then it will zip the downloaded files, in the given destination.

This is using a thread pool to download files real fast, approximatly 10 files per second if file size is low as 1 mb.

Imported Libraries,
  csv
  os
  multiprocessing -> Pool
  itertools -> product
  shutil -> make_archive
  requests

It is my pleasure if anyone found this helpful.
Thank you.
