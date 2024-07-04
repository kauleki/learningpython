import qrcode

firm_registered_office = "उद्योग तथा वाणिज्य कार्यालय, चितवन"
firm_name = "गौरदेव प्रिन्टर्स"
reg_number = "२३४१/०८०/०८१"
reg_date = "२०८०/०३/१७"
owner_name = "देवकी अधिकारी मैनाली"
firms_address = "भरतपुर महानगरपालिका ४, त्रिचोक, चितवन"
related_purpose = "प्रिप्रेस डिजाइन तथा स्क्रिन प्रिन्ट सम्बन्धी काम गर्ने"
firm_valid_to = "फर्म दर्ता भएको मितिले ५ वर्षसम्म"
detail = (f"फर्मको नाम : {firm_name} \n फर्म दर्ता नम्बर : {reg_number} \n फर्म दर्ता मिति : {reg_date} \n प्रोप्राइटरको नाम : {owner_name} \n"
        f"फर्मको ठेगाना : {firms_address} \n फर्मको उद्देश्य : {related_purpose}\n अध्यावधिक अवधि : {firm_valid_to}\n"
        f"फर्म दर्ता भएको कार्यालय : {firm_registered_office}")
img = qrcode.make(detail)
type(img)
img.save("reg_detail.png")