import sys
import logging
from pysitemap import crawler

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    # root_url = sys.argv[1]
    # root_url1 = input('Input URL:- ')
    root_url1 = 'classcentral.com'
    root_url = 'https://'+root_url1
    # print()
    crawler(root_url, out_file=root_url1+'-sitemap.xml')
    # a = crawler(root_url)
    # print(str(a))
