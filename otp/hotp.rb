#!/usr/bin/env ruby

require 'openssl'

secret = '12345678901234567890'
count = 1
digit = 6

count_in_byte = ''
for i in (0..7)
  count_in_byte = ((count & 0xff) << (8 * i)).chr + count_in_byte
  count >>= 8
end

hmac = OpenSSL::HMAC.digest('sha1', secret, count_in_byte)
offset = hmac[-1].ord & 0xf
num = (hmac[offset].ord & 0x7f) << 24 |
      (hmac[offset + 1].ord & 0xff) << 16 |
      (hmac[offset + 2].ord & 0xff) << 8 |
      (hmac[offset + 3].ord & 0xff)
puts num % (10 ** digit)
