tldlist
=======

A crawler to fetch and parse from http://www.iana.org/domains/root/db .

Total : 750 TLDs ( new gTLDs , "traditional" gTLDS , ccTLDs , test TLDs , idn TLDs) 

### Caution: ###


Due to some unpredictable errors (Mostly Network Errors),

I recommend you to run **ONE function** **each time**.

You could also fork my results directly .


### Usage: ###

1.Run tld_list() function , get tld list in brief(tldlist.txt)

return following lines .
>.ac --  -- country-code -- http://www.iana.org/domains/root/db/ac.html

2.Run tld_parser() function , get tld information in details (tldall.txt)

return following lines .
> .ac --  -- country-code -- http://www.iana.org/domains/root/db/ac.html -- http://www.nic.ac/ -- whois.nic.ac

3.Run following codes , create a xml file. (tldlist.xml)

return following xml .

    <?xml version="1.0" ?>
	<tldlist>
		<tld id="661">
			<domain>.我爱你</domain>
			<idn>xn--6qq986b3x</idn>
			<type>generic</type>
			<nic>http://www.zodiacregistry.com</nic>
			<whois>whois.gtld.knet.cn</whois>
		</tld>
		'''
	</tldlist>

