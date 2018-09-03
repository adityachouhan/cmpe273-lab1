import grequests

urls = ['https://webhook.site/f377a059-1c83-4ebd-80ce-007de6067d25',
'https://webhook.site/f377a059-1c83-4ebd-80ce-007de6067d25','https://webhook.site/f377a059-1c83-4ebd-80ce-007de6067d25'
]
rs = (grequests.get(u) for u in urls)
t = grequests.map(rs)
print(t)
