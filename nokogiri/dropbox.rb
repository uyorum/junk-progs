require 'nokogiri'
require 'open-uri'

url = 'https://www.dropbox.com/ja/install?os=linux'
uri = URI(url)
base_url = uri.scheme + '://' + uri.host

links = {}
Nokogiri::HTML.parse(open(url)).xpath('//table[@class="linux-download-table"]/tr').each do |tr|
  os = tr.xpath('td')[2].text.match(/^(\w+) \(/)
  next unless os
  hrefs = {}
  tr.xpath('td/a[@href]').each do |h|
    hrefs['x86_64'] = base_url + h.get_attribute('href') if h.text =~ /^64/
    hrefs['i386'] = base_url + h.get_attribute('href') if h.text =~ /^32/
  end
  links[os[1].downcase] = hrefs
end
puts links
