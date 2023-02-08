from autoscraper import AutoScraper
am_url="https://www.amazon.in/s?k=neckband&crid=6GC9YVYYJYNH&sprefix=neck%2Caps%2C373&ref=nb_sb_ss_ts-doa-p_2_4"
want_list=["boAt Rockerz 255 Pro+ in-Ear Bluetooth Neckband with Upto 40 Hours Playback, ASAP Charge, IPX7, Dual Pairing, BT v5.0, with Mic (Teal Green)","₹1,299"]
s=AutoScraper()
res=s.build(am_url,want_list)

# s.get_result_similar(am_url,grouped=True)
print(s.get_result_similar(am_url,grouped=True))