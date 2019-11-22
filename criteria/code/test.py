import re
import exrex

pattern1 = '(Hello|Hey|Hi|Howdy|Greetings) my (0\\.1|0\\.2|3\\.3|5\\.5)\.'
pattern2 = 'Have you seen my favorite (movie|film) - (The Fight Club|Pirates of Caribbean|Mr\. Nobody|The Matrix|Hackers)\? '
pattern3 = 'I highly recommend it!'

pattern = pattern1 + pattern2 + pattern3

p = '(the use of (a|b)|hello) is at least (\d|\d{2}) (week(s| )|month|year(s| ))'

obj = exrex.getone(p)

print obj


