import time
from urllib.request import Request, urlopen
import concurrent.futures


def check_link(link):
    try:
        request = Request(
            link,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        response = urlopen(request, timeout=5)
        code = response.code
        print(code)
        response.close()
    except Exception as e:
        print("Exception occured. URL: ", link, "Exception:", e)


links = open('res.txt', encoding='utf8').read().split('\n')
worker_count = 5
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
    future_to_url = {executor.submit(check_link, url): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
end_time = time.time()

print(end_time - start_time)
