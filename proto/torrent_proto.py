# import libtorrent as lt
import time


def add_torrent(magnet_link):
    ses = lt.session()
    params = { 'save_path': 'C:\Users\Eugene\Downloads'}
    link = magnet_link
    handle = lt.add_magnet_uri(ses, link, params)

    print 'downloading metadata...'
    while (not handle.has_metadata()): time.sleep(1)
    print handle.status()
    print 'got metadata, starting torrent download...'
    while (handle.status().state != lt.torrent_status.seeding):
        pass
        # print '%d %% done' % (handle.status().progress*100)
        # time.sleep(1)
    return 1