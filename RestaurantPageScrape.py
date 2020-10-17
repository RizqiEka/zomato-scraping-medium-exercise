# Initialize Empty List that we will use to store the scraping data results
rest_name = []
rest_type = []
rest_area = []
rest_rating = []
rest_review = []
price_for_2 = []
rest_address = []
rest_info = []
rest_lat = []
rest_long = []

# Initialize Webdriver
driver = webdriver.Chrome(chromepath)

# Scrape the data by looping through entries in DataFrame
for url in out_df_nd['Website']:
    driver.get(url)
    time.sleep(6)
    print('Accessing Webpage OK')

    #Restaurant Name
    try:
        name_anchor = driver.find_element_by_tag_name('h1')
        name = name_anchor.text
        rest_name.append(name)
    except NoSuchElementException:
        name = "404 Error"
        rest_name.append(name)
        pass

    print(f'Scraping Restaurant Name - {name} - OK')

    #Restaurant Type
    rest_type_list = []
    rest_type_eltlist = driver.find_elements_by_xpath("""/html/body/div[1]/div[2]/main/div/section[3]/section/section[1]/section[1]/div/a""")


    for rest_type_anchor in rest_type_eltlist:
        rest_type_text = rest_type_anchor.text
        rest_type_list.append(rest_type_text)

    rest_type.append(rest_type_list)
    print(f'Scraping Restaurant Type - {name} - {rest_type_text} - OK')

    #Restaurant Area
    rest_area_anchor = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[3]/section/section[1]/section[1]/a""")
    rest_area_text = rest_area_anchor.text
    rest_area.append(rest_area_text)
    print(f'Scraping Restaurant Area - {name} - {rest_area_text} - OK')

    #Restaurant Rating
    try:
        rest_rating_anchor = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[3]/section/section[2]/section/div[1]/p""")
        rest_rating_text = rest_rating_anchor.text
    except NoSuchElementException:
        rest_rating_text = "Not Rated Yet"
        pass

    rest_rating.append(rest_rating_text)
    print(f'Scraping Restaurant Rating - {name} - {rest_rating_text} - OK')

    #Restaurant Review
    try:
        rest_review_anchor = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[3]/section/section[2]/section/div[2]/p""")
        rest_review_text = rest_review_anchor.text
    except NoSuchElementException:
        rest_review_text = "Not Reviewed Yet"
        pass

    rest_review.append(rest_review_text)
    print(f'Scraping Restaurant Review Counts - {name} - {rest_review_text} - OK')


    #Restaurant Price for 2
    try:
        price_for_2_anchor = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[4]/section/section/article[1]/section[2]/p[1]""")
        price_for_2_text = price_for_2_anchor.text

    except NoSuchElementException:
        price_for_2_text = "No Price Data Found"
        pass   

    price_for_2.append(price_for_2_text)
    print(f'Scraping Restaurant Price for Two - {name} - {price_for_2_text} - OK')

    #Restaurant Address
    rest_address_anchor = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[4]/section/article/section/p""")
    rest_address_text = rest_address_anchor.text
    rest_address.append(rest_address_text)
    print(f'Scraping Restaurant Address - {rest_address_text} - OK')

    #Restaurant Additional Information
    addt_info_list = []
    addt_info_bigelt = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[4]/section/section/article[1]/section[2]/div[3]""")
    addt_info_eltlist = addt_info_bigelt.find_elements_by_tag_name('p')

    for addt_info_anchor in addt_info_eltlist:
        addt_info_text = addt_info_anchor.text
        addt_info_list.append(addt_info_text)

    rest_info.append(addt_info_list)
    print(f'Scraping Restaurant Additional Info - {name} - {addt_info_text} - OK')

    #Restaurant Latitude and Longitude
    map_url = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/main/div/section[4]/section/article/section/div[2]/a""").get_attribute("href")
    lat = map_url[-28:-15]
    long = map_url[-14:-1]
    rest_lat.append(lat)
    rest_long.append(long)
    print(f'Scraping Restaurant Latitude-Longitude - {name} - {lat} - {long} - OK')

    print('-------------------------------------------------------------------------------------------------------------------------------------------')


driver.close()
