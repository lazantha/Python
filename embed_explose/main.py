import re

# \d=0-9
# \w=A-Z,a-z,0-9

string='hellow ben10'
digits=re.findall('\w{4}',string)



embed='<iframe width="560" height="315" src="https://www.youtube.com/embed/ly36kn0ug4k?si=AXeW8lMKIvy0Tplp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
embed_2='<iframe width="560" height="315" src="https://www.youtube.com/embed/p1QU3kLFPdg?si=MJ4FZEVjCAZmc_E5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

tokens=embed_2.split()
path=(tokens[3])
url_src = path.split('"')
print(url_src[1])
